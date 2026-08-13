# Changelog

Toutes les modifications notables de ce projet sont documentées ici.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/)
et le versionnage respecte [SemVer](https://semver.org/lang/fr/).

## [0.2.0] - 2026-08-12

### Ajouté
- Contrôle du schéma des fichiers CSV avant ingestion, avec restitution des
  colonnes manquantes.
- Tests unitaires du module de validation.

## [0.1.0] - 2026-08-12

### Ajouté
- Structure du dépôt et fichiers de gouvernance (`.gitignore`,
  `.gitattributes`, `CODEOWNERS`).
- Stack de développement Docker : MinIO et PostgreSQL.
- Makefile pour les commandes courantes.
- Script d'ingestion CSV vers le stockage objet.
- Tests unitaires du module d'ingestion.
- Configuration `pre-commit` avec détection de secrets.
- Documentation : README, guide de contribution, ADR-0001.
