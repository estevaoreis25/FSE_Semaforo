from Semaforo import Semaforo 
from time import sleep 
from gpiozero import Button

class Cruzamento:
  def __init__(self, verm1, amar1, verd1, verm2, amar2, verd2, botao1, botao2):
    self.tempo_estado = 0
    self.estado = 0
    self.smf_principal = Semaforo(n_semaforo=1, vermelho=verm1, amarelo=amar1, verde=verd1)
    self.smf_auxiliar = Semaforo(n_semaforo=2, vermelho=verm2, amarelo=amar2, verde=verd2)
    self.botao_pedestre1 = Button(botao1)
    self.botao_pedestre2 = Button(botao2)
    self.is_botao_pedestre = False
    self.botao_pedestre1.when_pressed = self.modo_pedestre

  def controla_semaforos(self):
    match self.estado:
      case 0:
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        self.estado = 1
      case 1:
        if(self.tempo_estado > 10 and self.is_botao_pedestre == True):
          self.is_botao_pedestre == False
          self.estado = 2
          self.tempo_estado = 0
        elif(self.tempo_estado > 20):
          self.estado = 2
          self.tempo_estado = 0
        else:
          self.smf_principal.passe()
          self.smf_auxiliar.pare()
          self.tempo_estado +=1
      case 2:
        self.smf_principal.atencao()
        self.smf_auxiliar.pare()
        self.estado = 3
      case 3:
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        self.estado = 4
      case 4:
        if(self.tempo_estado > 10):
          self.estado = 5
          self.tempo_estado = 0
        else:
          self.smf_principal.pare()
          self.smf_auxiliar.passe()
          self.tempo_estado +=1
      case 5:
        self.smf_principal.pare()
        self.smf_auxiliar.atencao()
        self.estado = 0
      case 6:
        self.smf_principal.ativa_modo_noturno()
        self.smf_auxiliar.ativa_modo_noturno()

    if(self.estado < 6):
      self.estado+=1
    elif(self.estado == 6):
      self.estado = 0
    elif(self.estado == 7):
      self.estado = 0


  def ativa_noturno(self):
    self.estado = 6
  
  def ativa_emergencia(self):
    self.estado = 7

  def desativa_noturno_emergencia(self):
    self.estado = 0
  
  def modo_pedestre(self):
    self.is_botao_pedestre = True