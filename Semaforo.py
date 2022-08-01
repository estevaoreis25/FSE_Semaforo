from gpiozero import LED
from time import sleep


class Semaforo:
  def __init__(self, n_semaforo, vermelho, verde, amarelo):
    self.n_semaforo = n_semaforo
    self.vermelho = LED(vermelho)
    self.verde = LED(verde)
    self.amarelho = LED(amarelo)
    self.vermelho.off()
    self.amarelho.off()
    self.verde.off()

  def pare(self):
    self.vermelho.on()
    self.amarelho.off()
    self.verde.off()
  
  def atencao(self):
    self.vermelho.off()
    self.amarelho.on()
    self.verde.off()

    
  def passe(self):
    self.vermelho.off()
    self.amarelho.off()
    self.verde.on()

  def ativa_modo_noturno(self):
    self.vermelho.off()
    self.amarelho.on()
    self.verde.off()
    sleep(1)
    self.amarelho.off()

  def desliga_semaforo(self):
    self.vermelho.close()
    self.amarelho.close()
    self.verde.close()
    