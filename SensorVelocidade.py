from gpiozero import Button
import time
class SensorVelocidade:
  def __init__(self, sensor_v_a, sensor_v_b):
      self.sensor_v_a = Button(sensor_v_a)
      self.sensor_v_b = Button(sensor_v_b)
      self.sensor_v_a.when_pressed = self.calcula_velocidade
      self.sensor_v_b.when_pressed = self.registra_ti
      self.quantidade_carros = 0
      self.velocidade_media = 0
      self.velocidades = []
      self.velocidade_via = 0
      self.ti = 0
      self.tf = 0  
      print("Sensor de velocidade criado")   

  def registra_ti(self):
    self.ti = time.time()
  

  def calcula_velocidade(self):
    self.tf = time.time()
    # delta s/ deslta t
    self.velocidade_media = round((1.0/(self.tf - self.ti)) * 3.6, 2)
    self.velocidades.append(self.velocidade_media)
    self.velocidade_via = sum(self.velocidades)/len(self.velocidades)
    print(f'Velocidade media: {self.velocidade_media}km')
    print(f'Velocidade media da via: {self.velocidade_via}km')
    
