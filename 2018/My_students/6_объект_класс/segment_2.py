

import sys
import math

class Direction(object):
	def __init__(self, dx=0, dy=0):
		self.dx = dx
		self.dy = dy

	def __str__(self):
		return '{} {}'.format(self.dx, self.dy)

	def __repr__(self):
		return 'Direction({},{})'.format(self.dx, self.dy)


class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '{} {}'.format(self.x, self.y)

	def __repr__(self):
		return 'Point({}, {})'.format(self.x, self.y)

	def move(self, dir=None):
		if dir is None:
			return

		self.x +=dir.dx
		self.y +=dir.dy

	def dir(self, other=object):
		if other is None:
			other = Point(0,0)

		dx = self.x - other.x
		dy = self.y - other.y

		return Direction(dx,dy)

	def dist2(self, other):
		"""Квадрат рсстояния до точки other"""
		dx = self.x - other.x
		dy = self.y - other.y

		return dx*dx + dy*dy

	def dist0(self, other):
		"""Квадрат рсстояния до точки (0,0)"""
		return dist2(Point(0,0))

class Segment2(object):
	def __init__(self, start=None, finish=None):
		self.start = start or Point()
		self.finish = finish or Point()

	def __str__(self):
		return '{} {}'.format(self.start, self.finish)

	def length2(self):
		return self.start.dist2(self.finish)

	def length(self):
		return math.sqrt(self.length2())

	def move(self, dir=None):
		self.start.move(dir)
		self.finish.move(dir)

	def left(self):
		return self.start.x


if __name__ == "__main__":

	def read_segment2(str):
		x1, y1, x2, y2 = map(int, str.split())
		s = Segment2(Point(x1,y1),Point(x2,y2))
		return s

	def move_to_zero(a):
		zero = Point(0,0)
		for s in a:
			dir = zero.dir(s.start) # вычисляем Direction от точки (0,0) до точки start отрезки
			#print (s)
			s.move(dir) #двигаем отрезок s на это dir
			print (s)

	a = []

	for str in sys.stdin:
		s = read_segment2(str)
		a.append(s)

	move_to_zero(a)


















