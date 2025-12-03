from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col
import sqlite3

# ---------------------------------------------
# Function to write batch data to sqlite
# ---------------------------------------------
def write_to_sqlite(df, epoch_id):
    # Convert df to pandas for easy insert
    pdf = df.toPandas()

    # Connect to sqlite
    conn = sqlite3.connect("stream_output.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS word_count (
            word TEXT,
            count INTEGER
        )
    """)

    # Insert rows
    for _, row in pdf.iterrows():
        cursor.execute(
            "INSERT INTO word_count (word, count) VALUES (?, ?)",
            (row["word"], int(row["count"]))
        )

    conn.commit()
    conn.close()


# ---------------------------------------------
# Main streaming code
# ---------------------------------------------
if __name__ == "__main__":

    spark = SparkSession.builder.appName("socket_to_sqlite").getOrCreate()

    # 1. Read socket stream
    data = spark.readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    # 2. Convert text to word counts
    words = data
