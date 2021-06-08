build:
	sudo docker build --rm=true -t cribl-filemanger .

up:
	sudo docker container run -d -v /etc/hosts:/tmp/hosts --name cribl-filemanger -p 5000:5000 cribl-filemanger

start:
	sudo docker start cribl-filemanger

stop:
	sudo docker stop cribl-filemanger

remove:
	sudo docker container rm -f cribl-filemanger

login:
	sudo docker exec -it cribl-filemanger /bin/bash