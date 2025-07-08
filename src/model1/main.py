import os
import typer

from .model_libs.api import API
from .spices.medium import MediumBox
from .tee.tee import Tee 
from .teebags.teebags import Teebags

app = typer.Typer()

def build(model: API) -> None:
    model.build()
    model.export()
    model.get().show()

@app.command()
def teebags(name: str = 'teebaags') -> None:
    build(Teebags(name))

@app.command()
def tee(name: str = 'tee') -> None:
    build(Tee(name))

@app.command()
def spices(name: str = 'spices') -> None:
    print(f"[{name}] Creating Spices container.")

def main() -> int:
    os.makedirs("build", exist_ok=True)
    app()
    return 0

    # Parametry pierścienia
    # outer_radius = 10
    # inner_radius = 8
    # height = 5
    scene = trimesh.Scene()
    # Tworzymy pierścień jako różnicę dwóch cylindrów
    cylinder = trimesh.creation.cylinder(radius=5, height=54, sections=742)
    box = trimesh.creation.box(extents=[10, 10, 10])
    result = cylinder.difference(box)
    scene.add_geometry(result)
    scene.show()

    scene.export('build/tee.stl')

    # inner = trimesh.creation.cylinder(radius=inner_radius, height=height + 1, sections=64)
    # inner.apply_translation([0, 0, -0.5])  # Przesuwamy lekko, by uniknąć "coplanar faces"
    # ring = outer.difference(inner)

    # # Tworzymy rowek (np. wzdłuż wewnętrznej ściany)
    # groove_radius = inner_radius + 0.3  # tuż przy wewnętrznej ściance
    # groove_depth = 1.5
    # groove_height = 1.0
    # groove = trimesh.creation.cylinder(radius=groove_radius, height=groove_height, sections=64)
    # groove.apply_translation([0, 0, height / 2 - groove_height / 2])  # umieszczamy w górnej połowie

    # # Odejmuje rowek
    # ring_with_groove = ring.difference(groove)

    # Podgląd
    # ring_with_groove.show()