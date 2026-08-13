"""Tests du module de validation de schema."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from validation import valider_schema  # noqa: E402


def test_schema_complet(tmp_path):
    f = tmp_path / "ok.csv"
    f.write_text("id,date,montant,client\n1,2026-01-01,100,ACME\n")
    valide, manquantes = valider_schema(f)
    assert valide is True
    assert manquantes == []


def test_schema_incomplet(tmp_path):
    f = tmp_path / "ko.csv"
    f.write_text("id,montant\n1,100\n")
    valide, manquantes = valider_schema(f)
    assert valide is False
    assert manquantes == ["client", "date"]
