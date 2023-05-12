class Carro:
    
    
    def __init__(self, piloto, equipe, modelo, velocidadeMedia, tempoVolta):
        self.piloto = piloto
        self.equipe = equipe
        self.modelo = modelo
        self.velocidadeMedia = velocidadeMedia
        self.tempoVolta = tempoVolta
        
    @property
    def competidor(self):
        return '{} da {} ultrapassou'.format(self.piloto, self.equipe)
    
    @property
    def mediaVolta(self):
        self.media = int(self.velocidadeMedia)/int(self.tempoVolta)
        