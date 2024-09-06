from flask import Flask, render_template, jsonify, request
from waitress import serve
from pydub import AudioSegment
from pydub.playback import play as pl
import io
import multiprocessing

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return "About page is open, will fix it."

@app.route('/audio', methods=['POST'])
def upload_audio():
    # Check if the post request has the file part
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    
    file = request.files['audio']

    # If user does not select a file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the audio file into an AudioSegment object
        audio_data = AudioSegment.from_file(file, format="webm")

        # Play the audio (this will play the audio on the server side)
        pl(audio_data)

        return jsonify({'message': 'Audio file played successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    pass