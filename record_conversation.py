import json
import os
from datetime import datetime

def get_messages():
    # Define the directory path for conversation data
    # Define the directory path
    directory = "json_files"

    # Ensure the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the filename
    filename = "conversation_log.json"

    # Combine the directory path and filename to get the full file path
    file_path = os.path.join(directory, filename)

    
    # Check if the file exists and is not empty
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            # Open and read the JSON file
            with open(file_path) as f:
                data = json.load(f)

            # Return the messages
            return data
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return []
    else:
        print("Conversation log file is empty or doesn't exist.")
        return []
    
    # # Renders a page displaying logged conversations from a JSON file.


def log_conversation(role, message):
    # Create the conversation_data directory if it doesn't exist
    # Define the directory path
    directory = "json_files"

    # Ensure the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the filename
    filename = "conversation_log.json"

    # Combine the directory path and filename to get the full file path
    file_path = os.path.join(directory, filename)


    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a new entry for the user's input or AI response
    log_entry = {
        "role": role,
        "message": message,
        "timestamp": timestamp
    }

    # Load existing data from the file or initialize as an empty list
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, mode='r') as file:
            data = json.load(file)
    else:
        data = []

    # Append the new log entry to the data
    data.append(log_entry)

    # Write the updated data back to the file
    with open(file_path, mode='w') as file:
        json.dump(data, file, indent=4)
    # Explicitly close the file
    file.close()
