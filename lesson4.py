# class Car:
#     def __init__(self,model, year,):
#         self.model = model
#         self.year = year
#     def info (self):
#         print(f"бренд -{self.model} ","год выпуска - {self.year}")
        
# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(model, year)
#         self.battery = battery
        
#     def drive(self):
#         print(f"машина - {self.model} едет на электричестве")
        
# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(model, year)
#         self.fuel_bank = fuel_bank
        
#     def drive(self):
#         print(f"машина - {self.model} едет на топливе")
        
# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year,battery,fuel_bank):
#         super().__init__(model,year,battery)
#         FuelCar.__init__(self,model, year,fuel_bank)
        
#     def drive(self):
#         print(f"машина - {self.model} едет и на топливе и на электричестве")

# lexus = HybridCar("lexus - ex300",2020 , 90)
# lexus.info()
# lexus.drive()       

        
# # tesla = ElectricCar("tesla - model x",2024,90)
# # tesla.info()
# # tesla.drive()

# # matiz= FuelCar("matiz - 3",2020,30)
# # matiz.info()
# # matiz.drive()
    #   //////////////////////////////////////
# class Car: 
#     def __init__(self, model, year): 
#         self.model = model 
#         self.year = year 
         
         
#     def info(self): 
#         print(f"Модель - {self.model}, Год выпуска - {self.year}") 
         
# class ElectricCar(Car): 
#     def __init__(self, model, year, battery): 
#         Car.__init__(self,model, year) 
#         self.battery = battery 
         
         
#     def drive(self): 
#         print(f"Мишина - {self.model} едет на электричестве") 
         
         
# class FuelCar(Car): 
#     def __init__(self, model, year, fuel_bank): 
#         Car.__init__(self,model, year) 
#         self.fuel_bank = fuel_bank 
         
         
#     def drive(self): 
#         print(f"Мишина - {self.model} едет на топливе") 
         
         
         
# class HybridCar(ElectricCar,FuelCar): 
#     def __init__(self, model, year, battery, fuel_bank): 
#         super().__init__(model, year, battery) 
#         FuelCar.__init__(self,model, year, fuel_bank) 
         
#     def drive(self,speed): 
#         if speed >= 60:
#             print(f"Мишина - {self.model} едет на топливе")
#         else:
#             print(f"Мишина - {self.model} едет на электричестве")        
    
    
 
# tesla = ElectricCar("Tesla - Model X", 2024, 90) 
# tesla.info() 
# tesla.drive() 
 
 
# matiz = FuelCar("Matiz - 3 ", 2020, 30) 
# matiz.info() 
# matiz.drive() 
 
 
# lexus = HybridCar("Lexus - es300 ", 2020, 40, 60) 
# lexus.info() 
# lexus.drive(60)

# ?????????????????????????????

class Car: 
    def __init__(self, model, year): 
        self.model = model 
        self.year = year 
         
         
    def info(self): 
        print(f"Модель - {self.model}, Год выпуска - {self.year}")
    
    def __str__(self):
        return f"Модель - {self.model}, Год выпуска - {self.year}" 
      
bmw = Car("bmw - m5",2022)
print(bmw) 
