from gpiozero import Button

class BotaoPedesrtre:
  def __init__(self, botao_pedestre):
    self.botao_pedestre = Button(botao_pedestre)
    self.botao_pedestre.when_pressed = self.set_pedestre_esperando
    self.pedestre_esperando = False

  def set_pedestre_esperando(self):
    self.pedestre_esperando = True

  def set_pedestre_passando(self):
    self.pedestre_esperando = False

  def get_pedestre_esperando(self):
    return self.pedestre_esperando