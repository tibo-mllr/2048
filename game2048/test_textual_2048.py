import os
import sys
sys.path.append(os.path.join(""))

from game2048.textual_2048 import read_player_command


def test_read_player_command(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda cmd: "g")  #a trouver sur stack overflow le builtins pour simuler un input
    assert read_player_command() == "g"


    