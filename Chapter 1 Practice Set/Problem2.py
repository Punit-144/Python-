#Install an External module and perform an operation from that. 
import pyttsx3
engine = pyttsx3.init()
engine.say(" I will repeat the tex writted by you!")
engine.runAndWait()