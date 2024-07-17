# Import statements (assuming other imports are correct)
from fast_whisper import whisper
from audio import create_audio_file
from open_ai import open_ai_conversation
from eleven_labs import text_to_voice

# Main function for running the chat in a loop until the user exits
while True:
    # Prompt the user for input
    user_choice = input("Do you want to start recording? (yes/no/quit): ").lower().strip()    

    # Checks if the user wants to quit
    if user_choice == "quit":
        print("Exiting the chat.")
        break  # Exit the loop and end the program
        
    # Checks if the user wants to start recording
    elif user_choice == "yes":
        # Attempt to handle exceptions 
        try:
            audio_file_name = create_audio_file()
            text_user_input = whisper(audio_file_name)
            response = open_ai_conversation(text_user_input)
            text_to_voice(response)
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Invalid choice. Please enter 'yes', 'no', or 'quit'.")
