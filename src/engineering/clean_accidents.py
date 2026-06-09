from pyspark.sql.functions import col, to_timestamp


def clean_accidents(df):
    """
    Nettoyage des données accidents.
    """

    df_clean = df \
        .withColumn("Severity", col("Severity").cast("integer")) \
        .withColumn("Start_Time", to_timestamp(col("Start_Time"))) \
        .withColumn("End_Time", to_timestamp(col("End_Time"))) \
        .withColumn("Start_Lat", col("Start_Lat").cast("double")) \
        .withColumn("Start_Lng", col("Start_Lng").cast("double"))

    # Vérification / suppression des doublons
    df_clean = df_clean.dropDuplicates(["ID"])

    # Suppression des nulls critiques
    df_clean = df_clean.dropna(
        subset=["Severity", "Start_Time", "State"]
    )

    return df_clean