#! /bin/bash
#-----------------------------------------------------------------------------------------------------------

curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=1"}'

curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=2"}'

curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=3"}'

curl -H "Content-Type: application/json" \
    http://127.0.0.1:5000/create_job \
    -X POST -d '{"url":"http://www.boohoo.com/restofworld/accessories/beauty/icat/beauty#esp_pg=4"}'
