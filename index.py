from src import init_app
from config import config
from flask import render_template,request, redirect,url_for


configuration = config['development']

app = init_app(configuration)



@app.route('/')
def index():
    return render_template('index.html')
 


if __name__ == '__main__':
 app.run()
