# # . Can you change the self-parameter inside a class to something else (say
# # “harry”). Try changing self to “slf” or “harry” and see the effects

# import pyjokes

# # Get a random joke in English
# joke = pyjokes.get_joke()

# print(joke)



import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source
with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Optional: adjust for ambient noise
    print("Listening...")
    
    # Capture the audio
    audio = recognizer.listen(source)

# Try to recognize the speech in the audio
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)  # Using Google's API
    print(f"You said: {text}")
    
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
    
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
