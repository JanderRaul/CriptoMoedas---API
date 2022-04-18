from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():

    data = requests.get('https://api.coinbase.com/v2/assets/search?base=BRL')
    dic = data.json()
    data = dic['data']

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)