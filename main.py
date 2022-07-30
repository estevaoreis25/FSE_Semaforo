from time import sleep
from Cruzamento import Cruzamento
import signal
import sys

if __name__ == "__main__":

  cruzamento1 = Cruzamento(
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
                  sensor_v1_a = 27, 
                  sensor_v1_b = 22,
                  sensor_v2_a = 13, 
                  sensor_v2_b = 19)
  
  def finaliza_programa(sig, frama):
    print("Até mais ...")
    cruzamento1.smf_principal.desliga_semaforo()
    cruzamento1.smf_auxiliar.desliga_semaforo()
    sleep(2)
    sys.exit(0)


  signal.signal(signal.SIGINT, finaliza_programa)
  signal.signal(signal.SIGTERM, finaliza_programa)
  contador_segundos = 0

  while(True):
    #cruzamento1.controla_semaforos()
    cruzamento2.controla_semaforos()
    sleep(1)
    contador_segundos+=1
    print(f'Qtd carros →: {(cruzamento2.sensor_v1.get_quantidade_carros()/contador_segundos)*60}')