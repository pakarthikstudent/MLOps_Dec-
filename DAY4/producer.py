from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
  bootstrap_server = ["localhost:9092"],
  value_serializer = lambda v:json.dumps(v).encode('utf-8'),
)

users = ["karthik","bibu","leo","raj"]

for var in range(20):
        event = { "user": random.choice(users),"value": random.randint(1,100),}
        producer.send("input-topic",value=event)
        time.sleep(0.5)

producer.flush()
print("----- End of the Appln ------")
