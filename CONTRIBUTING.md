# Guide de contribution

## Workflow

Ce projet suit **GitHub Flow** : la branche `main` est maintenue déployable en
permanence, et toute modification passe par une branche de courte durée
intégrée par Pull Request.

La justification de ce choix figure dans
[ADR-0001](docs/adr/0001-choix-workflow.md).

`main` est protégée : les poussées directes sont refusées.

## Convention de branches

Format : `<type>/<TICKET>-<description-courte>`

| Préfixe | Usage | Exemple |
|---|---|---|
| `feat/` | nouvelle fonctionnalité | `feat/DATA-12-ingestion-kafka` |
| `fix/` | correction de bug | `fix/DATA-45-timeout-minio` |
| `docs/` | documentation | `docs/DATA-08-guide-demarrage` |
| `refactor/` | refonte sans changement de comportement | `refactor/DATA-21-client-s3` |
| `chore/` | maintenance, dépendances | `chore/DATA-33-maj-pytest` |

La description est en kebab-case, sans accent, cinq mots maximum.

## Convention de commits

Ce projet applique [Conventional Commits](https://www.conventionalcommits.org/fr/).
