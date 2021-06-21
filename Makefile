build:
	sudo docker build --rm=true -t cribl-filemanager .

up:
	sudo docker container run -d -v /etc/hosts:/tmp/hosts --name cribl-filemanager-p 5000:5000 cribl-filemanager

start:
	sudo docker start cribl-filemanager

stop:
	sudo docker stop cribl-filemanager

remove:
	sudo docker container rm -f cribl-filemanager

login:
	sudo docker exec -it cribl-filemanager /bin/bash