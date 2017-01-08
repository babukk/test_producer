
import time
import requests
import redis
import json

# -----------------------------------------------------------------------------------------------------------------------
def fetch_content(url, cont_redis_url):
    cont_redis = redis.from_url(cont_redis_url)

    sess = requests.Session()

    try:
        html = sess.get(url, timeout=10)
    except requests.RequestException as err:
        print 'fetch_content: Network error. err = ' + str(err)
    else:
        # print 'fetch_content:' + repr(html.text)
        # data = {'url': url, 'content': html.text}
        # cont_redis.lpush('content', json.dumps(data))

        cont_redis.lpush('content', html.text)
