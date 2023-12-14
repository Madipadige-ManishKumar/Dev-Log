import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0])
# Set the speed (rate)
speed = engine.getProperty('rate')   # Get the current speed (rate)
engine.setProperty('rate', speed - 47)  # Increase the speed by 50
# Set the language
engine.setProperty('voice', 'english-in')
engine.save_to_file("Master Maanish You Have E cet Exam on sixth may  you have just 5 days after your semster exam so get up and prepare  for the exam . Leave Yesterday Failure or Success.Today is Other Day So Try Hard","C:\\Programming_Files\\Html_file\\Html_College\\alarm.mp3")
engine.runAndWait()