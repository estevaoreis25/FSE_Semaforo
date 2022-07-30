from gpiozero import Button

class SensorEsperaAuxiliar:
  def __init__(self, sensor_espera):
    self.sensor_espera = Button(sensor_espera)
    self.sensor_espera.when_pressed = self.set_carro_esperando
    self.sensor_espera.when_released = self.set_carro_passando
    self.carro_esperando = False
    self.qtd_carros = 0


  def set_carro_esperando(self):
    self.qtd_carros+=1
    self.carro_esperando = True

  def set_carro_passando(self):
    self.qtd_carros +=1
    self.carro_esperando = False

  def get_carro_esperando(self):
    return self.carro_esperando

  def get_qtd_carros(self):
    return self.qtd_carros