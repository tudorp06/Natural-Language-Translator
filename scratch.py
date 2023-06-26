import openai
import gradio as gr

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "You are an AI model that is going to translate code from any programming language into natural language so that the average human can understand it. If the user will ask you any question that is not related to code, programming, or maths, you will act like a good AI and pretend that you do not know the answer to that question and that he should ask you about code instead."})

def CustomChatGPT(code):
    messages.append({"role": "user", "content": code})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role" : "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo_web = gr.Interface(fn=CustomChatGPT, inputs=gr.inputs.Textbox(lines = 2, placeholder="Your code goes here: "), outputs=gr.outputs.Textbox(), title = "Natural Language Translator", theme = gr.themes.Soft(), favicon= 'C:/eu/picon.ico')

demo_web.launch(share = True)