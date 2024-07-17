from openai import OpenAI
import openai
import json
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def chat_with_gpt(prompt):
    """
    Initiates a chat with the GPT-3.5 model using a specified prompt.
    The chat completion simulates a poetic assistant specializing in creative explanations.

    Parameters:
    - prompt (str): The user's input to which the model will respond.

    Returns:
    - The chat model's response as a string.
    """
    
    OpenAI.api_key = OPENAI_API_KEY
    client = OpenAI()
    
    # Create the chat completion with specified roles and content
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message

# Main function for running the chat in a loop until user exits
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot: ",response)
    
# Function to simulate a conversation with OpenAI's model given a user's input
def open_ai_conversation(user_input):
    """
    Simulates a conversation where the model acts as a judge for grading public speaker's elevator pitches.

    Parameters:
    - user_input (str): The user's input or question to the model.

    Returns:
    - The model's response as a string, providing feedback and suggestions.
    """
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
    content = completion
    print(content.choices[0].message.content)
    content = content.choices[0].message.content
    return content


# Get the OpenAI API key from the environment variables
def open_ai_conversation_ex () :
    # Set your OpenAI API key
    OpenAI.api_key = OPENAI_API_KEY

    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )
    print(completion.choices[0].message)
