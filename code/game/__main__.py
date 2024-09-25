# game.__main__.py
from importlib import resources

print("Game starting")

file = resources.files("game") / "sounds.txt"
print(file.read_text())
