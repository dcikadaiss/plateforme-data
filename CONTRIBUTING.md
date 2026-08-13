# Guide de contribution

## Workflow
[Lequel tu retiens, en une phrase. Renvoie vers l'ADR pour la justification.]

## Convention de branches
| Prefixe | Usage | Exemple |
|---|---|---|
| feat/ | nouvelle fonctionnalite | feat/DATA-12-ingestion-kafka |
| fix/ | correction de bug | fix/DATA-45-timeout-minio |
| docs/ | documentation | docs/DATA-08-guide-demarrage |
| chore/ | maintenance | chore/DATA-33-maj-dependances |

## Convention de commits
Conventional Commits : `<type>(<portee>): <description>`

Exemples :
- `feat(ingestion): ajout du support des fichiers Parquet`
- `fix(docker): correction du healthcheck PostgreSQL`
- `docs(readme): mise a jour du guide de demarrage`

## Pull Requests
- Maximum 400 lignes modifiees
- Un seul sujet par PR
- CI verte obligatoire
- [tes autres regles]

## Avant de committer
```bash
make lint
make test
```
