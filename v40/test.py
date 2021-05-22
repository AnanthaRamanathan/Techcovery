import os
from flask import Flask, request, render_template
from kafka import KafkaConsumer
import sys
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for,make_response
from flask_mysqldb import MySQL,MySQLdb 
import queries
import json
from flask import Response



app = Flask(__name__)




@app.route('/test', methods=['GET', 'POST'])
def test():

    data = [
    {
        "name": "Meowsy",
        "species" : "cat",
        "foods": {
        "likes": ["tuna", "catnip"],
        "dislikes": ["ham", "zucchini"]
        }
    },
    {
        "name": "Barky",
        "species" : "dog",
        "foods": {
        "likes": ["bones", "carrots"],
        "dislikes": ["tuna"]
        }
    },
    {
        "name": "Purrpaws",
        "species" : "cat",
        "foods": {
        "likes": ["mice"],
        "dislikes": ["cookies"]
        }
    }
    ]

    
    #return jsonify(data)
    #return json.dumps(data)
    return jsonify({
        "api_stuff": "values",
    })


if __name__ == "__main__":

    app.run(host="localhost", port=5050, debug=True)