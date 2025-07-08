import math
import trimesh
from trimesh.visual import ColorVisuals

from .units import *

class API:
    scene: trimesh.Scene = None
    name: str = None
    extension: str = 'stl'

    red = [255, 0, 0, 255]
    green = [0, 255, 0, 255]
    blue = [0, 0, 255, 255]

    def __init__(self, name: str = 'model'):
        print(f'New {name} model')
        self.name = name
        self.scene = trimesh.Scene()

    def build(self) -> None:
        self.bottom()
        self.left()
        self.right()
        self.back()
        self.front()

    def add_box(self,*args, **kwargs) -> None:
        self.scene.add_geometry(self.box(*args, **kwargs))

    def box(self, width: mm, depth: mm, height: mm, twidth: mm, tdepth: mm, theight: mm) -> trimesh.Trimesh:
        return trimesh.creation.box(extents=[width, depth, height], transform = trimesh.transformations.translation_matrix([twidth, tdepth, theight]))

    def triangle(self, a: mm, b: mm, height: mm) -> trimesh.Trimesh:
        v0 = [0, 0, 0]
        v1 = [a, 0, 0]
        v2 = [0, b, 0]

        v3 = [0, 0, height]
        v4 = [a, 0, height]
        v5 = [0, b, height]

        # Tworzenie siatki
        vertices = [v0, v1, v2, v3, v4, v5]
        faces = [
            [2, 1, 0], [3, 4, 5],         # podstawy
            [0, 1, 4], [0, 4, 3],         # bok 1
            [1, 2, 5], [1, 5, 4],         # bok 2
            [2, 0, 3], [2, 3, 5]          # bok 3
        ]
        return trimesh.Trimesh(vertices=vertices, faces=faces)

    def transform(self, g: trimesh.Trimesh, x: mm, z: mm, y: mm) -> None:
        g.apply_transform(trimesh.transformations.translation_matrix([x, z, y]))

    def addform(self, g: trimesh.Trimesh, x: mm, z: mm, y: mm) -> None:
        self.transform(g, x, z, y)
        self.scene.add_geometry(g)

    def add(self, g: trimesh.Trimesh) -> None:
        self.scene.add_geometry(g)

    def get(self) -> trimesh.Scene:
        return self.scene
    
    def export(self, name = None) -> None:
        self.scene.export(f'build/{name or self.name}.{self.extension}')
    
    def paint_red(self, g: trimesh.Trimesh) -> None:
        g.visual = ColorVisuals(mesh=g, face_colors=self.red)

    def paint_blue(self, g: trimesh.Trimesh) -> None:
        g.visual = ColorVisuals(mesh=g, face_colors=self.blue)

    def paint_green(self, g: trimesh.Trimesh) -> None:
        g.visual = ColorVisuals(mesh=g, face_colors=self.green)

    def rotate_x(self, g: trimesh.Trimesh, degrees: grade):
        angle = math.radians(degrees)
        matrix = trimesh.transformations.rotation_matrix(angle, [1, 0, 0])
        return g.apply_transform(matrix)

    def rotate_y(self, g: trimesh.Trimesh, degrees: grade):
        angle = math.radians(degrees)
        matrix = trimesh.transformations.rotation_matrix(angle, [0, 1, 0])
        return g.apply_transform(matrix)

    def rotate_z(self, g: trimesh.Trimesh, degrees: grade):
        angle = math.radians(degrees)
        matrix = trimesh.transformations.rotation_matrix(angle, [0, 0, 1])
        return g.apply_transform(matrix)