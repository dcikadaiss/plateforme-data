"""Validation du schema des fichiers ingeres."""

import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

COLONNES_ATTENDUES = {"id", "date", "montant", "client"}


def lire_entete(chemin: Path) -> set[str]:
    """Retourne l'ensemble des colonnes du fichier CSV."""
    with chemin.open(newline="", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        return set(next(lecteur, []))


def valider_schema(chemin: Path) -> tuple[bool, list[str]]:
    """Verifie que toutes les colonnes attendues sont presentes."""
    colonnes = lire_entete(chemin)
    manquantes = sorted(COLONNES_ATTENDUES - colonnes)
    if manquantes:
        logger.error("Colonnes manquantes : %s", ", ".join(manquantes))
        return False, manquantes
    return True, []
