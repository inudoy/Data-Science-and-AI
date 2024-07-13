class programmer:
    company="Microsoft"
    def __init__(self,name , salary, pin):#constructor 
        self.name=name
        self.salary=salary
        self.pin=pin
p=programmer("Imran","1200000","00100")
print(p.name,p.salary,p.pin)