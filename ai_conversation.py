from openai import OpenAI
# from fast_whisper import whisper  # Importing whisper from a commented-out module
from faster_whisper import WhisperModel  # Importing the WhisperModel module
from eleven_labs import text_to_voice  # Importing text_to_voice from the eleven_labs module

import pyaudio  # Library for audio I/O
import wave  # Library for reading and writing WAV files
import os  # Library for interacting with the operating system
from dotenv import load_dotenv  # Loading environment variables from .env files

# Load variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_audio_file():
    """
    Function to record audio and save it as a WAV file.
    """
    audio = pyaudio.PyAudio()  # Initialize PyAudio object
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)  # Open audio stream
    frames = []  # List to store audio frames

    try: 
        while True:  # Continue recording until interrupted
            data = stream.read(1024)  # Read audio data
            frames.append(data)  # Append data to frames list
    except KeyboardInterrupt:
        pass

    stream.stop_stream()  # Stop audio stream
    stream.close()  # Close audio stream
    audio.terminate()  # Terminate PyAudio object

    # Create a WAV file and write audio frames to it
    sound_file = wave.open("myrecording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    return "myrecording.wav"  # Return the filename of the recorded audio

def whisper(audio_file_name):
    """
    Function to transcribe audio using the WhisperModel.
    """
    model_size = "tiny"  # Set model size
    # Initialize the WhisperModel
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    # Transcribe audio file
    segments, info = model.transcribe(audio_file_name, beam_size=5)
    
    # Combine the transcribed segments into a single text
    text = ''.join(segment.text for segment in segments)
    print(text)  # Print transcribed text
    return text  # Return transcribed text

def open_ai_conversation(user_input):
    """
    Function to generate conversation response using OpenAI Chat API.
    """
    # Set your OpenAI API key
    OpenAI.api_key = OPENAI_API_KEY
    
    client = OpenAI()
    # Generate completion using OpenAI Chat API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a judge for grading public speaker's elevator pitch. You give them positive and negative feedback. Look for words that need to be changed. give a suggestion on what the user should say."},
            {"role": "user", "content": user_input}
        ]
    )
    content = completion.choices[0].message.content  # Get generated response
    print(content)  # Print generated response
    return content  # Return generated response

if __name__ == "__main__":
    while True:
        text_to_voice("Do you want to start recording? (yes or no): ")  # Speak prompt
        
        user_choice = input("Do you want to start recording? (yes or no): ").lower().strip()  # Take user input

        if user_choice == "no":
            print("Exiting the chat.")
            break
        
        elif user_choice == "yes":
            audio_file_name = create_audio_file()  # Record audio and get filename
            text_user_input = whisper(audio_file_name)  # Transcribe audio
            response = open_ai_conversation(text_user_input)  # Generate response
            text_to_voice(response)  # Speak response
            
            # Perform further actions with the response if needed
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'quit'.")
