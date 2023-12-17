""" This file is primarily designed for testing the Agent exclusively and is not an integral part of the project. It can be removed if necessary."""
from Agent import Agent

Input = None
b = True
messages = ""

while(True):
    Response = Agent(Input)
    print(" Agent : ",Response,'\n')

    if(Input == 'END'):
        break
    
    Input = input("\n Input : ")

    messages = messages + '\n' + Input

print(messages)