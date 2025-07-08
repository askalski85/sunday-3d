import trimesh

from ..model_libs.units import *
from ..model_libs.api import API

class Tee(API):
    name: str = 'tee'
    label_height: mm = 80  # wysokosc etykiety
    label_thickness: mm = 6
    label_hole: mm = 3.6
    label_preview: mm = 12
    height: mm = 120  # wysokosc y
    width: mm = 70  # szerokosc x
    depth: mm = 80  # glebokosc z
    thickness: mm = 1.2  # grubosc scian

    def label(self):
        main_label = self.box(self.width, self.label_thickness, self.label_height, 0, -self.depth/2 + self.label_thickness/2, self.height - self.label_height/2)
        # self.paint_red(main_label)
        # self.add(main_label)

        # zrobic okno na tytke od herbaty
        label_preview = self.box(self.width - 2 * self.label_preview, self.label_thickness - self.thickness, self.label_height - 2 * self.label_preview, 0, -self.depth/2 + self.label_thickness/2 - self.thickness, self.height - self.label_height/2)
        # self.paint_blue(label_preview)
        # self.add(label_preview)
        main_label = main_label.difference(label_preview)

        # zrobic rowek na tytke od herbaty
        label_preview2 = self.box(self.width - 2 * self.thickness, self.label_hole, self.label_height - self.thickness, 0, -self.depth/2 + self.label_thickness/2, self.height - self.label_height/2 + self.thickness/2)
        # self.paint_green(label_preview2)
        # self.add(label_preview2)
        main_label = main_label.difference(label_preview2)
        self.paint_red(main_label)
        self.add(main_label)

    def build(self):
        self.add_box(self.width, self.depth , self.thickness, 0, 0, self.thickness/2)  ## bottom
        self.add_box(self.thickness, self.depth, self.height, self.width/2 - self.thickness/2, 0, self.height/2)   # right wall
        self.add_box(self.thickness, self.depth, self.height, -self.width/2 + self.thickness/2, 0, self.height/2)  # left wall
        self.add_box(self.width, self.thickness, self.height, 0, self.depth/2 - self.thickness/2, self.height/2)   # back wall
        # self.add_box(self.width, self.thickness, self.height, 0, -self.depth/2 + self.thickness/2, self.height/2)  # front label

        self.label()
