
from flask import Flask, request, abort
from flask_restful import  reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# ----------------------------------------------------------------------------------------------------------------------
class CreateJobByURL(Resource):
    def post(self):
         args = parser.parse_args()
         print repr(args)
         print 'URL = ' + args['url']
         return {'URL': args['url']}


# ----------------------------------------------------------------------------------------------------------------------
@app.route('/')
def HomePage():
    abort(404)

parser = reqparse.RequestParser()
# parser.add_argument('url', type=str)
parser.add_argument('url', type=str, location=['json', 'form'], required=True)

api.add_resource(CreateJobByURL, '/create_job');

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
