"""Tests unitaires du module d'ingestion."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ingestion import construire_cle, valider_source  # noqa: E402


def test_valider_source_fichier_absent(tmp_path):
    assert valider_source(tmp_path / "inexistant.csv") is False


def test_valider_source_fichier_vide(tmp_path):
    fichier = tmp_path / "vide.csv"
    fichier.touch()
    assert valider_source(fichier) is False


def test_valider_source_fichier_valide(tmp_path):
    fichier = tmp_path / "donnees.csv"
    fichier.write_text("id,nom\n1,Serge\n")
    assert valider_source(fichier) is True


def test_construire_cle_prefixe_par_defaut():
    assert construire_cle(Path("/tmp/ventes.csv")) == "raw/ventes.csv"


def test_construire_cle_prefixe_personnalise():
    assert construire_cle(Path("/tmp/ventes.csv"), "staging") == "staging/ventes.csv"
