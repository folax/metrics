# Metrics
Metrics is a python based scrypt, using to get system information about central processor unit and memory utilization. 
Script using psutil(Cross-platform lib for process and system monitoring in Python.) to obtain system information.  

--------------------------------------------------------
   Usage: metrics [ cpu | mem ]
   No args         Display help.
   cpu             Display CPU metrics information.
   mem             Display MEMORY metrics information.
--------------------------------------------------------

# Using Docker
Instruction:
1) Create empty directory;
2) Copy our metrics.py script file to the directory.
3) Create Dockerfile
4) Edit Dockerfile:

 FROM:python3
 ADD metrics.py /
 RUN pip install psutil
 ENV _options ""
 CMD "python" ./metrics.py $_options

5) Build image:
	sudo docker -t metrics

6) Run image with keys:
	CPU information: 	sudo docker run -e _options="cpu" metrics
	MEMORY information: sudo docker run -e _options="mem" metrics

# Answers to questions. 
Question: How to display information about processes running on the host machine from within container environment (think about pid namespaces).
Question: How to display usernames for processes running on the host machine from within container environment (think how linux resolves uid to username and docker volumes). 
Answer: We need to get a shell on the host!

HowTo:

1) Create Dockerfile
	FROM centos:7
	RUN yum makecache
	RUN yum install -y httpd
	EXPOSE 80

	VOLUME /var/www/html

	ENTRYPOINT [ "/usr/sbin/httpd" ]
	CMD ["-D", "FOREGROUND"]

2) Build image.
	sudo docker build -t centos .

3) Run our image. 
--privileged : grants additional permissions to the container, it allows the container to gain access to the devices of the host (/dev)
--pid=host : allows the containers to use the processus tree of the Docker host (the VM in which the Docker daemon is running)

	sudo docker run -d -it --privileged --pid=host centos

4) Enter to our container, run bash
	
	sudo docker exec -it 8457fd3d2add /bin/bash

5) Starting nsenter and run commands on host machine

	nsenter -t 1 -m -u -n -i sh

-t, --target pid
	



