# Plateforme Data

## Contexte
Plateforme d'ingestion et d'analyse des données transactionnelles.
Elle centralise les flux issus des systèmes opérationnels, les historise dans un entrepôt, et alimente les tableaux de bord métier.

## Architecture

```
  Sources → Ingestion → Stockage → Transformation → Restitution
   (API,     (Kafka)     (MinIO)      (Spark/dbt)     (Power BI)
    CSV)
```

## Prérequis
| Outil | Version minimale |
|---|---|
| Docker | 24.0 |
| Terraform | 1.6 |
| Python | 3.10 |

## Démarrage rapide
> TODO


## Structure du dépôt
> TODO

## Contribuer
Voir [CONTRIBUTING.md](CONTRIBUTING.md)
