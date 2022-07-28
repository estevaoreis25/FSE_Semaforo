from gpiozero import LED
from time import sleep


class Semaforo:
  def __init__(self, n_semaforo, vermelho, verde, amarelo):
    self.n_semaforo = n_semaforo
    self.vermelho = LED(vermelho)
    self.verde = LED(verde)
    self.amarelho = LED(amarelo)
    self.is_verde = False
    self.is_vermelho = True
    self.is_amarelo = False


  def pare(self):
    self.vermelho.on()
    self.amarelho.off()
    self.verde.off()
    self.is_verde = False
    self.is_vermelho = True
    self.is_amarelo = False
  
  def atencao(self):
    self.vermelho.off()
    self.amarelho.on()
    self.verde.off()
    self.is_verde = False
    self.is_vermelho = False
    self.is_amarelo = True
    
  def passe(self):
    self.vermelho.off()
    self.amarelho.off()
    self.verde.on()
    self.is_verde = True
    self.is_vermelho = False
    self.is_amarelo = False

  def ativa_modo_noturno(self):
    self.vermelho.off()
    self.amarelho.on()
    self.verde.off()
    sleep(1)
    self.amarelho.off()

  def desliga_semaforo(self):
    self.vermelho.off()
    self.amarelho.off()
    self.verde.off()
    