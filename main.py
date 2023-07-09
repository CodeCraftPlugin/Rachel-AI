from whisper_mic.whisper_mic import WhisperMic
from characterai import PyCAI
from elevenlabs import generate, play,set_api_key
from AppOpener import open as op

import os
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
    client = PyCAI(os.getenv('CAI'))
    mic = WhisperMic(model="small.en",device="cpu",)
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
        elif has_common_word(result, search):
                result = search_wiki(result, message)
                break
        if has_common_word(result, open):
            app_name = result.replace("open ","")
            op(app_name,match_closest=True,output=False) # App will be open be it matches little bit too
            break

def search_wiki(result, message):
    import wikipedia
    result = ' '.join(result)
    print(result)
    try:
        search_results = wikipedia.search(result)
        if search_results:
            print("Search results:")
            for wiki_result in search_results:
                print("- ", wiki_result)
                audio = generate_audio(message)
                play(audio)                            
        else:
            print("No results found.")
    except wikipedia.exceptions.WikipediaException as e:
        print("Error occurred: ", str(e))
    return result

def generate_audio(message):
    audio = generate( 
            text=message,
            voice="Rachel",
            model='eleven_monolingual_v1'
        )
    
    return audio
        
if __name__ == "__main__":
    generate_audio("Hello greating user Your are using Rachel By CodeCraft Studios")
    main()
