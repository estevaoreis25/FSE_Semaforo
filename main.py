from time import sleep
from Cruzamento import Cruzamento
import signal
import sys
from threading import Thread, Event
import os

exit_execution = Event()


if __name__ == "__main__":

  cruzamento1 = Cruzamento(
                    id = 1,
                    verm1=12, 
                    amar1=16, 
                    verd1=20, 
                    verm2=21, 
                    amar2=26, 
                    verd2=1,
                    botao1=8,
                    botao2=7,
                    sensor_pass1 = 14, 
                    sensor_pass2 = 15, 
                    sensor_v1_a = 18, 
                    sensor_v1_b = 23,
                    sensor_v2_a = 24, 
                    sensor_v2_b = 25)

  cruzamento2 = Cruzamento(
                  id = 2,
                  verm1=6, 
                  amar1=5, 
                  verd1=0,
                  verm2=11, 
                  amar2=3, 
                  verd2=2,
                  botao1=10,
                  botao2=9,
                  sensor_pass1 = 4, 
                  sensor_pass2 = 17, 
                  sensor_v1_b = 27, 
                  sensor_v1_a = 22,
                  sensor_v2_b = 13, 
                  sensor_v2_a = 19)


  def executa_cruzamento1():
    while True:
      if exit_execution.is_set():
          cruzamento1.smf_principal.desliga_semaforo()
          cruzamento1.smf_auxiliar.desliga_semaforo()
          break
      cruzamento1.controla_semaforos()
  
  def executa_cruzamento2():
    while True:
      if exit_execution.is_set():
        cruzamento2.smf_principal.desliga_semaforo()
        cruzamento2.smf_auxiliar.desliga_semaforo()
        break
      cruzamento2.controla_semaforos()
  
  def modifica_modo():
    while True:
      if exit_execution.is_set():
          break
      else:
          modo = input('')
          if(modo == 'N'):
            cruzamento1.ativa_noturno()
            cruzamento2.ativa_noturno()
          elif(modo == 'E'):
            cruzamento1.ativa_emergencia()
            cruzamento2.ativa_emergencia()
          elif(modo =='X'):
            cruzamento1.desativa_noturno_emergencia()
            cruzamento2.desativa_noturno_emergencia()
  
  def mostra_info():
    while True:
      if exit_execution.is_set():
        break
      else:
        sleep(2)
        os.system('clear')
        print('Digite N para o modo NOTURNO, E para o o modo EMERGENCIA" e X para desativa-los')
        cruzamento1.mostra_informacoes()
        cruzamento2.mostra_informacoes()

  def finaliza_programa(sig, frama):
    exit_execution.is_set()
    print("Até mais ...")
    sleep(3)
    sys.exit(0)

  tcruz1 = Thread(target=executa_cruzamento1)
  tcruz2 = Thread(target=executa_cruzamento2)
  modos = Thread(target=modifica_modo)
  informacoes = Thread(target=mostra_info)

  tcruz1.daemon = True
  tcruz2.daemon = True
  modos.daemon = True
  informacoes.daemon = True

  signal.signal(signal.SIGINT, finaliza_programa)
  signal.signal(signal.SIGTERM, finaliza_programa)

  tcruz1.start()
  tcruz2.start()
  informacoes.start()
  modos.start()

  tcruz1.join()
  tcruz2.join()
  informacoes.join()
  modos.join()