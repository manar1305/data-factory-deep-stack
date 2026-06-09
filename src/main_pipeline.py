import os
from pyspark.sql import SparkSession

from ingestion.read_bronze import read_bronze
from engineering.clean_accidents import clean_accidents
from engineering.write_silver import write_silver


def create_spark_session():

    spark = SparkSession.builder \
        .appName("data-factory-team2") \
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "https://minio.lab.sspcloud.fr"
        ) \
        .config(
            "spark.hadoop.fs.s3a.access.key",
            os.environ["AWS_ACCESS_KEY_ID"]
        ) \
        .config(
            "spark.hadoop.fs.s3a.secret.key",
            os.environ["AWS_SECRET_ACCESS_KEY"]
        ) \
        .config(
            "spark.hadoop.fs.s3a.session.token",
            os.environ["AWS_SESSION_TOKEN"]
        ) \
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider"
        ) \
        .config(
            "spark.hadoop.fs.s3a.path.style.access",
            "true"
        ) \
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        ) \
        .getOrCreate()

    return spark


def main():

    spark = create_spark_session()

    print(f"Spark {spark.version} démarré")

    # Lecture Bronze
    df = read_bronze(spark)

    print(f"Lignes Bronze : {df.count()}")
    print(f"Colonnes Bronze : {len(df.columns)}")

    # Nettoyage
    df_clean = clean_accidents(df)

    print(f"Lignes après nettoyage : {df_clean.count()}")

    # Écriture Silver
    write_silver(df_clean)

    print("✓ Pipeline terminé avec succès")


if __name__ == "__main__":
    main()