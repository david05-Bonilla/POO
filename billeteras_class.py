class Billeteras:
    def __init__(self, material, money):
        self.material = material
        self.money = money
    
    def guardar(self):
        print(f"Esta billetera es de {self.material} y tiene {self.money} dolares")
    