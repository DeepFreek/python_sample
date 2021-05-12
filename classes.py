class Car():
    def __init__(self,label,year,odometer):
        self.label=label
        self.year=year
        self.odometer=odometer
    def Info(self):
        print("{} {} odometer:{}".format(self.label,self.year,self.odometer))
    def Inc_odom(self,Miles):
        self.odometer+=Miles
    def set_gas_value(self,gas):
        self.gas_val=gas
    def Gas_Info(self):
        print(self.gas_val)

class EC(Car):
    def __init__(self,label,year,odometer):
        super().__init__(label,year,odometer)
    def Gas_Info(self):
        print("There are no gas in EC")
audi=Car("Audi",2007,150000)
audi.Info()
audi.Inc_odom(20000)
audi.Info()
audi.set_gas_value(200)
audi.Gas_Info()
tesla=EC("Tesla",2020,10000)
tesla.Info()
tesla.Gas_Info()