from flask import Flask
from flask_restful import Resource, Api
from controllers import *

app = Flask(__name__)
api = Api(app)
RESULT_FOLDER="/result"
app.config["RESULT_FOLDER"]=RESULT_FOLDER


#### Rotalar

api.add_resource(
    ImageController, 
    '/ImageEdit/<string:operation>',
    '/getImage/<string:resim_adi>'
)

#### Rotalar

if __name__ == '__main__':
    app.run(debug=True)