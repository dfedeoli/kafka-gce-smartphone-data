from google.cloud import storage
from kafka import KafkaConsumer
import json

client = storage.Client()
bucket = client.get_bucket("smartphone-sensor-data")
print(bucket)

# modify {gce_external_ip} for GCE's external ip
consumer = KafkaConsumer('sensorlogger', bootstrap_servers=['{gce_external_ip}:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for count, i in enumerate(consumer):
    print(count)
    print(i.value)
    file_name = "data/smartphone_data_{}.json".format(count)
    with open(file_name, 'w') as file:
        file.write(json.dumps(i.value))

    blob = bucket.blob(file_name)
    if blob.upload_from_filename(file_name):
        print("File successfully uploaded to bucket.")
    else:
        print("Error uploading file to bucket.")