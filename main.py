# coding: utf8

""" imports """
from bottle import run
from src import routing
config = routing.config
app = application = routing.app

import os
os.chdir(os.path.dirname(__file__))

if __name__ == '__main__':
    run(routing.app,
        host=config["host"] or 'localhost',
        port=config["port"] or 8080,
        reloader=True)