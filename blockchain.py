#!/usr/bin/Python37

from flask import Flask, render_template
from time import time

class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []
        # Create a genesis block with nonce and previous hash
        self.create_block(0, '00')

    def create_block(self, nonce, previous_hash):
        """ Adding a block of transactions to the block chain"""
        block = {"block number" : len(self.chain) + 1,
                 "timestamp" : time(),
                 "transactions" : self.transactions,
                "nonce" : nonce,
                "previous_hash" : previous_hash }

        # Now that transactions have been added to the block
        # We clear the transaction list to start a new series
        self.transactions = []
        self.chain.append(block)



# instantiate the blockchain and call it out
blockchain = Blockchain()

# Installation on the node

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5008, type=int, help="port to list to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)