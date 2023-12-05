import os
from speech_synthesis import ai_speak
from speech_capture import recording_input
from python_to_xml import create_xml
from speech_emotion import ai_speak2
from botcaseinstr import Case_1_system_instruction, Case_2_system_instruction
import openai

openai.api_key ='ENTER YOUR KEY'


def get_completion_from_messages(messages, model="gpt-4", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

class Chatbot:
    def __init__(self, system_context: str = Case_1_system_instruction) -> None:
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
    ai_speak(bot.chat('Hi, my name is {}'.format(user)))
    
    while user_input not in ['Bye.', 'Bye', 'bye.', 'bye', 'byee', 'Byee', 'Goodbye', 'byeee', 'Byeee', 'exit', 'quit']:
        user_input = recording_input()
        response = bot.chat(user_input)
        create_xml(response)
        ai_speak2(response)

        
friendly = Chatbot()
converse("Ricky", friendly)

