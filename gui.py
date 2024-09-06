from flask import Flask, render_template, jsonify, request
from waitress import serve
import os
import asyncio
from characterai import aiocai
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
from whisper import load_model
from pydub import AudioSegment
from multiprocessing import Process

client_eleven = ElevenLabs(
    api_key=os.getenv('ELEVENLABS_API'),
)

app = Flask(__name__)

# Load Whisper model
whisper_model = load_model("small.en")

# Homepage
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# About Page
@app.route('/about/')
def about():
    return "About page is open will fix it"

# Helper functions for AI
def has_common_word(sentence, word_list):
    words = sentence.split()
    for word in words:
        if word in word_list:
            return True
    return False

def generate_audio(message):
    audio = client_eleven.generate(
        text=message,
        voice="OYTbf65OHHFELVut7v2H",
        model='eleven_turbo_v2',
    )
    return audio

async def ai(transcription):
    char = "jIjYwp1Ke8wmsYWFmZsOkqP_5_YqqnPCw-pObjJyRBA"
    client = aiocai.Client(os.getenv('CAI'))

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )
        bye = ['bye', 'goodbye', 'exit', 'close']
        open_list = ['open', 'start', 'launch', 'run']

        # Process transcription
        result = transcription.lower()
        message = await chat.send_message(char, new.chat_id, result)
        print(f'{message.name}: {message.text}')
        
        # Generate audio response
        audio_response = generate_audio(message.text)
        play(audio_response)
        
        if has_common_word(result, bye):
            return jsonify({"status": "AI session closed", "response": message.text}), 200
        if has_common_word(result, open_list):
            open(result, match_closest=True, output=False)

        return jsonify({"status": "AI responded", "response": message.text}), 200

# Route to handle audio file uploads
@app.route('/audio', methods=['POST'])
def upload_audio():
    # Check if the post request has the file part
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    
    file = request.files['audio']

    # If user does not select a file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file temporarily
    file_path = os.path.join('temp', file.filename)
    file.save(file_path)

    # Load audio file and transcribe it using Whisper
    audio = AudioSegment.from_file(file_path)
    transcription = whisper_model.transcribe(file_path)['text']
    print(f'Transcription: {transcription}')

    # Process transcription with AI asynchronously
    response = asyncio.run(ai(transcription))
    
    # Clean up temporary file
    os.remove(file_path)

    return response

# Status route
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Server running"}), 200

if __name__ == "__main__":
    # Run the app
    app.run(debug=True)
