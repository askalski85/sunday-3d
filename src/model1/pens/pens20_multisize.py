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
    width: mm = 200  # Szerokosc pudelka
    depth: mm = 80  # Glebokosc pudelka
    height: mm = 100  # wysokosc pudelka
    lower_cut: mm = 40

    thickness: mm = 2
    separator_thickness: mm = 1
    separator_height_buffer: mm = 10
    separator_shift: mm = 10
    separator_innen_shift: mm = 10


    def build(self) -> None:
        box = self.box(self.width, self.depth, self.height, 0, 0, 0)
        # self.paint_blue(box)
        box_cut = self.box(self.width - 2*self.thickness, self.depth - 2*self.thickness, self.height, 0, 0, 1)
        box = box.difference(box_cut)
        # self.paint_green(box_cut)
        # self.add(box_cut)
        
        box_cut_top = self.box(self.width/2 - self.thickness/2 - self.separator_shift, self.depth, self.lower_cut, self.width/4 + self.separator_shift/2 + self.separator_thickness/2, 0, 30)
        # self.paint_red(box_cut_top)
        # self.add(box_cut_top)
        box = box.difference(box_cut_top)

        self.add(box)

        # separator
        separator = self.box(self.thickness, self.depth, self.height, 0, 0, 0)
        # self.paint_red(separator)
        # self.add(separator)

        self.paint_green(separator)
        self.addform(separator, self.separator_shift, 0, 0)

        # horizontal separator left part
        hseparator_left = self.box(self.width/2 + self.separator_shift + self.thickness/2, self.thickness, self.height - self.separator_innen_shift, -self.width/4 + self.separator_shift/2 + self.thickness/4, 0, -self.separator_innen_shift/2)
        # self.paint_red(hseparator_left)
        self.add(hseparator_left)

        # horizontal separator right part
        hseparator_left = self.box(
            self.width/2 - self.separator_shift + self.thickness/2,
            self.thickness,
            self.height - self.separator_innen_shift - self.lower_cut,
            self.width/4 + self.separator_shift/2 - self.thickness/4,
            0,
            -self.separator_innen_shift/2 - self.lower_cut/2)
        self.paint_red(hseparator_left)
        self.add(hseparator_left)


