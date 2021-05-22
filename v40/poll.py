running = True

def basic_consume_loop(consumer, myTopic):
    try:
        consumer.subscribe(myTopic)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def shutdown():
    running = False


import os
from flask import Flask, request, render_template
from kafka import KafkaConsumer
import sys



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
        print(message.value)
        return(message.value)

    




if __name__ == "__main__":

    app.run(host="localhost", port=5026, debug=True)