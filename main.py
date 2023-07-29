from whisper_mic.whisper_mic import WhisperMic
from characterai import PyCAI
from elevenlabs import generate, play,set_api_key,save
from AppOpener import open
from pydub.playback import play as pl
from pydub import AudioSegment
from threading import Thread
import os
import gui as g
def has_common_word(sentence, word_list):
    words = sentence.split()  # Split the sentence into words
    for word in words:
        if word in word_list:
            return True
    return False

def main(arg):
    bye = ['bye','Bye','goodbye','Goodbye','exit','Exit','close','Close','Bye!','bye!','bye.','Bye.','goodbye.','Goodbye.','exit.','Exit.','close.','Close']
    open_list=  ['open','Open','start','Start','launch','Launch','run','Run']
    client = PyCAI(os.getenv('CAI'))
    mic = WhisperMic(model="small.en",)
    set_api_key(os.getenv('ELEVENLABS-API'))
    run=True
    while run:
        print("listening")
        result = mic.listen()
        print(result)
        adata = client.chat.send_message('jIjYwp1Ke8wmsYWFmZsOkqP_5_YqqnPCw-pObjJyRBA', result)
        message = adata['replies'][0]['text']
        name = adata['src_char']['participant']['name']
        print(f"{name}: {message}")
        audio = generate_audio(message)
        play(audio)
        if has_common_word(result, bye):
                run=False
                break
        if has_common_word(result, open_list):
            open(result,match_closest=True,output=False) # App will be open be it matches little bit too
            
def generate_audio(message):
    audio = generate( 
            text=message,
            voice="Rachel",
            model='eleven_monolingual_v1'
        )
    
    return audio
        
if __name__ == "__main__":
    greet = "greetings.mp3"
    if os.path.exists(greet):
        pl(AudioSegment.from_mp3(greet))
    else:
        Gene = generate_audio("Hello, I am your personal assistant...How can I help you?")
        save(Gene,filename=greet)
        play(Gene)
        print("main thread started")
    main_thread = Thread(target=main,args=(12,))
    gui_thread = Thread(target=g.gui,args=(12,))
    gui_thread.start()
    main_thread.start()
    g.window.mainloop()
    