import os
import typer

from .model_libs.api import API
from .spices.mediumbox import MediumBox
from .pens.mediumbox import MediumBox as PensMediumBox
from .baterries.mediumbox import MediumBox as BaterriesMediumBox
from .samsung.cover import YEPPCover

from .tee.tee import Tee 
from .teebags.teebags import Teebags

app = typer.Typer()

def build(model: API) -> None:
    model.build()
    model.export()
    model.get().show()

@app.command()
def batteries(name: str = 'batteries') -> None:
    build(BaterriesMediumBox(name))

@app.command()
def samsung(name: str = 'cover') -> None:
    build(YEPPCover(name))

@app.command()
def teebags(name: str = 'teebaags') -> None:
    build(Teebags(name))

@app.command()
def tee(name: str = 'tee') -> None:
    build(Tee(name))

@app.command()
def spices(name: str = 'spices') -> None:
    print(f"[{name}] Creating Spices container.")
    build(MediumBox(name))

@app.command()
def pens(name: str = 'pens') -> None:
    print(f"[{name}] Creating Pens container.")
    build(PensMediumBox(name))

def main() -> int:
    os.makedirs("build", exist_ok=True)
    app()
    return 0
