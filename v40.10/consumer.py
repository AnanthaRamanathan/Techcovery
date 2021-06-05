import os
from flask import Flask, request, render_template
from kafka import KafkaConsumer
import sys
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for




app = Flask(__name__)

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')

@app.route('/get_msg', methods=('GET', 'POST'))
def get_msg():
    print("get msg")
    
    
    #print("creating msg list")
    #msg_list = []

    
    #for message in consumer:
    #    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    #    print(message.value)
    #    #msg_list.append(message.value)
    #    #print (msg_list)
    #   return(message.value)
    #    #return (' '.join(msg_list))
    
    
    for message in consumer:
        #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        slackmsg = message.value
        print(slackmsg)
        return(message.value)
        #return jsonify(slackmsg)
        

    




if __name__ == "__main__":

    app.run(host="localhost", port=5026, debug=True)