# ELK stack Proof of Concept

This project is a proof of concept that uses Filebeat, Logstash, Elasticsearch and Kibana for summarizing and centralizing logs from two microservices developed with SpringBoot (Java) and FastAPI (Python) respectively. In fact, it's aimed to send logs to Logstash and visualize them in Kibana by creating the corresponding indexes in Elasticsearch.

## Technologies

This PoC have been made with:
* Windows 7 Professional SP 1
* Docker Toolbox for Windows 7
* Docker 18.03.0
* Java 11

Due to Windows 7 runs docker into a VirtualBox virtual machine, there are two changes that must be made in the VM for being able to run Elasticsearch:
- the VM needs unless 4Gb of RAM
- within the VM it's necessary to run the following command: ``` sysctl -w vm.max_map_count=262144 ```

## Architecture

The project run 6 containers, all of them from the *docker-compose.yml*. Four of them belonging to the ELK stack and the other two are the simplest  microservices ever developed:

- Kibana
- Elasticsearch: a cluster with only one node
- Logstash
  - /logstash contains the logstash.conf and the Dockerfile used for build the logstash image.
- Filebeat
  - /filebeat contains the filebeat.yml and the Dockerfile used for build the filebeat image.
- Micrologs
  - /logs contains the SpringBoot project. It exposes just the following GET endpoint: */*, which returns the message ``` Hello! ```. It creates an info log, which is sent to Logstash.
- Fastapi
  - /fastapi contains the FastAPI project.  It exposes just the following GET endpoint: */api/greetings/*, which returns a json. It saves logs in a file which is used by Filebeat afterwards.
  ```
  {
   "greetings": "Hi folks!"
  }
  ```

Some extra details

1. Kibana, Elasticsearch, Logstash and Filebeat belong to the ELK stack.

2. Filebeat uses a mounted volume for read log files and send them to Logstash.  

  FastAPI is a microservice developed with FastAPI (Python 3.7). It use a mounted volume for save log files.

  **Both Filebeat and FastAPI, mount the same host path. This is the representation of Sidecar Pattern, being Filebeat the Sidecar of FastAPI microservice. Thus, all log files produced by the FastAPI microservice are read and sent by Filebeat to Logstash.**

3. Micrologs is a microservice developed with SpringBoot (Java 11). It send logs to Logstash using an appender defined in logback-spring.xml.

## Run the project

For running the whole project use the following command: ``` docker-compose up --build -d ```
