import json
from pyflink.common import Types
from pyflink.datastream import (
    StreamExecutionEnvironment,
    TimeCharacteristic
)
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema


def process_stream():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    env.set_stream_time_characteristic(TimeCharacteristic.EventTime)

    # Kafka config
    kafka_props = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "pyflink-group",
        "auto.offset.reset": "earliest"
    }

    consumer = FlinkKafkaConsumer(
        topics='input-topic',
        deserialization_schema=SimpleStringSchema(),
        properties=kafka_props
    )

    stream = env.add_source(consumer)

    # Process events
    processed = (
        stream.map(lambda x: json.loads(x), output_type=Types.MAP(Types.STRING(), Types.STRING()))
              .map(lambda x: f"user={x['user']}, value={x['value']}")
    )

    processed.print()

    env.execute("PyFlink Kafka Pipeline")


if __name__ == "__main__":
    process_stream()
