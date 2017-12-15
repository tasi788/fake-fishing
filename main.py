from flask import request
from flask import Flask
import requests
import json

app = Flask(__name__)
lookup = 'http://ip-api.com/json/{ip}?fields=520191&lang=en'
@app.route('/')
def hello_world():
    agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    try:
        r = requests.get(lookup.format(ip=ip))
        get = json.loads(r.text)
        country = get['country']+get['city']
        return '你用的裝置是{agent}\n你的IP是{ip}\n來自於{country}'.format(agent=agent,ip=ip,country=country)
    except:
        return '你用的裝置是{agent}\n你的IP是{ip}'.format(agent=agent,ip=ip)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))