class Cylinder() :
  def __init__(self,radius,height) :
    self.radius = radius
    self.height = height
  
  def get_radius(self) :
    return self.radius
  def get_height(self) :
    return self.height
  def set_radius(self,radius) :
    self.radius = radius
  def set_height(self,height) :
    self.height = height

  def base_area(self) : 
    base_area = 3 * (self.radius ** 2 )
    return base_area

  def surface_area(self) :
    surface_area = 2 * 3 * (self.radius) * (self.height)
    return surface_area

  def area_calculator(self) :
    base_area = self.base_area()
    surface_area = self.surface_area()
    area = (2 * base_area) + surface_area
    return area

  def volume_calculator(self) :
    base_area = self.base_area()
    volume = base_area * self.height
    return volume

a = Cylinder(3,5)
print(a.area_calculator())
print(a.volume_calculator())
