from src import init_app
from config import config


configuration = config['development']

app = init_app(configuration)


# configuration.init_app(app)

@app.route('/')
def index():
    return '<h1>Proyecto 7 - María Nadales</h1>'
 


if __name__ == '__main__':
 app.run()
