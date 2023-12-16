from Agent import Agent

Input = None
b = True
messages = ""

while(True):
    Response = Agent(Input , b)
    b=False
    print("Response Generated is : ",Response,'\n')
    
    if(Input == 'END'):
        break
    
    Input = input(" \n Enter Input :    ")
    
    if(Input == 'clear_convo'):
        b=True
    # messages = messages + '\n' + Input

print(messages)