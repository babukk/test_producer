
from flask import Flask, request, abort
from flask_restful import  reqparse, abort, Api, Resource
from rq import Queue
from rq.job import Job

from worker import conn

app = Flask(__name__)
api = Api(app)
rqueue = Queue(connection=conn)

# ----------------------------------------------------------------------------------------------------------------------
def xxx(url):
    print '--------------------------------> url = ' + url
    pass


# ----------------------------------------------------------------------------------------------------------------------
class CreateJobByURL(Resource):
    def post(self):
         args = parser.parse_args()
         print repr(args)
         print 'URL = ' + args['url']
         job = rqueue.enqueue_call(
            func=xxx, args=(args['url'],), result_ttl=5000
         )
         print('job = ' + job.get_id())

         return {'URL': args['url'], 'JOB': job.get_id()}


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
