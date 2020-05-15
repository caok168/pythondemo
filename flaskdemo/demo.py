import flask
from flask import render_template,redirect,url_for

app = flask.Flask(__name__, static_folder='./static', static_url_path='', template_folder='./static')

@app.route('/',methods=['GET'])
def search():
    print("test")
    return render_template('index.html')

if __name__ == "__main__":
    app.run()