# coding: utf8

""" imports """
from bottle import run
import routing
config = routing.config

def main():
    run(routing.app,
        host=config["host"] or 'localhost',
        port=config["port"] or 8080,
        reloader=True
    )
pass

if __name__ == '__main__':
    main()