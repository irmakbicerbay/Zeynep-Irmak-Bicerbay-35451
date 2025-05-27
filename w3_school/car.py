class Car:

    def __init__(self, brand):
        self.brand = brand              
        self.__engine_status = 'off'    

    def display_engine_status(self):    
        print(f"Engine status: {self.__engine_status}")

    def start_the_car(self):       
        self.__start_the_engine() 

    def __start_the_engine(self):   
        self.__engine_status = 'on'
        print("Engine has started")

my_car = Car("Audi")
my_car.display_engine_status()  
my_car.start_the_car()         
my_car.display_engine_status() 
