# Streaming Data Project with GCP and Python

Streaming Smartphone Data (Sensor Logger App) through Kafka with Python, Google Compute Engine, Cloud Storage and BigQuery

GitHub repos that helped me accomplish this project:
* [Awesome Sensor Logger](https://github.com/tszheichoi/awesome-sensor-logger#the-sensor-logger-app) - Sensor Logger App repo
* [Stock Market Kafka Real Time Data Engineering Project](https://github.com/darshilparmar/stock-market-kafka-data-engineering-project)
  
![alt-text](https://github.com/dfedeoli/kafka-gce-smartphone-data/blob/main/kafka-gcp.drawio.png?raw=true)

The idea was to get streaming Accelerometer data from my phone, send it to a Kafka Broker through a Producer .py file, get it from a Consumer .py app that sends it to Google Cloud Storage. Finally, create a BigQuery table that queries into the specific GCS bucket.

Important variables in this project:
<pre><code>your_host_ip -> Your machine's IP  
gce_external_ip -> Google Cloud Engine's external IP
</code></pre>

## Sensor Logger App - Available for iOS and Android
Pushes smartphone data (Accelerometer, gravity, gyroscope, etc) to your host IP through (default) Push URL: http://{your_host_ip}:8000/data  
See [App repo](https://github.com/tszheichoi/awesome-sensor-logger#the-sensor-logger-app) above!

## Producer Python file
Flask app that sends obtained data from app to Kafka broker in GCE and also plots a graph at http://localhost:8000 (thanks to [Kelvin Choi](https://github.com/tszheichoi))

## Google Compute Engine
Kafka broker installation and configuration, according to gce-linux-commands.txt. Remember to open tcp:9092 port for ingress and egress traffic, in order to connect to it from your machine.

## Consumer Python file
Gets data from Kafka topic, puts them into files and sends to Google Cloud Storage.

## Google Cloud Storage
Receives .json files constructed in consumer.py to GCS bucket.

## BigQuery
Create table from the bucket's .json files with the following path: smartphone_data_*.json
