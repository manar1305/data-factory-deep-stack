from pyspark.sql import DataFrame


def read_bronze(spark) -> DataFrame:
    """
    Lecture des données brutes depuis la couche Bronze.
    """

    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(
            "s3a://manar1305/data-factory-bronze/accidents/US_Accidents_March23.csv"
        )

    return df