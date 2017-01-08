## Test producer

### Features
Gets URL as a POST-parameter (via JSON or form input), extracts HTML-content and places it into Redis database.

### How to

First install everything in a virtualenv:

```bash
virtualenv venv
. ./venv/bin/activate
pip install -I -r requirements.txt
```
Run the rq-worker (in separate terminal winwod):
```bash
cd test-producer
. ./venv/bin/activate
python req-worker.py
```

Run the application:

```bash
cd test-producer
. ./venv/bin/activate
python app.py
```

Try to send the POST-requests. For example (via curl command in shell):
```bash
curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=1"}'
```
