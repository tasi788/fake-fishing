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
        browser = request.user_agent.browser
        agent = request.headers.get('User-Agent').split('(')[1].split(')')[0]
        version = request.user_agent.version
        r = requests.get(lookup.format(ip=ip))
        get = json.loads(r.text)
        country = get['country']+', '+get['city']
        return '你用的裝置：{agent}\n瀏覽器：{browser}({version})\n你的IP：{ip}\n來自於{country}'.format(version=version,browser=browser,agent=agent,ip=ip,country=country)
    except:
        #raise
        return 'something got error'
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=int(os.environ.get('PORT', 5000)))
