from characterai import aiocai
import asyncio
from whisper_mic import WhisperMic
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
from AppOpener import open
from pydub.playback import play as pl
from pydub import AudioSegment
import os


client_eleven = ElevenLabs(
    api_key=os.getenv('ELEVENLABS-API'),
)
def has_common_word(sentence, word_list):
    words = sentence.split()  # Split the sentence into words
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
async def main():
    char = "jIjYwp1Ke8wmsYWFmZsOkqP_5_YqqnPCw-pObjJyRBA"

    client = aiocai.Client(os.getenv('CAI'))

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )
        bye = ['bye','Bye','goodbye','Goodbye','exit','Exit','close','Close','Bye!','bye!','bye.','Bye.','goodbye.','Goodbye.','exit.','Exit.','close.','Close']
        open_list=  ['open','Open','start','Start','launch','Launch','run','Run']
        print(f'{answer.name}: {answer.text}')
        mic = WhisperMic(model="small.en",)
        run=True
        while run:            
            print("listening")
            result = mic.listen().lower()
            print(result)
            message = await chat.send_message(
                char, new.chat_id, result
            )
            print(f'{message.name}: {message.text}')
            print(type(message.text))
            audio = generate_audio(message.text)
            play(audio)
            if has_common_word(result, bye):
                run=False
                break
            if has_common_word(result, open_list):
                open(result,match_closest=True,output=False) # App will be open be it matches little bit too

if __name__ == "__main__":
    greet = "greetings.mp3"
    if os.path.exists(greet):
        pl(AudioSegment.from_mp3(greet))
    else:
        Gene = generate_audio("Hello, I am your personal assistant...How can I help you?")
        save(Gene,filename=greet)
        play(Gene)
        print("main thread started")
    asyncio.run(main())

