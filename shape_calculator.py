class Rectangle:
  def __init__(self, wd, h):
    self.width = wd
    self.height = h

  def __str__(self):
    rstr = 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    return rstr

  def set_width(self, wd):
    self.width = wd

  def set_height(self,h):
    self.height = h

  def get_perimeter(self):
    return self.width *2 + self.height *2

  def get_area(self):
    return self.width * self.height

  def get_amount_inside(self, sq):
    return int(self.get_area()/ sq.get_area())

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    pic=''
    for i in range(self.height):
      for j in range(self.width):
        pic += '*'
      pic += '\n'
    return pic
  
  def get_diagonal(self):
    return (self.width **2 + self.height**2) **.5

class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side

  def set_width(self, wd):
    self.width = wd
    self.height = wd

  def set_height(self,h):
    self.width = h
    self.height = h

  def set_side(self,side):
    self.width = side
    self.height = side

  def __str__(self):
    square_str = 'Square(side=' + str(self.width) + ')'
    return square_str  

