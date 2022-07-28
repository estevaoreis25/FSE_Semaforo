from gpiozero import Button
class SensorVelocidade:
  def __init__(self, sensor_v_a, sensor_v_b):
      self.sensor_v1_a = Button(sensor_v_a)
      self.sensor_v1_b = Button(sensor_v_b)
      self.quantidade_carros = 0
      self.velocidade_media = 0
      self.velocidades = []
  

