
import time
import requests

# -----------------------------------------------------------------------------------------------------------------------
def fetch_content(url):
    print 'fetch_content: -----> url = ' + url

    sess = requests.Session()

    try:
        html = sess.get(url, timeout=10)
    except requests.RequestException as err:
        print 'fetch_content: Network error. err = ' + str(err)
    else:
        print 'fetch_content:' + repr(html.text)

    time.sleep(3)
    print 'fetch_content: -- finished ---> url = ' + url
    pass
