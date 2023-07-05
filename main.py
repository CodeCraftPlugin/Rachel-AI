from whisper_mic.whisper_mic import WhisperMic
from characterai import PyCAI
from elevenlabs import generate, play,set_api_key
from AppOpener import open
import wikipedia
def has_common_word(sentence, word_list):
    words = sentence.split()  # Split the sentence into words
    for word in words:
        if word in word_list:
            return True
    return False

def main():
    bye = ['bye','Bye','goodbye','Goodbye','exit','Exit','close','Close']
    search = ['search','Search','find','Find','look','Look','google','Google','find me','Find me','look for','Look for']
    open=  ['open','Open','start','Start','launch','Launch','run','Run']
    client = PyCAI('b1612d52b4ccce5bcbb51a2d046891ad07ebce17')
    mic = WhisperMic(model="small.en",device="cpu",)
    set_api_key("9d1cf5037b8994ba6f89343beaf40c92")
    run=True
    while run:
        print("listening")
        result = mic.listen()
        print(result)
        adata = client.chat.send_message('jIjYwp1Ke8wmsYWFmZsOkqP_5_YqqnPCw-pObjJyRBA', result)
        message = adata['replies'][0]['text']
        name = adata['src_char']['participant']['name']
        print(f"{name}: {message}")
        audio = generate( 
            text=message,
            voice="Rachel",
            model='eleven_monolingual_v1'
        )
        play(audio)
        if has_common_word(result, bye):
                run=False
                break
        elif has_common_word(result, search):
                result = ' '.join(result)
                print(result)
                wikipedia.search(result)
                break
        if has_common_word(result, open):
            app_name = result.replace("open ","")
            open(app_name,match_closest=True,output=False) # App will be open be it matches little bit too

def UI():
    import tkinter as tk
    
if __name__ == "__main__":
     main()
