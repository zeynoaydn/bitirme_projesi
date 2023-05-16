from flask import Flask
from flask_restful import Resource, Api
from controllers import *
from route import rota_ekle

app = Flask(__name__)
api = Api(app)
RESULT_FOLDER="/result"
app.config["RESULT_FOLDER"]=RESULT_FOLDER


#### Rotalar

rota_ekle(api, ImageController, '/ImageEdit/<string:operation>')

#### Rotalar

if __name__ == '__main__':
    app.run(debug=True)