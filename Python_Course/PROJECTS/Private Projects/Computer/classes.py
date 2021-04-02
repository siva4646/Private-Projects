class Computer:
    def __init__(self, model, frequency):
        self.model = model
        self.frequency = frequency
    def Model(self, model):
        return str(self.model)
    def cpu_freq(self, frequency):
        return int(self.frequency)

class Desktop(Computer):
    def __init__(self, graphics):
        self.graphics = graphics
    def Graphics(self, graphics):
        return self.graphics


class Laptop(Desktop):
    def __init__(self, weight):
        self.weight = weight
    def Weight(self, weight):
        return weight

test = Desktop(input("Graphics: "))
test.cpu_freq = int(input("CPU Frequency: "))
test.model = str(input("Model: "))
#graphics = ['GeForce', 'Nvidia']
test.weight = float(input("Weight: "))
print(f'''
Graphics: {test.graphics}
CPU Frequency: {test.cpu_freq}
Model: {test.model}
Weight: {test.weight}
''')