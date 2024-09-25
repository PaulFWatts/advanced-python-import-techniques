# getgift.py
import sys
from pathlib import Path

folder = Path(__file__).parent / "src"
sys.path.insert(0, str(folder))

from package.gift import WRAPPING
print("Wrapping color is", WRAPPING)
