import speech_recognition as sr	
import pyttsx
import time

def get_voice() :
	
	r = sr.Recognizer()
	m = sr.Microphone()
	try:
#		print("A moment of silence, please...")
		with m as source: r.adjust_for_ambient_noise(source)
		#print("Set minimum energy threshold to {}".format(r.energy_threshold))
		print("Say something!")
		with m as source: audio = r.listen(source)
		print("Got it! Now to recognize it...")
	except :
		print "error"


	print "start"
	# recognize speech using Sphinx
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		v = r.recognize_google(audio)
		print v
		return v
	#	print("Google Speech Recognition thinks you said " + v)
	except sr.UnknownValueError:
		print "error"
	#	print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	#	print("Could not request results from Google Speech Recognition service; {0}".format(e))
		print "error"
		
def send_voice(x):

	engine = pyttsx.init()
	engine.setProperty('rate', 120)

	voices = engine.getProperty('voices')
	engine.say(x)
	engine.runAndWait()




	
def V ():
	b = get_voice()
	if(b == "open the door"):
		send_voice("Yes I will")
		engine = pyttsx.init()
		engine.setProperty('rate', 120)

		voices = engine.getProperty('voices')
		engine.say("Okay Omar"+b)
		
		engine.runAndWait()

	elif(b=="close the door"):
		send_voice("Yes I will")
		engine = pyttsx.init()
		engine.setProperty('rate', 120)

		voices = engine.getProperty('voices')
		engine.say("Yes I will"+b)
		engine.runAndWait()
	
	
		
	

#send_voice("Jack Starting")
time.sleep(1)
#send_voice("Jack in Sleeping Mode")

#send_voice("To wake up me Use My Name 'Jack' ")
while 1 :
	V()
