import chat
import time
import subprocess
import database

database.create_db()

print("North.")
print("System commands......")
print("'clear' to clear the terminal.")
print("'history' to get full chat history.")
print("'quit' to close the chat.")
print("'delete' to delete complete chat history.\n\n")

while True:
    user_input = input("You: ").strip()

    if user_input == "":
        print("System: Please Enter something.\n")
        continue

    if user_input.lower() == "quit":
        print("System: Goodbye!")
        time.sleep(10)
        break

    if user_input.lower() == "clear":
        subprocess.run(["cls"], shell=True)
        print("North.")
        print("System commands......")
        print("'clear' to clear the terminal.")
        print("'history' to get full chat history.")
        print("'quit' to close the chat.")
        print("'delete' to delete complete chat history.\n\n")
        print("You: ", user_input)
        print("System: Terminal Cleared.\n")
        continue

    if user_input.lower() == "delete":
        database.delete_chats()
        print("System: Chat history cleared.\n")
        continue

    if user_input.lower() == "history":
        all_messages = database.get_all_messages()
        if len(all_messages) == 0:
            print("System: No chat history.\n")
        else:
            print("System: Showing chat history.")
            print("\n--- Chat History ---")
            for msg in all_messages:
                print(msg["role"] + ": " + msg["message"])
            print("--- End ---\n")
        continue

    if len(user_input) > 250:
        print("System: Message too long. Please keep it under 250 characters.\n")
        continue

    print("North: ", end="", flush=True)

    for chunk in chat.stream_response(user_input):
        print(chunk, end="", flush=True)

    print("\n")