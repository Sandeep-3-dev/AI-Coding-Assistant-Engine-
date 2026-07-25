from google import genai
from dotenv import load_dotenv

load_dotenv()

client=genai.Client()

#def models_list():
#     for models in client.models.list():
#     print(models.name+"\n")

def chat_bot(user_input):

        try:
            
            response=client.models.generate_content(
                model="models/gemini-3.1-flash-lite",
                contents=user_input
            )

            return response.text

        except Exception as e:
            return f"An error occurred: {e}"



