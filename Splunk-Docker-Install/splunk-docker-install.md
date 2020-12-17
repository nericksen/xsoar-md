# Docker Splunk

```
sudo docker run -d -p 8000:8000 -p 8088:8088 -p 8089:8089 -p 9997:9997 --name splunk -e 'SPLUNK_START_ARGS=--accept-license' -e 'SPLUNK_PASSWORD=pocINSTANCEpassword1' splunk/splunk:latest
```