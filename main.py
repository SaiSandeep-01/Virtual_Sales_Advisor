""" Twilio Calling Module Connectiong the Call with the Agent """

from twilio.twiml.voice_response import VoiceResponse
from flask import Flask , url_for , request , jsonify
from twilio.rest import Client
from flask_cors import CORS
from Agent import Agent as AI_Agent
import urllib.request
import openai
import random
from config import os

app = Flask(__name__)
CORS(app)

class Twilio_Agent :

    def __init__(self):
        """ Initialising Key Variables """
        self.account_sid = os.environ.get("Account_sid")
        self.auth_token = os.environ.get("Auth_token")
        self.openai_api_key = os.environ.get("openai_api")
        self.client = Client(self.account_sid, self.auth_token)

    def transcribe(self, recording_url):
        """
        Transcribes the audio recording using OpenAI Whisper API.

        """
        hash = str(random.getrandbits(32))
        try:
            urllib.request.urlretrieve(recording_url, hash + ".wav")
        except:
            return None
        openai.api_key = self.openai_api_key

        """
        Random names for every recording because to avoid read and write error.

        """
        audio_file = open(hash + ".wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

        """
        Deleting the files as soon as we get the recording because we don't want our system to store the 
        personal recordings 

        """
        audio_file.close()
        os.remove(hash + ".wav") 
        return transcript['text']
        
myAgent = Twilio_Agent()
Phone=''

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST': 
        """ POST request to make a call """
        global Phone

        """ JSON Data Handling """
        data = request.get_json() 
        if 'phone' not in data:
            return jsonify({"message": 'Missing required field "phone"'}), 400
        data = request.get_json() # JSON Data
        Phone = data['phone']

        """ Clearing the Previous Conversation. """
        AI_Agent('clear_convo')

        """ Making a Call to the Provided Number. """
        forward_url = url_for("handle", _external=True)
        call = myAgent.client.calls.create(
            to = "+91" + Phone,
            from_ = os.environ.get("Twilio_no"),
            url= forward_url
        )
        print(call.sid)
        return "__Call_Generated__"

    return "__BACKEND__"


@app.route('/handle',methods=['GET','POST'])
def handle():
    global Qtn_index
    response = VoiceResponse()
    Intro = AI_Agent()
    response.say(Intro)
    """Capturing 5 seconds of audio for user response"""
    response.record(action='/Ongoing',timeout=4, finish_on_key='*',play_beep=False)
    return str(response)

@app.route('/Ongoing', methods=['GET','POST'])
def Ongoing():
    """
    The endpoint for transcribing audio and verbalizing the agent's response.

    """
    recording_url = request.form["RecordingUrl"]
    transcription = Twilio_Agent.transcribe(recording_url)
    if not transcription:
        response = VoiceResponse()
        response.hangup()
        return str(response)

    """ Furnishing User Input to the Agent."""
    AI_response = AI_Agent(transcription)
    
    """ Terminating the call when the agent determines it's time to conclude the conversation. """
    response = VoiceResponse()
    if AI_response == 'END' :
        print(AI_Agent('get_convo')) # To save the Transcript to the database, Add a database And make API request here.
        response.hangup()
        return str(response) 
    
    """ Using Twilio to deliver the Response of the Agent. """
    response.say(AI_response)
    response.record(action='/Ongoing',timeout=4, finish_on_key='*',play_beep=False)
    return str(response)

if __name__ == '__main__':
    app.run(debug=False,host='localhost',port=5000)
    # To facilitate the hosting process, utilize the following line
    # app.run(debug=False,host='0.0.0.0')