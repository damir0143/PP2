#device smartphone laptop 
#1. brand model 
#device info 
#2 storage 
#3. operation system and ram 


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand, model)
        self.storage = storage

    def device_info(self):
        return f"{super().device_info()}, Smartphone storage: {self.storage} GB"


class Laptop(Device):
    def __init__(self, brand, model, ram, operating_system):
        super().__init__(brand, model)
        self.ram = ram
        self.operating_system = operating_system

    def device_info(self):
        return f"{super().device_info()}, Laptop RAM: {self.ram} GB, Operating System: {self.operating_system}"


device = Device("Iphone", "17 Pro Max")
phone = Smartphone("Samsung", "Galaxy S23", 256)
laptop = Laptop("Dell", "XPS 15", 16, "Windows 11")

print(device.device_info())
print(phone.device_info())
print(laptop.device_info())



