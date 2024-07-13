import math
class calculator:
    def __init__(self ,n) -> None:
        self.n=n
    def square(self):
        print(f"the square of the number is {self.n*self.n}")
    def cube(self):
        print(f"the cube of the number is {self.n**3}")
    def sqrt(self):
      
        result = math.ceil(math.sqrt(self.n))
        print(f"the sqrt root of the number is {result}")
    def multi(self):
        print(f"the multi of the number is {self.n*self.n/2}")
a=calculator(4)
a.square()
a.cube()
a.sqrt()
a.multi()