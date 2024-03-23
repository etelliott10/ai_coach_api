from openai import OpenAI
# from fast_whisper import whisper
from faster_whisper import WhisperModel
from eleven_labs import text_to_voice

import pyaudio
import wave
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_audio_file():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    try: 
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("myrecording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    return "myrecording.wav"

def whisper(audio_file_name):
    model_size = "tiny"
    # Initialize the WhisperModel
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    segments, info = model.transcribe(audio_file_name, beam_size=5)
    
    # Combine the transcribed segments into a single text
    text = ''.join(segment.text for segment in segments)
    print(text)
    return text

def open_ai_conversation(user_input):
    # Set your OpenAI API key
    OpenAI.api_key = OPENAI_API_KEY
    
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a judge for grading public speaker's elevator pitch. You give them positive and negative feedback. Look for words that need to be changed. give a suggestion on what the user should say."},
            {"role": "user", "content": user_input}
        ]
    )
    content = completion.choices[0].message.content
    print(content)
    return content

if __name__ == "__main__":
    while True:
        text_to_voice("Do you want to start recording? (yes or no): ")
        
        user_choice = input("Do you want to start recording? (yes or no): ").lower().strip()

        if user_choice == "no":
            print("Exiting the chat.")
            break
        
        elif user_choice == "yes":
            audio_file_name = create_audio_file()
            text_user_input = whisper(audio_file_name)
            response = open_ai_conversation(text_user_input)
            text_to_voice(response)
            
            # Perform further actions with the response if needed
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'quit'.")
