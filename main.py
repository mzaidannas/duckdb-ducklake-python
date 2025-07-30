import duckdb
import pandas as pd
import polars as pl
from duckdb.experimental.spark.sql import SparkSession as session
from duckdb.experimental.spark.sql.functions import lit, col

def main():
    spark = session.builder.getOrCreate()

    with duckdb.connect("ducklake:my_ducklake.db") as con:
        con.sql("CREATE TABLE IF NOT EXISTS my_table (id INTEGER, name VARCHAR, age INTEGER)")
        con.sql("DELETE FROM my_table")
        con.sql("INSERT INTO my_table VALUES (1, 'John', 25)")
        con.sql("INSERT INTO my_table VALUES (2, 'Charlie', 32)")
        con.table("my_table").show()
        pandas_dataframe = con.sql("SELECT * FROM my_table").df()
        polars_dataframe = con.sql("SELECT * FROM my_table").pl()
        pyspark_dataframe = spark.createDataFrame(pandas_dataframe)

        print(pandas_dataframe)
        print(polars_dataframe)
        print(pyspark_dataframe)

if __name__ == "__main__":
    main()
