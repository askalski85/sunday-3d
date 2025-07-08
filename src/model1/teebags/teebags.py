import trimesh

from ..model_libs.units import *
from ..model_libs.api import API

class Teebags(API):
    name: str = 'teebags'
    label_height: mm = 80  # wysokosc etykiety
    label_thickness: mm = 6
    label_hole: mm = 3.6
    label_preview: mm = 12
    height: mm = 120  # wysokosc y
    width: mm = 70  # szerokosc x
    depth: mm = 85  # glebokosc z
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
        # self.paint_red(main_label)
        self.addform(main_label, 0, 0, self.thickness)

    def top(self) -> None:
        top1 = self.box(self.label_thickness/2, self.depth - self.label_thickness, self.thickness, self.label_thickness/4 - self.width/2, self.label_thickness/2, self.height - self.thickness/2)  ## top
        # self.paint_green(top1)
        self.add(top1)
        top2 = self.box(self.label_thickness/2, self.depth - self.label_thickness, self.thickness, -self.label_thickness/4 + self.width/2, self.label_thickness/2, self.height - self.thickness/2)  ## top
        # self.paint_blue(top2)
        self.add(top2)
        top3 = self.box(self.width, self.label_thickness/2 , self.thickness, 0, self.depth/2 - self.label_thickness/4, self.height - self.thickness/2)  ## top
        # self.paint_red(top3)
        self.add(top3)

        # pins
        left_pin = top1.intersection(top3)
        self.addform(left_pin, 0, 0, self.thickness)

        right_pin = top2.intersection(top3)
        self.addform(right_pin, 0, 0, self.thickness)

        # trojkatne podpory
        triangle_back = self.triangle(5, self.label_thickness/2, self.width)
        triangle_back = self.rotate_y(triangle_back, 90)
        triangle_back = self.rotate_z(triangle_back, 180)
        # self.paint_blue(triangle_back)
        self.addform(triangle_back, self.width/2, self.depth/2, self.height - self.thickness)

        triangle_left = self.triangle(5, self.label_thickness/2, self.depth - self.label_thickness)
        triangle_left = self.rotate_y(triangle_left, 90)
        triangle_left = self.rotate_z(triangle_left, -90)
        # self.paint_blue(triangle_left)
        self.addform(triangle_left, -self.width/2, self.depth/2 , self.height - self.thickness)

        triangle_right = self.triangle(5, self.label_thickness/2, self.depth - self.label_thickness)
        triangle_right = self.rotate_y(triangle_right, 90)
        triangle_right = self.rotate_z(triangle_right, 90)
        # self.paint_blue(triangle_right)
        self.addform(triangle_right, self.width/2, -self.depth/2 + self.label_thickness, self.height - self.thickness)

    def bottom(self):
        cutoff_size = self.label_thickness/2 + 1
        cutoff_height = self.thickness + 1
        cutoff_right = self.box(cutoff_size, cutoff_size, cutoff_height, self.width/2 - cutoff_size/2, self.depth/2 - cutoff_size/2, cutoff_height/2)
        # self.paint_blue(cutoff_right)
        # self.add(cutoff_right)
        cutoff_left = self.box(cutoff_size, cutoff_size, cutoff_height, -self.width/2 + cutoff_size/2, self.depth/2 - cutoff_size/2, cutoff_height/2)
        # self.paint_red(cutoff_left)
        # self.add(cutoff_left)

        bottom = self.box(self.width, self.depth - self.label_thickness, self.thickness, 0, self.label_thickness/2, self.thickness/2)  # bottom
        # cutoff = self.box(self.width, self.label_thickness, 2*self.thickness, 0, self.depth/2 - self.label_thickness/2, self.thickness/2)  ## top
        # self.paint_blue(cutoff)
        # self.add(cutoff)
        bottom = bottom.difference(cutoff_left).difference(cutoff_right)
        self.add(bottom)


        right = self.box(self.thickness, self.depth - self.label_thickness, self.height, self.width/2 - self.thickness/2, self.label_thickness/2, self.height/2)   # right wall
        right = right.difference(cutoff_right).difference(cutoff_right)
        self.add(right)

        left = self.box(self.thickness, self.depth - self.label_thickness, self.height, -self.width/2 + self.thickness/2, self.label_thickness/2, self.height/2)  # left wall
        left = left.difference(cutoff_left).difference(cutoff_right)
        self.add(left)

        back = self.box(self.width, self.thickness, self.height, 0, self.depth/2 - self.thickness/2, self.height/2)   # back wall
        back = back.difference(cutoff_left).difference(cutoff_right)
        self.add(back)

    def build(self):

        self.bottom()
        self.label()
        self.top()
        
        # Label bottom
        cutoff_box = self.box(self.width - 2*self.thickness, 2, 2, 0, -self.depth/2 + self.label_thickness, self.height - self.label_height-8)
        # self.paint_blue(cutoff_box)
        # self.add(cutoff_box)
        
        triangle = self.triangle(10, self.label_thickness, self.width)
        # self.paint_green(triangle)
        triangle = self.rotate_y(triangle, 90)
        triangle = self.rotate_z(triangle, 180)
        self.transform(triangle, self.width/2, -self.depth/2 + self.label_thickness, self.height - self.label_height + self.thickness)
        triangle = triangle.difference(cutoff_box)
        self.add(triangle)

        box = self.box(self.width, self.thickness, 10, 0, -self.depth/2 + self.label_thickness - self.thickness/2, self.height - self.label_height-8)
        # self.paint_blue(box)
        self.add(box)

        # trojkatny dol
        triangle_bottom = self.triangle(20, 4, self.thickness)
        # self.paint_red(triangle_bottom)
        self.rotate_y(triangle_bottom, 90)
        self.rotate_x(triangle_bottom, 90)
        self.addform(triangle_bottom.copy(), self.width/4, -self.depth/2 + self.label_thickness, self.thickness)
        self.addform(triangle_bottom.copy(), -self.width/4, -self.depth/2 + self.label_thickness, self.thickness)
        self.addform(triangle_bottom.copy(), 0, -self.depth/2 + self.label_thickness, self.thickness)

