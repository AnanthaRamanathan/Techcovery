from slack import RTMClient
import requests

from flask import Flask

app = Flask(__name__)

@RTMClient.run_on(event="message")
def amusebot(**payload):
    
    data = payload["data"]
    
    web_client = payload["web_client"]
    
    bot_id = data.get("bot_id", "")
    



@app.route('/send/<message>', methods=('GET', 'POST'))
def send(message):

    rtm_client = RTMClient(token="xoxb-1733759796176-2065419109941-MsWuhfxIW3bJs03VSFRZwIcN")
    rtm_client.start()
        
    web_client.chat_postMessage(channel="D022D3BA41F", text=message)

    return(message)


if __name__ == "__main__":
    
    app.run(host="localhost", port=5020, debug=True)
    