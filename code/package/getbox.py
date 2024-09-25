# getbox.py
import sys
from pathlib import Path

folder = Path(__file__).parent / "src"
sys.path.insert(0, str(folder))

from package.box import CONTENTS
print("Box contents are ", CONTENTS)
