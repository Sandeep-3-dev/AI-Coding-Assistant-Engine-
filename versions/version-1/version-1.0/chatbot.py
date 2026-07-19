from google import genai
from dotenv import load_dotenv

load_dotenv()

def chat_bot():

    client=genai.Client()
#     for models in client.models.list():
#         print(models.name+"\n")
# chat_bot()

    print("Hi! This is a Simple Chatbot .Type 'exit' or 'quit' to end.\n")

    while True:
        try:
            user_input=input("You: ")

            if user_input.strip().lower() in ["exit","quit"]:
                print("Gemini: GoodBye!")
                break

            if not user_input.strip():
                continue

            response=client.models.generate_content(
                model="models/gemini-3.5-flash",
                contents=user_input
            )

            print(f"Gemini: {response.text}\n")

        except Exception as e:
            print(f"An error occured: {e}\n")
            break

if __name__=="__main__":
    chat_bot()


