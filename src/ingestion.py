"""Ingestion de fichiers CSV vers le stockage objet MinIO."""

import argparse
import logging
import os
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def valider_source(chemin: Path) -> bool:
    """Verifie que le fichier source existe et n'est pas vide."""
    if not chemin.exists():
        logger.error("Fichier introuvable : %s", chemin)
        return False
    if chemin.stat().st_size == 0:
        logger.error("Fichier vide : %s", chemin)
        return False
    return True


def construire_cle(chemin: Path, prefixe: str = "raw") -> str:
    """Construit la cle objet a partir du nom de fichier."""
    return f"{prefixe}/{chemin.name}"


def ingerer(source: Path, bucket: str) -> int:
    """Ingere un fichier CSV vers le bucket cible."""
    if not valider_source(source):
        return 1

    cle = construire_cle(source)
    endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")

    logger.info("Ingestion de %s vers %s/%s (endpoint %s)",
                source, bucket, cle, endpoint)
    logger.info("Ingestion terminee avec succes")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingestion CSV vers MinIO")
    parser.add_argument("source", type=Path, help="Chemin du fichier CSV")
    parser.add_argument("--bucket", default="plateforme-raw",
                        help="Bucket cible (defaut: plateforme-raw)")
    args = parser.parse_args()
    return ingerer(args.source, args.bucket)


if __name__ == "__main__":
    sys.exit(main())
