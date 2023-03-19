import toml
import os, shutil
from .temp import set_environment
from datetime import datetime

# Setting up dir --------------------------------------------------------------------------------- #
pkg_dir = os.path.dirname(__file__)
templates_dir = os.path.join(pkg_dir, "templates")
demo_dir = os.path.join(templates_dir, "demo")

# Setting up meta data --------------------------------------------------------------------------- #
cur_year = datetime.now().year
structure = toml.load(os.path.join(templates_dir, "structure.toml"))
meta_data = {
    "year": cur_year
}

# Create demo file ------------------------------------------------------------------------------- #
def create_demo():
    os.makedirs("demo", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    shutil.copyfile(src=os.path.join(demo_dir, "demo.py"), dst="demo/demo.py")
    shutil.copyfile(src=os.path.join(demo_dir, "md_demo.md"), dst="docs/md_demo.md")
    shutil.copyfile(src=os.path.join(demo_dir, "py_demo.md"), dst="docs/py_demo.md")