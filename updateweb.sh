#updateweb.sh
docker-compose build web
docker-compose stop web
docker-compose up -d