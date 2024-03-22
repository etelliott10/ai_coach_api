import requests
import subprocess
import os
from dotenv import load_dotenv
import requests

# Load variables from the .env file
load_dotenv()
voice_id = 'FjgI3kfCCF7asWkUpSJ3'
# Access the OpenAI API key from the environment variables
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
url ='https://api.elevenlabs.io/v1/text-to-speech/'+voice_id
# url = 'https://api.elevenlabs.io/v1/text-to-speech/pQuCyW4WMgrIdomn3uS4/stream'
headers = {
    'accept': '*/*',
    'xi-api-key': ELEVEN_LABS_API_KEY,
    'Content-Type': 'application/json'
}
data = {
    'text': 'This is pretty fast huh?! Look at me talking away! doo doo doo.',
    'voice_settings': {
        'stability': 0.50,
        'similarity_boost': 0.30
    }
}

# response = requests.post(url, headers=headers, json=data, stream=True)
# response.raise_for_status()

# # use subprocess to pipe the audio data to ffplay and play it
# ffplay_cmd = ['ffplay', '-autoexit', '-']
# ffplay_proc = subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE)
# for chunk in response.iter_content(chunk_size=4096):
#     ffplay_proc.stdin.write(chunk)
#     print("Downloading...")

# # close the ffplay process when finished
# ffplay_proc.stdin.close()
# ffplay_proc.wait()

def labs_text_to_voice(ai_text):
    data = {
    'text': ai_text,
        'voice_settings': {
            'stability': 0.50,
            'similarity_boost': 0.30
        }
    }

    response = requests.post(url, headers=headers, json=data, stream=True)
    response.raise_for_status()

    # use subprocess to pipe the audio data to ffplay and play it
    ffplay_cmd = ['ffplay', '-autoexit', '-']
    ffplay_proc = subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE)
    for chunk in response.iter_content(chunk_size=4096):
        ffplay_proc.stdin.write(chunk)
        print("Downloading...")

    # close the ffplay process when finished
    ffplay_proc.stdin.close()
    ffplay_proc.wait()