# reverse-proxy-demo
CS3219 Task A

How to run docker container

Step 1: To get docker images

Method 1: Via Docker Hub

Pull relevant images from Docker Hub repository

docker pull permasteo/microservice1
docker pull permasteo/microservice2
docker pull permasteo/mynginx

Method 2: Via Github

Pull code from repository.

git clone https://github.com/Permas-Teo/reverse-proxy-demo.git

Build images in each individual repo.

docker build -t permasteo/microservice1 .
docker build -t permasteo/microservice2 .
docker build -t permasteo/mynginx .

Step 2: Run docker containers

Run on separate terminal:

docker run -p 9090:5000 --name microservice1 permasteo/microservice1

At this point, image microservice1 can be accessed via http://localhost:9090/app1 

Run on separate terminal:

docker run -p 9091:5000 --name microservice2 permasteo/microservice2

At this point, image microservice2 can be accessed via http://localhost:9091/app2

Run on separate terminal:

docker run -d --name mynginx -p 80:80 -p 443:443 --link=microservice1 --link=microservice2 permasteo/mynginx

At this point, on top of existing links above, images microservice1 and microservice2 can be accessed via http://localhost:80/app1 and http://localhost:80/app2 respectively through the reverse-proxy.