#!/usr/bin/Python37

from flask import Flask

class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []



# instantiate the blockchain and call it out
blockchain = Blockchain()

# Installation on the node

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return "hello world"