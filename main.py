from flask import request
from flask import Flask
import requests
import json
import os

app = Flask(__name__)
lookup = 'http://ip-api.com/json/{ip}?fields=520191&lang=en'
@app.route('/')
def hello_world():
    #agent = request.headers.get('User-Agent')
    try:
        #heroku request.headers['X-Forwarded-For']
        #origin request.remote_addr
        ip = request.headers['X-Forwarded-For']
        browser = request.headers.browser
        agent = user_agent.platform
        version = user_agent.version
        r = requests.get(lookup.format(ip=ip))
        get = json.loads(r.text)
        country = get['country']+', '+get['city']
        return '你用的裝置：{agent}\n瀏覽器：{browser}({version})\n你的IP：{ip}\n來自於{country}'.format(version=version,browser=browser,agent=agent,ip=ip,country=country)
    except:
        return 'something got error'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))