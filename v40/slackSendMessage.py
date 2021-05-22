from slack import RTMClient
import requests

from flask import Flask

app = Flask(__name__)




@app.route('/slack/<message>', methods=('GET', 'POST'))
def slack (message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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', data = payload)
    print(response.text)  
     
    
    return(message)      

@app.route('/slackmsg/<message>', methods=('GET', 'POST'))
def slackmsg (message):
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
            
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id)

    try:
        rtm_client = RTMClient(token="xoxb-1733759796176-2065419109941-MsWuhfxIW3bJs03VSFRZwIcN")
        print("Bot is up and running!")
        rtm_client.start()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    
    app.run(host="localhost", port=5015, debug=True)
    