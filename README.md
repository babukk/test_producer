## Test prodicer

### Features
Gets URL as a POST-parameter (via JSON or form input), extracts HTML-content and palces it into Redis database.

### How to

1. First install everything in a virtualenv:

```bash
virtualenv venv
. ./venv/bin/activate
pip install -I -r requirements.txt
```
2. Run th worker (in separate terminal winwod):
```
cd test-producer
. ./venv/bin/activate
python req-worker.py
```

3. Run the application:

```
cd test-producer
. ./venv/bin/activate
python app.py
```

4. Try to send the POST-requests. For example (via curl command in shell):
```curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=1"}'
```
