from flask import Flask, request, render_template
from pyhipku import encode
import re

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def iphaiku():
    if request.method == "GET":
        try:
            IPADDRESS = request.headers.get('X-Forwarded-For', request.remote_addr)
            haiku = re.sub('\n', '<br>', (encode(IPADDRESS)))
            return render_template('index.html', haiku=haiku, ip=IPADDRESS)
        except:
            return("didn't work")
