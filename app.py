import os
from speech_synthesis import speak
from speech_capture import recording_input
import openai

openai.api_key ='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'


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

class Chatbot:
    def __init__(self, system_context: str = 'You are a friendly chatbot.') -> None:
        self.context = [
            {'role': 'system', 'content': system_context}
        ]

    def chat(self, user_input: str, debug=False):
        messages = self.context.copy()
        messages.append(
            {'role': 'user', 'content': user_input}
        )
        
        response = get_completion_from_messages(messages, temperature=0)
        print(response)
        
        if debug:
            print('Chat History')
            for message in self.context:
                print(message)
        
        self.context.append(
            {'role': 'user', 'content': user_input}
        )
        self.context.append(
            {'role': 'assistant', 'content': response}
        )
        return response


def converse(user: str, bot: Chatbot):
    user_input = ''
    speak(bot.chat('Hi, my name is {}'.format(user)))
    
    while user_input not in ['Bye.', 'Bye', 'bye.', 'bye', 'byee', 'Byee', 'Goodbye', 'byeee', 'Byeee', 'exit', 'quit']:
        user_input = recording_input()
        response = bot.chat(user_input)
        speak(response)

        
friendly = Chatbot()
converse("Ricky", friendly)

