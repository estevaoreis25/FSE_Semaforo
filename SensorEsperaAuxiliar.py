from gpiozero import Button

class SensorEsperaAuxiliar:
  def __init__(self, sensor_espera):
    self.sensor_espera = Button(sensor_espera)
    self.sensor_espera.when_pressed = self.set_carro_esperando
    self.sensor_espera.when_released = self.conta_infracao
    self.carro_esperando = False
    self.qtd_carros = 0
    self.qtd_carros_sinal_vermelho = 0
    self.infracao_sinal_vermeho = 0

  def set_carro_esperando(self):
    self.qtd_carros+=1
    self.carro_esperando = True

  def conta_infracao(self):
    self.qtd_carros_sinal_vermelho+=1

  def set_carro_passando(self):
    self.carro_esperando = False

  def get_carro_esperando(self):
    return self.carro_esperando

  def get_qtd_carros(self):
    return self.qtd_carros

  def reinicia_contagem_carros(self):
    self.qtd_carros_sinal_vermelho = 0

  def get_infracoes_sinal_vermelho(self):
    self.infracao_sinal_vermeho += self.qtd_carros_sinal_vermelho
    return self.infracao_sinal_vermeho