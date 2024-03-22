from fast_whisper import whisper
from audio import create_audio_file
from open_ai import open_ai_conversation
from eleven_labs import text_to_voice
# from labs import labs_text_to_voice
# Main function for running the chat in a loop until user exits
if __name__ == "__main__":
    while True:
        # Prompt the user for input
        user_choice = input("Do you want to start recording? (yes/no/quit): ").lower().strip()
        
        # Check if the user wants to quit
        if user_choice == "quit":
            print("Exiting the chat.")
            break  # Exit the loop and end the program
        
        # Check if the user wants to start recording
        elif user_choice == "yes":
            audio_file_name = create_audio_file()
            text_user_input = whisper(audio_file_name)
            response = open_ai_conversation(text_user_input)
            # print("Chatbot: ", response)
            text_to_voice(response)
            # labs_text_to_voice(response)
            
        # If user inputs anything other than "yes", prompt again
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'quit'.")



# ## Define a function to create audio file with stop command
# def create_audio_file_with_stop():
#     # Placeholder for stopping condition
#     stop_condition_met = False
    
#     # Iterate until stop condition is met
#     while not stop_condition_met:
#         audio_file_name = create_audio_file()
#         # Check if the audio file creation returned None (indicating stop command)
#         if audio_file_name is None:
#             stop_condition_met = True
#             break
#         text_user_input = whisper(audio_file_name)
#         print('text_user_input:', text_user_input)
#         print('function is stopped')
#         # response = open_ai_conversation(text_user_input)
#         # print("Chatbot: ", response)
        

# # Main function for running the chat in a loop until user exits
# if __name__ == "__main__":
#     create_audio_file_with_stop()
