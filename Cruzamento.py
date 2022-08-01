from Semaforo import Semaforo
from SensorVelocidade import SensorVelocidade 
from SensorEsperaAuxiliar import SensorEsperaAuxiliar
from BotaoPedrestre import BotaoPedesrtre
from time import sleep
import os

class Cruzamento:
  def __init__(self, id, verm1, amar1, verd1, 
                    verm2, amar2, verd2, 
                    botao1, botao2, 
                    sensor_pass1, sensor_pass2, 
                    sensor_v1_a, sensor_v1_b,
                    sensor_v2_a, sensor_v2_b):

    self.id = id
    self.contador_segundos = 0
    self.tempo_estado = 0
    self.estado = 0

    self.smf_principal = Semaforo(n_semaforo=1, vermelho=verm1, amarelo=amar1, verde=verd1)
    self.smf_auxiliar = Semaforo(n_semaforo=2, vermelho=verm2, amarelo=amar2, verde=verd2)
    
    self.is_botao_pedestre = False
    self.botao_pedestre1 = BotaoPedesrtre(botao1)
    self.botao_pedestre2 = BotaoPedesrtre(botao2)

    self.is_carro_esperando_aux = False
    self.sensor_aux1 = SensorEsperaAuxiliar(sensor_pass1)
    self.sensor_aux2 = SensorEsperaAuxiliar(sensor_pass2)

    self.is_carro_esperando_principal = False
    self.sensor_v1 = SensorVelocidade(sensor_v1_a, sensor_v1_b)
    self.sensor_v2 = SensorVelocidade(sensor_v2_a, sensor_v2_b)

    self.infracoes_sinal_vermelho = 0
    self.infracoes_excesso_velocidade = 0

  def controla_semaforos(self):
    if(self.estado == 0):
        # As duas vias fecahdas
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_v1.set_infracoes_sinal_vermelho()
        self.sensor_v2.set_infracoes_sinal_vermelho()
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        self.estado = 1
    elif(self.estado == 1):
      # Via auxiliar fechada e via princial aberta
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_v1.reinicia_contagem_carros()
        self.sensor_v2.reinicia_contagem_carros()
        if(self.tempo_estado >= 10 and self.is_carro_esperando_aux == True):
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
        # Via principal em atenção
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_v1.reinicia_contagem_carros()
        self.sensor_v2.reinicia_contagem_carros()
        self.smf_principal.atencao()
        self.smf_auxiliar.pare()
        #os.system('omxplayer example.mp3') # Avisa os pedestres que o sinal das vias auxiliares vão abrir
        self.estado = 3
    elif(self.estado == 3):
        # As duas vias fechadas
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_aux1.set_infracoes_sinal_vermelho()
        self.sensor_aux2.set_infracoes_sinal_vermelho()
        self.smf_principal.pare()
        self.smf_auxiliar.pare()
        #os.system('cvlc example.mp3') # Avisa os pedestres que o sinal das vias auxiliares vão abrir
        self.estado = 4
    elif(self.estado == 4):
        # Via auxiliar aberta e via princial fechada
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_aux1.reinicia_contagem_carros()
        self.sensor_aux2.reinicia_contagem_carros()
        if(self.tempo_estado >= 5 and (self.is_botao_pedestre or self.is_carro_esperando_principal)):
          self.estado = 5
          self.tempo_estado = 0
        elif(self.tempo_estado >= 10):
          self.estado = 5
          self.tempo_estado = 0
        else:
          self.smf_principal.pare()
          self.smf_auxiliar.passe()
          self.tempo_estado +=1
    elif(self.estado == 5):
        # Via auxiliar em atenção
        self.verifica_pedestre_esperando()
        self.verifica_carro_esperando_via_auxliar()
        self.verifica_carro_esperando_principal()
        self.sensor_aux1.reinicia_contagem_carros()
        self.sensor_aux2.reinicia_contagem_carros()
        self.smf_principal.pare()
        self.smf_auxiliar.atencao()
        self.estado = 0
        
    elif(self.estado == 6):
        self.smf_principal.ativa_modo_noturno()
        self.smf_auxiliar.ativa_modo_noturno()

    elif(self.estado == 7):
        self.smf_principal.passe()
        self.smf_auxiliar.pare()
    
    sleep(1)
    self.contador_segundos+=1

    self.infracoes_sinal_vermelho = self.sensor_v1.get_infracoes_sinal_vermelho() + self.sensor_v2.get_infracoes_sinal_vermelho() + self.sensor_aux1.get_infracoes_sinal_vermelho() + self.sensor_aux2.get_infracoes_sinal_vermelho()

    self.infracoes_excesso_velocidade = self.sensor_v1.get_excesso_velocidade()+self.sensor_v1.get_excesso_velocidade() 

    print('')
    print(f'-------------------CRUZAMENTO {self.id}--------------------')
    """print(f'Pedestre quer passar? {self.is_botao_pedestre}')
    print(f'Carro na auxiliar esperando? {self.is_carro_esperando_aux}')
    print(f'Carro na principal esperando? {self.is_carro_esperando_principal}')
    #print(f'Qtd Ultrapassagens: {self.ultrapassagens}')
    print(f'TEMPO(s): {self.tempo_estado}')
    print(f'ESTADO: {self.estado}')
    print("---------------------------------------------------")
    print(f'Qtd carros por minuto →: {int((self.sensor_v1.get_quantidade_carros()/self.contador_segundos)*60)}')
    print(f'Qtd carros por minuto ←: {int((self.sensor_v2.get_quantidade_carros()/self.contador_segundos)*60)}')
    print(f'Qtd carros por minuto ↑: {int((self.sensor_aux2.get_qtd_carros()/self.contador_segundos)*60)}')
    print(f'Qtd carros por minuto ↓: {int((self.sensor_aux1.get_qtd_carros()/self.contador_segundos)*60)}')"""
    print(f'Qtd Infraceos sinal vermelho: {self.infracoes_sinal_vermelho}')
    print(f'Qtd Infraceos sinal excesso de velocidade: {self.infracoes_excesso_velocidade}')
    print('')


  def ativa_noturno(self):
    self.estado = 6
  
  def ativa_emergencia(self):
    self.estado = 7

  def desativa_noturno_emergencia(self):
    self.estado = 0
  
  def modo_pedestre(self):
    if(self.estado != 1):
      self.is_botao_pedestre = True
    else:
      self.is_botao_pedestre = False
      
  def verifica_pedestre_esperando(self):
    if(self.estado != 1 and (self.botao_pedestre1.get_pedestre_esperando() or self.botao_pedestre2.get_pedestre_esperando())):
      self.is_botao_pedestre = True
    else:
      self.botao_pedestre1.set_pedestre_passando()
      self.botao_pedestre2.set_pedestre_passando()
      self.is_botao_pedestre = False

  def verifica_carro_esperando_via_auxliar(self):
    if(self.estado != 4 and (self.sensor_aux1.get_carro_esperando() or self.sensor_aux2.get_carro_esperando())):
      self.is_carro_esperando_aux = True
    else:
      self.is_carro_esperando_aux = False
      self.sensor_aux1.set_carro_passando()
      self.sensor_aux2.set_carro_passando()


  def verifica_carro_esperando_principal(self):
    if(self.estado != 1 and (self.sensor_v1.get_carro_parado() or self.sensor_v2.get_carro_parado())):
      self.is_carro_esperando_principal = True
    else:
      self.sensor_v1.set_carro_passando()
      self.sensor_v1.set_carro_passando()
      self.is_carro_esperando_principal = False   