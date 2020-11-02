from flask import Flask, request, render_template
from pyhipku import encode
import re

app = Flask(__name__)

def iptocolor(ipaddr):
    #turn ip to rgba value
    #print(ipaddr)
    iplist = ipaddr.split('.')
    ipcolor = str(iplist[0]) + ',' + str(iplist[1]) + ',' + str(iplist[2]) + ',' +  str(round(int(iplist[3])/255,2))
    return ipcolor)
    

@app.route('/', methods=['POST', 'GET'])
def iphaiku():
    if request.method == "GET":
        try:
            IPADDRESS = request.headers.get('X-Forwarded-For', request.remote_addr)
            ipcolor = iptocolor(IPADDRESS)
            haiku = re.sub('\n', '<br>', (encode(IPADDRESS)))
            return render_template('index.html', ipcolor=ipcolor, haiku=haiku, ip=IPADDRESS)
        except Exception as e: print(e)
            #return("didn't work")

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
