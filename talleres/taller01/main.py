"""import math
class Punto2D():


    def __init__(self, x, y):
      self.x = x
      self.y = y
        

    def get_x(self):
      return self.x
    def get_y(self):
      return self.y
    
    def radio_polar(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def angulo_polar(self):
      return math.atan2(self.y/self.x)
 

    def dist_euclidiana(self, z, q):
      Punto2D(z,q)
      difx = abs(self.x - z)
      dify = abs(self.y - q)
      return math.sqrt(difx*difx+dify*dify)"""
   

class Fecha():

  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year

  def day(self):
    return self.day

  def month(self):
    return self.month

  def year(self):
   return self.year

  def cadena(self):
    fecha = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
    return fecha
  
  def eval(self, day2, month2, year2):
    sum1 = self.day + self.month*30 + self.year*360
    sum2 = day2 + month2*30 + year2*360
    dif = sum1 - sum2
    if dif == 0:
      return "La fecha es exactamente igual"
    elif dif > 0:
      return "La fecha " + str(self.day) + "/" + str(self.month) +"/" + str(self.year) + " Es mayor que " + str(day2) + "/" + str(month2) +"/" + str(year2)
    else:
      return "La fecha " + str(day2) + "/" + str(month2) +"/" + str(year2) + " Es mayor que " + str(self.day) + "/" + str(self.month) +"/" + str(self.year)


print(Fecha(22,1,2020).eval(25,1,2020))

