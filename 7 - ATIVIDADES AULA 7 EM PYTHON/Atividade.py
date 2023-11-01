class Veiculo:
    def __init__(self,ano,peso,tanque,modelo):
        self.ano=int(ano)
        self.peso=int(peso)
        self.tanque=float(tanque)
        self.modelo=modelo
    
    def getAno(self):
        return self.ano
    
    def getPeso(self):
        return self.peso
    
    def getTanque(self):
        return self.tanque
    
    def getModelo(self):
        return self.modelo
    
    def setAno(self,ano):
        self.ano=int(ano)
    
    def setPeso(self,peso):
        self.peso=int(peso)
    
    def setTanque(self,tanque):
        self.tanque=float(tanque)
    
    def setModelo(self,modelo):
        self.modelo=modelo
    
    def info(self):
        print('Ano do veículo:',self.getAno())
        print('Peso do veículo:',self.getPeso())
        print('Tamanho do tanque:',self.getTanque())
        print('Modelo do veículo:',self.getModelo())

class Terrestre(Veiculo):
    def __init__(self,ano,peso,tanque,modelo,qtRoda,qtPorta):
        super().__init__(ano,peso,tanque,modelo)
        self.qtRoda=int(qtRoda)
        self.qtPorta=int(qtPorta)
    
    def getQtRoda(self):
        return self.qtRoda
    
    def getQtPorta(self):
        return self.qtPorta
    
    def setQtRoda(self,qtRoda):
        self.qtRoda=int(qtRoda)

    def setQtPorta(self,qtPorta):
        self.qtPorta=int(qtPorta)

    def info(self):
        super().info()
        print('Quantidade de Rodas:',self.getQtRoda())
        print('Quantidade de Portas:',self.getQtPorta())
        print('Consumo: {:.2f}km/l.'.format(self.consumo()))
        print('Autonomia do veículo: {:.2f}km.'.format(self.autonomia()))
                                                                                        
    def consumo(self):                                                                     
        peso=self.getPeso()
        consumo=1/((peso*0.00005)+(self.getQtRoda()*0.005))
        return consumo

    def autonomia(self):
        autonomia=self.tanque*self.consumo()
        return autonomia

class Aereo(Veiculo):
    def __init__(self,ano,peso,tanque,modelo,qtAsa,qtMotor):
        super().__init__(ano,peso,tanque,modelo)
        self.qtAsa=int(qtAsa)
        self.qtMotor=int(qtMotor)

    def getQtAsa(self):
        return self.qtAsa 
    
    def getQtMotor(self):
        return self.qtMotor
    
    def setQtAsa(self,qtAsa):
        self.qtAsa=int(qtAsa)

    def setQtMotor(self,qtMotor):
        self.qtMotor=int(qtMotor)

    def info(self):
        super().info()
        print('Quantidade de Asas:',self.getQtMotor())
        print('Quantidade de Motores:',self.getQtAsa())
        print('Consumo: {:.2f}km/l.'.format(self.consumo()))
        print('Autonomia do veículo: {:.2f}km.'.format(self.autonomia()))

    def consumo(self):
        consumo=1/((self.peso*0.00003)+(self.qtMotor*0.01))
        return consumo
    
    def autonomia(self):
        autonomia=self.tanque*self.consumo()
        return autonomia

class Aquatico(Veiculo):
    def __init__(self,ano,peso,tanque,modelo,qtMotor,qtConves):
        super().__init__(ano,peso,tanque,modelo)
        self.qtMotor=int(qtMotor)
        self.qtConves=int(qtConves)

    def getQtMotor(self):
        return self.qtMotor
    
    def getQtConves(self):
        return self.qtConves
    
    def setQtMotor(self,qtMotor):
        self.qtMotor=int(qtMotor)

    def setQtConves(self,qtConves):
        self.qtConves=int(qtConves)

    def info(self):
        super().info()
        print('Quantidade de Motores:',self.getQtMotor())
        print('Quantidade de Conves:',self.getQtConves())
        print('Consumo: {:.2f}km/l.'.format(self.consumo()))
        print('Autonomia do veículo: {:.2f}km.'.format(self.autonomia()))

    def consumo(self):
        consumo=1/((self.peso*0.00002)+(self.qtMotor*0.02))
        return consumo
    
    def autonomia(self):
        autonomia=self.tanque*self.consumo()
        return autonomia

if __name__ == "__main__":
    veiculo1=Veiculo(2022,1000,20,'Civic')
    print('\nVeículo 1')
    veiculo1.info()
    veiculoTerrestre=Terrestre(2020,2000,40,'Ranger',4,4)
    print('\Veículo 2')
    veiculoTerrestre.info()
    veiculoAereo=Aereo(2018,850,30,'F-50',2,2)
    print('\nVeículo 3')
    veiculoAereo.info()
    veiculoAquatico=Aquatico(2021,10000,1000,'Kosatska',6,3)
    print('\nVeículo 4')
    veiculoAquatico.info()