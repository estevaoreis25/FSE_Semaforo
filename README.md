# FSE_Semaforo
Primeiro trabalho de Fundamentos de Sistemas Embarcados 2022.1
 
## Como executar
Para executar, clone todo o repositório para uma das Raspberry
 
na raiz do projeto execute o seguinte comando
 
     $ python3 main.py

Para ativar o modo NOTURNO digite a qualquer momento a tecla `N`

Para ativar o modo EMERGENCIA digite a qualquer momento a tecla `E`

Para desaativar o modo NOTURNO ou EMERGENCIA digite a qualquer momento a tecla `X`

Para finalizar o programa digite as teclas `CTRL+C`
 
## Sobre a aplicação
O arquivo `main.py` é responsável por instanciar os dois cruzamentos da Raspberry conectando todos os pinos necessários com o software.

Cada cruzamento será executada por uma thread.
 
Quando o programa estiver em execução será possível visualizar na placa os leds funcionando adequadamente como o um semáforo.
 
É possível diminuir o tempo de um estado dos semáforos utilizando os botões de pedestre e o sensor hall para os carros parados nas vias auxiliares.
 
A todo momento é possível observar em cada cruzamento as informações `FLUXO DE TRANSITO`, `VELOCIDADE MEDIA DA VIA` e `INFRACOES`.

Nos momentos em que os sensores de velocidada forem acionados, será mostrado na tela a velocidade do carro e a velocidade média dos carros que passaram por aquela via.
