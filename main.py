from Cruzamento import Cruzamento
if __name__ == "__main__":

  cruzamento1 = Cruzamento(verm1="BOARD21", 
                    amar1="BOARD26", 
                    verd1="BOARD01",
                    verm2="BOARD12", 
                    amar2="BOARD16", 
                    verd2="BOARD20")

  cruzamento2 = Cruzamento(verm1="BOARD11", 
                  amar1="BOARD03", 
                  verd1="BOARD02",
                  verm2="BOARD06", 
                  amar2="BOARD05", 
                  verd2="BOARD00")

  while(True):
    cruzamento1.controla_semaforos()
    #cruzamento2.controla_semaforos()
  