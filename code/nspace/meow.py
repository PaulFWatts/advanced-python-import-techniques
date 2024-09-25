# meow.py
import sys
from pathlib import Path

project1 = Path(__file__).parent / "project1"
project2 = Path(__file__).parent / "project2"
sys.path += [str(project1), str(project2)]

from cats import tiger
from cats import lion
