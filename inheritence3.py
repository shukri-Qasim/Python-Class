# this is the  first parent class named ElectricVehicle
class ElectricVehicle:
    # Constructor to initialize the battery capacity for an electric vehicle
    def __init__(self, battery_capacity):#attribute 
        self.battery_capacity = battery_capacity #assigning to a battery capacity
    
    # Method to display the battery capacity
    def display_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# this is the second parent class named GasolineVehicle
class GasolineVehicle:
    # Constructor to initialize the fuel capacity for a gasoline vehicle
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity #assigning to a fuel capacity
    
    # Method to display the fuel capacity
    def display_fuel_info(self):
        print(f"Fuel Capacity: {self.fuel_capacity} liters")

# this is thechild class named HybridCar that inherits from both ElectricVehicle and GasolineVehicle
class HybridCar(ElectricVehicle, GasolineVehicle):
    # Constructor to initialize the battery capacity, fuel capacity, and model of the hybrid car
    def __init__(self, battery_capacity, fuel_capacity, model):
        # Call the constructor of ElectricVehicle to initialize battery capacity
        ElectricVehicle.__init__(self, battery_capacity)
        # Call the constructor of GasolineVehicle to initialize fuel capacity
        GasolineVehicle.__init__(self, fuel_capacity)
        # Initialize the model of the hybrid car
        self.model = model
    
    # Method to display information about the hybrid car
    def display_hybrid_info(self):
        # Print the model of the hybrid car
        print(f"Model: {self.model}")
        # Call the method to display battery information (inherited from ElectricVehicle)
        self.display_battery_info()
        # Call the method to display fuel information (inherited from GasolineVehicle)
        self.display_fuel_info()

# Create an instance of HybridCar with specific values for battery capacity, fuel capacity, and model
hybrid_car = HybridCar(15, 50, "Toyota Prius")

# Display the information about the hybrid car using the display_hybrid_info method
hybrid_car.display_hybrid_info()
