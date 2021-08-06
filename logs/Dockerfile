#pull base image
FROM adoptopenjdk/openjdk11

EXPOSE 8080

#copy jar to docker image
ADD ./target/*.jar /data/logs.jar

#default command
CMD java -jar -Dlogstash.server=${LOGSTASH} /data/logs.jar