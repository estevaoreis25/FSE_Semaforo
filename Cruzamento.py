from Semaforo import Semaforo 
from time import sleep 
class Cruzamento:
  def __init__(self, verm1, amar1, verd1, verm2, amar2, verd2):
    self.estado = 0
    self.smf_principal = Semaforo(n_semaforo=1, vermelho=verm1, amarelo=amar1, verde=verd1)
    self.smf_auxiliar = Semaforo(n_semaforo=2, vermelho=verm2, amarelo=amar2, verde=verd2)

  def controla_semaforos(self):
    match self.estado:
      case 0:
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        sleep(1)
      case 1:
        self.smf_principal.passe()
        self.smf_auxiliar.pare()
        sleep(1)
      case 2:
        self.smf_principal.atencao()
        self.smf_auxiliar.pare()
        sleep(1)
      case 3:
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        sleep(1)
      case 4:
        self.smf_principal.pare()
        self.smf_auxiliar.passe()
        sleep(1)
      case 5:
        self.smf_principal.pare()
        self.smf_auxiliar.atencao()
        sleep(1)
      case 7:
        self.smf_principal.atencao()
        self.smf_auxiliar.atencao()
        sleep(1)

    if(self.estado < 6):
      self.estado+=1
    elif(self.estado == 6):
      self.estado = 0
    elif(self.estado == 7):
      self.estado = 0


  def ativa_noturno(self):
    self.estado = 7
  
  def ativa_emergencia(self):
    self.estado = 8

  def desativa_noturno_emergencia(self):
    self.estado = 0