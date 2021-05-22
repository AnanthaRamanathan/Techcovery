from slack import RTMClient
import requests
import json

import os
from flask import Flask, request, render_template

from kafka import KafkaProducer

app = Flask(__name__)








@app.route('/', methods=('GET', 'POST'))
def producer():
    @RTMClient.run_on(event="message")
    def amusebot(**payload):
        
        data = payload["data"]
        #print(data)
        web_client = payload["web_client"]
        #print(web_client)
        bot_id = data.get("bot_id", "")
        #print(bot_id)
        
        # If a message is not send by the bot
        if bot_id == "":
            channel_id = data["channel"]
            print(channel_id)

            bootstrap_servers = ['localhost:9092']
            topicName = 'myTopic'
            producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
            producer = KafkaProducer()

            # Extracting message send by the user on the slack
            text = data.get("text", "")
            text = text.split(">")[-1].strip()
            print(text)

            bootstrap_servers = ['localhost:9092']
            topicName = 'myTopic'
            producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
            producer = KafkaProducer()

            msg = json.dumps(text).encode('utf-8') 
            producer.send(topicName, msg)

            #ack = producer.send(topicName, b'Hello World!!!!!!!!')
            #metadata = ack.get()
            #print(metadata.topic)
            #print(metadata.partition)

                    
            producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('ascii'))
            
           

            

        
            response = "my hardcode response"
            print(response)
            
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)

try:
        rtm_client = RTMClient(token="xoxb-1733759796176-2065419109941-MsWuhfxIW3bJs03VSFRZwIcN")
        print("Bot is up and running!")
        rtm_client.start()
except Exception as err:
        print(err)

    



    

if __name__ == "__main__":

    app.run(host="localhost", port=5025, debug=True)

    