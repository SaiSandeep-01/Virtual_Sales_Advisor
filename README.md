<center><figcaption>Virtual Sales Advisor</figcaption></center>


> Sales Agent With Large-Language Model and Twilio API

Building a dynamic sales agent empowered by a large-language model and Twilio API integration, facilitated through Flask

## Execute/Run a Demo 
1. Signup on Twilio and retrieve your Twilio Account SID along with the Authentication by visiting Twilio [Login](https://www.twilio.com/login).
2. Purchase a number from Twilio Client that includes a Voice URL. You can refer to this [video tutorial](https://www.youtube.com/watch?v=ArYpgZxoF4U) for guidance.
3. Generate an OpenAI API Key by visiting [OpenAI's website]("https://openai.com/").
4. Retrieve the repository by using the command in the Terminal to clone it onto your local computer.

    `
        git clone https://github.com/SaiSandeep-01/Sales_Agent
    `
5. Configure the environment keys in the config.py file.

    `
    Account_sid
    Auth_token
    Twilio_no
    openai_api
    `
6. Install insomnia from this [Link].(https://insomnia.rest/download)
7. Install ngrok using the [Link](https://ngrok.com/download) and create a public URL for your localhost port 5000 using the following command in the ngrok CLI

    `
    ngrok.exe http 5000 
    `
8. Launch Insomnia and create a POST request to the PUBLIC URL provided by ngrok. Include a JSON body structured as

    `
    {
        "user": "Your_Username",
        "phone": "XXXXXXXX",
        "purpose": "Your_Desired_Purpose"
    }
    `
9. The phone number specified above will soon receive a call. Answer the call and engage in a conversation with the sales agent.

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