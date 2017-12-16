from flask import request, Flask, render_template
import requests
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
	return "You Cant't See Me"

@app.route('/fake-fishing')
def fake():
	lookup = 'http://ip-api.com/json/{ip}?fields=520191&lang=en'
	#agent = request.headers.get('User-Agent')
	try:
		#heroku request.headers['X-Forwarded-For']
		#origin request.remote_addr
		ip = request.headers['X-Forwarded-For'].split(',')[0]
		browser = request.user_agent.browser
		agent = request.headers.get('User-Agent').split('(')[1].split(')')[0]
		version = request.user_agent.version
		r = requests.get(lookup.format(ip=ip))
		get = json.loads(r.text)
		country = get['country']+', '+get['city']
		return render_template('index.html', version=version,browser=browser,agent=agent,ip=ip,country=country)
		#return '你用的裝置：{agent}\n瀏覽器：{browser}({version})\n你的IP：{ip}\n來自於{country}'.format(version=version,browser=browser,agent=agent,ip=ip,country=country)
	except:
		return '噴Error囉。',500
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=False)
