# Data Factory — Deep Stack Solutions — M2 IMSD 2025-2026
## Prédiction de la gravité des accidents routiers (US Accidents)

## Équipe
| Rôle | Membre |
|------|--------|
| Architecte Data | Manar Belmokaddem |
| Data Engineer | - |
| Data Engineer | - |
| Data Scientist | - |
| Data Analyst | - |

## Onboarding — se connecter en 5 étapes
1. Aller sur https://datalab.sspcloud.fr et se connecter
2. Catalogue → lancer Jupyter-pyspark (CPU 4, RAM 8 Go)
3. git clone https://github.com/manar1305/data-factory-deep-stack.git
4. Récupérer les credentials S3 auprès de Manar (Architecte Data)
5. Ouvrir notebooks/00_test_connexion.ipynb et exécuter toutes les cellules

## Structure S3 (bucket manar1305)
- bronze/accidents/   → CSV brut Kaggle — lecture seule
- silver/accidents/   → Parquet nettoyé — Data Engineers écrivent ici
- gold/ml_features/   → Features ML — Data Scientist écrit ici
- gold/kpi/           → Agrégats dashboard — Data Analyst écrit ici

## Stack technique
- Onyxia SSP Cloud (INSEE) · Jupyter-pyspark 3.1.5
- Apache Spark 3.x / PySpark · MinIO S3 · Hive Metastore
- Python 3.10+
