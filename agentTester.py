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