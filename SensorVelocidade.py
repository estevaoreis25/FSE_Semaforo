from gpiozero import DigitalInputDevice
import time
from threading import Thread

from soupsieve import select
class SensorVelocidade:
  def __init__(self, sensor_v_a, sensor_v_b):
      self.sensor_v_a = DigitalInputDevice(sensor_v_a, pull_up=True)
      self.sensor_v_b = DigitalInputDevice(sensor_v_b, pull_up=True)
      self.sensor_v_a.when_activated = self.calcula_velocidade
      self.sensor_v_a.when_deactivated = self.set_carro_passando
      self.sensor_v_b.when_activated = self.registra_ti
      self.quantidade_carros = 0
      self.velocidade_media = 0
      self.velocidades = []
      self.velocidade_via = 0
      self.ti = 0
      self.tf = 0  
      self.carro_parado = False
      self.verifica_carro_parado = Thread(target=self.is_carro_parado)  
      self.infracao_sinal_vermeho = 0
      self.qtd_carros_sinal_vermelho = 0
      self.infracao_limite_velocidade = 0
      self.velocidade_maxima = 60

  def registra_ti(self):
    print("VALOR INICIAL")
    self.ti = time.time()

  
  def calcula_velocidade(self):
    self.quantidade_carros+=1
    self.qtd_carros_sinal_vermelho+=1
    self.tf = time.time()
    #self.verifica_carro_parado.start()
    # delta s/ deslta t
    self.velocidade_media = int((1.0/(self.tf - self.ti)) * 3.6)
    self.velocidades.append(self.velocidade_media)
    self.velocidade_via = int(sum(self.velocidades)/len(self.velocidades))
    print(f'Velocidade media: {self.velocidade_media}km')
    print(f'Velocidade media da via: {self.velocidade_via}km')
    if(self.velocidade_media > self.velocidade_maxima):
      self.infracao_limite_velocidade+=1

  def get_quantidade_carros(self):
    return self.quantidade_carros

  def get_infracoes_sinal_vermelho(self):
    return self.infracao_sinal_vermeho

  def reinicia_contagem_carros(self):
    self.qtd_carros_sinal_vermelho = 0

  def is_carro_parado(self):
    time.sleep(1)
    if self.sensor_v_a.is_pressed:
      self.carro_parado = True
    else:
      self.carro_parado = False

  def get_carro_parado(self):
    return self.carro_parado

  def set_carro_passando(self):
    self.carro_parado = False

  def get_infracoes_sinal_vermelho(self):
    return self.infracao_sinal_vermeho
  
  def set_infracoes_sinal_vermelho(self):
    self.infracao_sinal_vermeho += self.qtd_carros_sinal_vermelho

  def get_excesso_velocidade(self):
    return self.infracao_limite_velocidade