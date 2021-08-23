# Elasticsearch and Kibana on Centos 7
Deploying ES instance and Kibana instance for testing is relatively straightforward using docker-compose.
Elastic provides and example file here which we have slightly modified [https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html]

This example `docker-compose.yml` has been reduced for deploying only a single node and kibana instance.

```
version: '2.2'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    container_name: es01
    environment:
      - node.name=es01
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - discovery.type=single-node
      - network.host=0.0.0.0
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic

  kib01:
    image: docker.elastic.co/kibana/kibana:7.14.0
    container_name: kib01
    ports:
      - 5601:5601
    environment:
      ELASTICSEARCH_URL: http://es01:9200
      ELASTICSEARCH_HOSTS: '["http://es01:9200"]'
    networks:
      - elastic

volumes:
  data01:
    driver: local

networks:
  elastic:
    driver: bridge
```

In this example ES will bind to all available IP address on the host which it is deployed.

We will deploy this on a Centos 7 server.
Once the server is deployed install docker and docker-compose following 

* [https://docs.docker.com/engine/install/centos/]
* [https://docs.docker.com/compose/install/]

You will also need to increase the swap memory limit on centos by modifying the `/etc/sysctl.conf` file and adding

```
vm.max_map_count=262144
```

Once these files have been modified you can run `docker-compose up -d` to spin up the ES and Kibana containers.

If you run into any issues you can check the logs using 

`docker logs [containerID]`

where the `containerID` can be found from `docker ps -a`.

You should then be able to curl to the ES instance and access the kibana server.

```
curl -X GET "http://<es-ip>:9200/_cat/nodes?v&pretty"
```

or navigate your web browerser to `http://<kibana-ip>:5601`
