from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName("deltalake-demo").master("local[*]").config("spark.sql.extensions","io.delta.sql.DeltaSparkSessionExtension").config("spark.sql.catalog.spark_catalog","org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

lake_path = "file:///home/student/users"

# lake_path = "s3a://your-bucket-name/delta-lake/user"

# create a dataframe and write as delta-table

data = [(101,"raj"),(102,"leo"),(103,"tom")]

df = spark.createDataFrame(data,["id","name"])
df.write.format("delta").mode("overwrite").save(lake_path)

# Read data from delta table

df_read = spark.read.format("delta").load(lake_path)
df_read.show()
