from typing import Text
from slack import RTMClient
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/receive/<text>', methods=('GET', 'POST'))
def slackmsg (text):
    @RTMClient.run_on(event="message")
    def amusebot(**payload):
        
        data = payload["data"]
        web_client = payload["web_client"]
        bot_id = data.get("bot_id", "")

        # If a message is not send by the bot
        if bot_id == "":
            channel_id = data["channel"]

            # Extracting message send by the user on the slack
            text = data.get("text", "")
            text = text.split(">")[-1].strip()
            print(text)
            

            #response = ""
            #if "help" in text.lower():
            #    user = data.get("user", "")
            #    response = f"Hi <@{user}>! I am AmuseBot :)"
            #else:
            #    activity_json_response = requests.get("http://www.boredapi.com/api/activity/").json()
            #    activity = activity_json_response['activity']
            #    response = str(activity)
            
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)

    try:
        rtm_client = RTMClient(token="xoxb-1733759796176-2065419109941-MsWuhfxIW3bJs03VSFRZwIcN")
        print("Bot is up and running!")
        rtm_client.start()
    except Exception as err:
        print(err)

   

if __name__ == "__main__":
    
    app.run(host="localhost", port=5021, debug=True)
    