from time import sleep
from Cruzamento import Cruzamento
if __name__ == "__main__":

  cruzamento1 = Cruzamento(
                    verm1=12, 
                    amar1=16, 
                    verd1=20, 
                    verm2=21, 
                    amar2=26, 
                    verd2=1,
                    botao1=8,
                    botao2=7)

  cruzamento2 = Cruzamento(
                  verm1=6, 
                  amar1=5, 
                  verd1=0,
                  verm2=11, 
                  amar2=3, 
                  verd2=2,
                  botao1=10,
                  botao2=9)

  while(True):
    cruzamento1.controla_semaforos()
    #cruzamento2.controla_semaforos()
    sleep(1)
  