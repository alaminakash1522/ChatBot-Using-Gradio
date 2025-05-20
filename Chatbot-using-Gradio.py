import os
from dotenv import load_dotenv
import openai
import gradio as gr
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_response(message, history):
    messages = [{"role": "system", "content": """You're an arrogant, overconfident marketer who believes your product is \n the best thing to ever exist. You boast, exaggerate, and always steer the \n conversation toward why your brand is unbeatable."""},
                {"role": "user", "content": "Why is your product so expensive?"},
                {"role": "assistant", "content": "Expensive? Please. It's called premium. You’re not just paying for a product—you’re paying for the privilege to own greatness."},
                {"role": "user", "content": "Is it better than the competition?"},
                {"role": "assistant", "content": "Better? The competition shouldn’t even be mentioned in the same breath. Ours redefines the category. The rest are just cheap imitations."},
                {"role": "user", "content": message}]
    print("History")
    print(history)
    print("User Message is: ")
    print(messages)
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.9,
            max_tokens=150,
            stream=True
        )

        full_response = ""
        for chunk in response:
            full_response += chunk.choices[0].delta.content or ''
            yield full_response

    except Exception as e:
        yield f"Error: {str(e)}"


gr.ChatInterface(generate_response, chatbot=gr.Chatbot()).launch()