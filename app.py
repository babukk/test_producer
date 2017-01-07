
from flask import Flask, request, abort
from flask_restful import  reqparse, abort, Api, Resource
from rq import Queue
from rq.job import Job

from worker import conn
from content_queue import conn

app = Flask(__name__)
api = Api(app)
req_queue = Queue(connection=conn)
con_queue = Queue(connection=conn)

from QueueServices import qservices

# -----------------------------------------------------------------------------------------------------------------------
class CreateJobByURL(Resource):
    def post(self):
        args = parser.parse_args()
        print repr(args)
        print 'URL = ' + args['url']
        job = req_queue.enqueue_call(
            func=qservices.fetch_content, args=(args['url'], con_queue), result_ttl=10
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
