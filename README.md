# Virtual Sales Advisor

> [!NOTE]
> The Sales Agent was generated using a Large-Language Model and integrated with the Twilio API.

Building a dynamic sales agent empowered by a large-language model and Twilio API integration, facilitated through Flask

## Execute / Run a Demo 
1. Signup on Twilio and retrieve your Twilio Account SID along with the Authentication by visiting Twilio [Login](https://www.twilio.com/login).
2. Purchase a number from Twilio Client that includes a Voice URL. You can refer to this [Video Tutorial](https://www.youtube.com/watch?v=ArYpgZxoF4U) for guidance.
3. Generate an OpenAI API Key by visiting [OpenAI's Website](https://openai.com/).
4. Retrieve the repository by using the command in the Terminal to clone it onto your local computer.

    `
        git clone https://github.com/SaiSandeep-01/Virtual_Sales_Advisor
    `
5. Configure the environment keys in the config.py file.

    `
    Account_sid
    Auth_token
    Twilio_no
    openai_api
    `
6. Install insomnia from this [Link](https://insomnia.rest/download).
7. Install ngrok using the [Link](https://ngrok.com/download) and create a public URL for your localhost port 5000 using the following command in the ngrok CLI

    `
    ngrok.exe http 5000 
    `
8. Launch Insomnia and create a POST request to the PUBLIC URL provided by ngrok. Include a JSON body structured as

    ```
    {
        "user": "Your_Username",
        "phone": "XXXXXXXX",
        "purpose": "Your_Desired_Purpose"
    }
    ```
9. The phone number specified above will soon receive a call. Answer the call and engage in a conversation with the sales agent.
10. The file named agentTester.py is primarily designed for testing the Agent exclusively and is not an integral part of the project. It can be removed if necessary.
11. To modify the operational prerequisites of the Agent, revise all the Conversation Stages and the Dictionary containing the company's information, located at line 222.
12. To enable integration, develop a frontend and initiate an HTTP request through it based on your requirement to the hosted link using the specified JSON format for functional purposes.

## Technology

- Flask
- Langchain
- Twilio API
- OpenAI 

## References

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Langchain](https://python.langchain.com/docs/get_started/introduction)
- [Twilio](https://www.twilio.com/docs)
- [OpenAi](https://platform.openai.com/docs/introduction)
- [Urllib](https://docs.python.org/3/library/urllib.html)
- [Typing](https://docs.python.org/3/library/typing.html)