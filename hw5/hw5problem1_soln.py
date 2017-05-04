"""
Author: Tevin Rivera
Solution module for Homework 5, Problem 1
Object Oriented Programming (50:198:113), Spring 2016

No documentation included due to time constraints!
"""

import math

class Point:
    def __init__(self, init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y

    def translate(self, s, t):
        self.x += s
        self.y += t

    def rotate(self, theta):
        oldx = self.x
        theta_rad = theta * math.pi / 180
        self.x = self.x * math.cos(theta_rad) - self.y * math.sin(theta_rad)
        self.y = oldx * math.sin(theta_rad) + self.y * math.cos(theta_rad)

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def left_of(self, q, r):
        first = r.x * self.y - self.x * r.y
        second = q.x * r.y - q.x * self.y
        third = q.y * self.x - q.y * r.x
        return (first + second + third) > 0

    def right_of(self, q, r):
        first = r.x * self.y - self.x * r.y
        second = q.x * r.y - q.x * self.y
        third = q.y * self.x - q.y * r.x
        return (first + second + third) < 0

    def __str__(self):
        return "(%.2f, %.2f)"%(self.x, self.y)

    def __repr__(self):
        return str(self)

class SimplePoly:
    def __init__(self, *vertices):
        self.vertexlist = list(vertices)
        for p in self.vertexlist:
            if type(p) != Point:
                raise Exception("Incorrect parameter to SimplePoly __init__")

    def translate(self, s, t):
        for p in self.vertexlist:
            p.translate(s, t)

    def rotate(self, theta):
        for p in self.vertexlist:
            p.rotate(theta)

    def __iter__(self):
        return SimplePolyIterator(self.vertexlist)

    def __len__(self):
        return len(self.vertexlist)

    def __getitem__(self, idx):
        if idx not in range(len(self)):
            raise IndexError
        return self.vertexlist[idx]

    def __str__(self):
        astr = ""
        for p in self.vertexlist:
            astr += str(p) + " "
        return astr[:-1]

    def perimeter(self):
        peri = 0
        num_verts = len(self)
        for i in range(num_verts):
            peri += self[i].distance(self[(i+1)%num_verts])
        return peri

class SimplePolyIterator:
    def __init__(self, vlist):
        self.vertexlist = vlist
        self.current_index = 0

    def __next__(self):
        if self.current_index >= len(self.vertexlist):
            raise StopIteration
        answer = self.vertexlist[self.current_index]
        self.current_index += 1
        return answer

class ConvPoly(SimplePoly):
    def __init__(self, *vertices):
        SimplePoly.__init__(self, *vertices)

        # Now check if the counter-clockwise list of vertices
        # defines a convex polygon.

        num_verts = len(self)
        for i in range(num_verts):
            if not self[i].left_of(self[(i-2)%num_verts], self[(i-1)%num_verts]):
                raise Exception("ConvPoly __init__: Polygon is not convex")

class EquiTriangle(ConvPoly):
    def __init__(self, init_len):
        ConvPoly.__init__(self, Point(0, 0),
                          Point(init_len, 0),
                          Point(init_len/2.0, math.sqrt(3)*init_len/2.0))
    def area(self):
        """
        Return area of the equilateral triangle
        Area = base * height/2 = sqrt(3) * (side length)^2 / 4.0
        """
        return (math.sqrt(3) * (self[0].distance(self[1])**2)/4.0)

class Rectangle(ConvPoly):
    def __init__(self, init_len, init_wid):
        ConvPoly.__init__(self, Point(0,0),
                          Point(init_len, 0),
                          Point(init_len, init_wid),
                          Point(0, init_wid))
    def area(self):
        """
        Return area of rectangle
        Area = length * width
        """
        return (self[0].distance(self[1]) * self[1].distance(self[2]))

class Square(Rectangle):
    def __init__(self, init_len):
        Rectangle.__init__(self, init_len, init_len)
