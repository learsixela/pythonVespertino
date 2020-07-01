class SumaDos:
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] + 2
        self.indice += 1
        return elemento
print(list(SumaDos([1,2,3,4,5])))