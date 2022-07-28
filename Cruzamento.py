from Semaforo import Semaforo 
from gpiozero import Button
from time import sleep

class Cruzamento:
  def __init__(self, verm1, amar1, verd1, verm2, amar2, verd2, botao1, botao2, sensor_pass1, sensor_pass2):
    self.tempo_estado = 0
    self.estado = 0
    self.smf_principal = Semaforo(n_semaforo=1, vermelho=verm1, amarelo=amar1, verde=verd1)
    self.smf_auxiliar = Semaforo(n_semaforo=2, vermelho=verm2, amarelo=amar2, verde=verd2)
    
    self.botao_pedestre1 = Button(botao1)
    self.botao_pedestre2 = Button(botao2)
    self.is_botao_pedestre = False
    self.botao_pedestre1.when_pressed = self.modo_pedestre
    self.botao_pedestre2.when_pressed = self.modo_pedestre

    self.sensor_pass1 = Button(sensor_pass1)
    self.sensor_pass2 = Button(sensor_pass2)
    self.is_carro_esperando = False
    self.sensor_pass1.when_pressed = self.libera_via_aux
    self.sensor_pass2.when_pressed = self.libera_via_aux

  def controla_semaforos(self):
    if(self.estado == 0):
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        self.estado = 1
    elif(self.estado == 1):
        if(self.tempo_estado >= 10 and (self.is_botao_pedestre == True or self.is_carro_esperando == True)):
          self.is_botao_pedestre == False
          self.estado = 2
          self.tempo_estado = 0
        elif(self.tempo_estado >= 20):
          self.estado = 2
          self.tempo_estado = 0
        else:
          self.smf_principal.passe()
          self.smf_auxiliar.pare()
          self.tempo_estado +=1
    elif(self.estado == 2):
        self.smf_principal.atencao()
        self.smf_auxiliar.pare()
        self.estado = 3
    elif(self.estado == 3):
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        self.estado = 4
    elif(self.estado == 4):
        if(self.tempo_estado >= 10):
          self.estado = 5
          self.tempo_estado = 0
        else:
          self.smf_principal.pare()
          self.smf_auxiliar.passe()
          self.tempo_estado +=1
        self.is_botao_pedestre = False
        self.is_carro_esperando = False
    elif(self.estado == 5):
        self.smf_principal.pare()
        self.smf_auxiliar.atencao()
        self.estado = 0
    elif(self.estado == 6):
        self.smf_principal.ativa_modo_noturno()
        self.smf_auxiliar.ativa_modo_noturno()
    
    print(f'Pedestre quer passar? {self.is_botao_pedestre}')
    print(f'Tem carro esperando? {self.is_carro_esperando}')
    print(f'TEMPO(s): {self.tempo_estado}')


  def ativa_noturno(self):
    self.estado = 6
  
  def ativa_emergencia(self):
    self.estado = 7

  def desativa_noturno_emergencia(self):
    self.estado = 0
  
  def modo_pedestre(self):
    if(self.estado != 4):
      self.is_botao_pedestre = True
    else:
      self.is_botao_pedestre = False

  def libera_via_aux(self):
    if(self.estado != 4):
      self.is_carro_esperando = True
    else:
      self.is_carro_esperando = False
  
  