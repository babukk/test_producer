
curl http://127.0.0.1:5000/create_job -X POST -d 'url=http://i02.c.aliimg.com/img/ibank/2015/762/803/2116308267_1378471200.jpeg'

curl -H "Content-Type: application/json" http://127.0.0.1:5000/create_job -X POST -d '{"url":"http://i02.c.aliimg.com/img/ibank/2015/762/803/2116308267_1378471200.jpeg"}'
