# Distributed Video Streaming with Python & Kafka
## Start Kafka & Zookeeper

$ sudo systemctl start confluent-zookeeper
$ sudo systemctl start confluent-kafka
$ kafka-topics --list --zookeeper localhost:2181
$ kafka-topics --delete --zookeeper localhost:2181 --topic testing
$ kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testing

## Producer & Consumer

(yungshun-py3) $ pip3 install kafka-python opencv-contrib-python Flask

### Consumer

(yungshun-py3) /workspace/py3/kafka-distributed-video-streaming$ python3 consumer/consumer.py 
 * Serving Flask app "consumer" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 106-857-465
127.0.0.1 - - [15/May/2019 17:16:39] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/May/2019 17:16:40] "GET /video_feed HTTP/1.1" 200 -

### Producer

(yungshun-py3) /workspace/py3/kafka-distributed-video-streaming$ python3 producer/producer.py videos/Countdown1.mp4 
Publishing video...
Bad read!
Publish complete!

### Browse 0.0.0.0:5000
