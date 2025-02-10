docker run -d -p 3000:8080 test_service
docker build -t testserviceb .
docker tag testserviceb 6regmcc/testserviceb:8


docker tag test_service 6regmcc/test-service
docker push 6regmcc/test-service 

docker build -t testserviceb .
