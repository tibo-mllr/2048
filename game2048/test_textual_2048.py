from textual_2048 import *
from _pytest.monkeypatch import monkeypatch


def test_textual(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda cmd: 'd')

    assert read_player_command() == 'd'

# Ouvrir anaconda prompt, se déplacer dans le bon dossier, lancer pytest
