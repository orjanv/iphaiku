#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from iphaiku import app

if __name__ == '__main__':
  WSGIServer(app, bindAddress = '/tmp/iphaiku-fcgi.sock').run()
