from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    api_url = 'https://k6t1cu3qp7.execute-api.eu-west-1.amazonaws.com/items'  # Replace with the URL of the API you are using
    response = requests.get(api_url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()