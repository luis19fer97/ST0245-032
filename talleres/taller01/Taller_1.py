import math
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
 
    def dist_euclidiana(self, x, y):
      difx = abs(self.x - x)
      dify = abs(self.y - y)
      return math.sqrt(difx*difx+dify*dify)

class Date(): #name of the class
  #methods of the class
  def __init__(self, day, month, year): #Constructor initialized with attributes day, month, and year
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
      return "The dates are the same"
    elif dif > 0:
      return "The date " + str(self.day) + "/" + str(self.month) +"/" + str(self.year) + " is greather than " + str(day2) + "/" + str(month2) +"/" + str(year2)
    else:
      return "The date " + str(day2) + "/" + str(month2) +"/" + str(year2) + " is greather than " + str(self.day) + "/" + str(self.month) +"/" + str(self.year)


#print(Fecha(22,1,2020).eval(12,1,2020)) #test
