from textual_2048 import *

def test_player_command(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda cmd:"g")
    assert read_player_command()=="g"
def  test_read_size_grid(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda cmd:"4")
    assert read_size_grid()=="4"
def test_read_theme_grid(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda cmd:"4")
     assert read_theme_grid()=='default'
    

