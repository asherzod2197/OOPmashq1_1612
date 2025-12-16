# 1
class Ishchi:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        return f"Ishchi: {self.ism}, Maosh: {self.maosh} so'm"

    def maosh_oshir(self, foiz):
        self.maosh += self.maosh * foiz / 100

ishchi1 = Ishchi("Ali", 3000000)

print(ishchi1.malumot())

ishchi1.maosh_oshir(10)
print(ishchi1.malumot())


# 2
class Velosiped:
    def __init__(self, turi, tezlik=0):
        self.turi = turi
        self.tezlik = tezlik

    def tezlik_oshir(self, qiymat):
        self.tezlik += qiymat

    def toxtat(self):
        self.tezlik = 0


v1 = Velosiped("Sport")

v1.tezlik_oshir(15)
print(v1.turi, "tezligi:", v1.tezlik)

v1.toxtat()
print(v1.turi, "tezligi:", v1.tezlik)
