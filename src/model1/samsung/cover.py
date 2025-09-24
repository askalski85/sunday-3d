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

class YEPPCover(API):
    name: str = "yeppcover"
    width: mm = 79  # Szerokosc pudelka
    depth: mm = 23  # Glebokosc pudelka
    height: mm = 5  # wysokosc pudelka

    thickness: mm = 2

    def build(self) -> None:
        box = self.box(self.width, self.depth, self.height, 0, 0, 0)
        self.paint_blue(box)
        box_cut = self.box(self.width - 2*self.thickness, self.depth - 2*self.thickness, self.height, 0, 0, 0)
        box = box.difference(box_cut)
        # self.paint_green(box_cut)
        # self.add(box_cut)
        
        self.add(box)

        # separator
        # separator = self.box(self.thickness, self.depth, self.height, 0, 0, 0)
        # self.paint_red(separator)
        # self.add(separator)

        # self.paint_green(separator)
        # self.addform(separator, 0, 0, 0)
