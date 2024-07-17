from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs
import requests
from dotenv import load_dotenv
import requests
import os
# Load variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment variables
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

client = ElevenLabs(
  api_key=ELEVEN_LABS_API_KEY, # Defaults to ELEVEN_API_KEY
)
# Define the API endpoint
url = "https://api.elevenlabs.io/v1/text-to-speech/FjgI3kfCCF7asWkUpSJ3"

# Define the headers
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ELEVEN_LABS_API_KEY  # Replace with your Eleven Labs API key
}

# Alex
# voice_id = 'FjgI3kfCCF7asWkUpSJ3'
# Natalie
# voice_id = 'ngvnNeEwGzQ3hAEheUbD'
# Momma Sasha
voice_id = 'KMPlsPuVrgLVDgEQrRJK'

def text_to_voice(ai_text):
    # Define the data (text to convert to speech)
    data = {
        "text": ai_text,
        # "voice": Voice(
        #     voice_id='EXAVITQu4vr4xnSDxMaL',
        #     settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        # ),
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    # Make the POST request to generate audio
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Plays the audio 
        audio_data = response.content
        play(audio_data)
    else:
        print("Failed to generate audio:", response.text)