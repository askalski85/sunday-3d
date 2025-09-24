from ..model_libs.api import API
from ..model_libs.units import *

# 0.20mm Strength

# Struktura
## wypelnienie 7%
## gyroidalny
## dolne wartwy powloki 2
## przenikanie malowania dolnych warstw 2

# Jakosc
## wysokosc pierwszej warstwy 0,1

# Podpora
## brak

# nozyczki
class MediumBox(API):
    name: str = "mediumbox"
    width: mm = 310  # Szerokosc pudelka
    depth: mm = 32.4  # Glebokosc pudelka
    height: mm = 30  # wysokosc pudelka

    thickness: mm = 1.2
    separator_thickness: mm = 1
    separator_height_buffer: mm = 10
    wall_height: mm = 60


    @property
    def separator_height(self):
        return self.height - self.separator_height_buffer

    def build(self) -> None:
        box = self.box(self.width, self.depth, self.height, 0, 0, 0)
        # self.paint_blue(box)
        box_cut = self.box(self.width - 2*self.thickness, self.depth - 2*self.thickness, self.height, 0, 0, 1)
        box = box.difference(box_cut)
        # self.paint_green(box_cut)
        # self.add(box_cut)
        
        self.add(box)
        wall = self.box(self.width, self.thickness, self.wall_height, 0, self.depth/2 - self.thickness/2, self.height/2)
        self.add(wall)
        

        # separator
        for sep in range(10):
            position = self.thickness/2 - self.width/2 + sep * 31
            separator = self.box(self.separator_thickness, self.depth, self.height, position, 0, 0)
            self.paint_red(separator)
            self.add(separator)

        # self.paint_green(separator)
        # self.addform(separator, 0, 0, 0)
