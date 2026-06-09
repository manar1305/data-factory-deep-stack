from pyspark.sql import DataFrame


def write_silver(df_clean: DataFrame) -> None:
    """
    Écriture des données nettoyées dans la couche Silver au format Parquet.
    """

    df_clean.write \
        .mode("overwrite") \
        .parquet(
            "s3a://manar1305/data-factory-silver/accidents/"
        )