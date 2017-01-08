import json
# import nose
# from nose.tools import *

from tests import test_app

def check_content_type(headers):
  eq_(headers['Content-Type'], 'application/json')

rv = test_app.post('/create_job', data='{"url": "http://www.boohoo.com/"}')
check_content_type(rv.headers)
eq_(rv.status_code, 200)


