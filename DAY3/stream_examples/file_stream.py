from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

# create spark session
spark = SparkSession.builder.appName("filestream").getOrCreate()

# define schema
schema = StructType([StructField('name',StringType(),True),
            StructField('age',IntegerType(),True),
            StructField('city',StringType(),True)])

# read stream from a folder/directory
file_stream = spark.readStream.option("header","true").schema(schema).csv("input_data/")

# process - filter
result = file_stream.filter(file_stream.age >= 30)

# write streaming output to console
query = result.writeStream.format("console").start()

query.awaitTermination()
