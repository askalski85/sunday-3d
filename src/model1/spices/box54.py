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

class MediumBox(API):
    name: str = "mediumbox"
    width: mm = 167  # Szerokosc pudelka
    depth: mm = 54  # Glebokosc pudelka
    height: mm = 85  # wysokosc pudelka

    thickness: mm = 1.2
    separator_thickness: mm = 1
    separator_height_buffer: mm = 20

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

        # separator
        separator = self.box(self.thickness, self.depth, self.separator_height, 0, 0, -self.separator_height_buffer/2)
        self.paint_red(separator)
        self.add(separator)

        # self.paint_green(separator)
        # self.addform(separator, self.width/4 + self.thickness/2, 0, 0)
        
        # self.paint_blue(separator)
        # self.addform(separator, -self.width/2 - self.thickness, 0, 0)
