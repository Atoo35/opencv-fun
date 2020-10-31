# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
with open('sample.txt', 'r') as reader:
    engine.say(reader.read())
    #print(reader.read())
# for voice in voices:
#    engine.setProperty('voice', voice.id) 
#    print(voice.id) # changes the voice
#    engine.say('The quick brown fox jumped over the lazy dog.')
# testing 


engine.runAndWait() 