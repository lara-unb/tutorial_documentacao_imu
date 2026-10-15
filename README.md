# Bem vindo ao tutorial de uso a imu.
### antes de iniciar por favor verifique alguns materiais presentes neste repositório dentro das pastas

dentro destas pastas você encontrará instaladores e também manuais do fabricante para melhor entendimento porem não são totalmente necessarios a leitura somente os instaladores.

# Guia Passo a Passo: Configuração e Uso do 3-Space Sensor Software Suite

O **3-Space Sensor Software Suite** é um programa oficial criado pela Yost Labs para ajudar você a gerenciar, configurar e testar sensores de movimento chamados **IMUs** (dispositivos que medem rotação, aceleração e orientação no espaço). 

Mesmo que você nunca tenha visto ou mexido com programação antes, este guia explica de forma bem simples como preparar o seu computador e usar o programa para enxergar o que o sensor está fazendo.

---

## Passo 1: Preparando o Computador (Instalação das Ferramentas)

Antes de abrir qualquer programa, precisamos garantir que o seu computador tem as ferramentas necessárias para conversar com o sensor.

1. **Baixar o programa do sensor:** Acesse o site oficial da Yost Labs em [yostlabs.com](https://yostlabs.com/yost-labs-3-space-sensor-software-suite/) e baixe o aplicativo tambem está disponivel na pasta instaladores do repositorio **3-Space Suit** para o seu computador disponivel para windows e mac OSx.

2. **Instalar os pacotes necessários:** Com a tela de comandos aberta, instale os complementos que fazem o programa funcionar rodando os comandos de instalação do `pip`:
   ```bash
   pip install matplotlib mediapipe PyQt5 pyserial pyqtgraph pyquaternion scipy
   ```

---

## Passo 2: Conectando os Aparelhos Físicos

1. **O Dongle:** Pegue a pecinha parecida com um pen drive (chamada **Dongle**) e plugue-a em uma entrada USB livre do seu computador. É ela que vai receber os sinais sem fio do sensor.
2. **O Sensor (IMU):** Certifique-se de que a sua caixinha IMU está com a bateria carregada (para carregar, basta deixá-la ligada por um cabo USB no computador). 
3. **Ligar o sensor:** Segure o botão da IMU até que a luzinha (LED) acenda e comece a brilhar.

---

## Passo 3: Descobrindo e Alterando o "ID" do Sensor

Cada sensor possui um número de identificação único chamado **ID** (por exemplo, `9`). Para que o computador saiba com qual sensor ele deve conversar:

1. Abra o programa **3-Space Suit** que você baixou no site da Yost Labs.
2. Conecte o Dongle e selecione nos campos de ID do aplicativo cada número, até que o modelo do programa responda à movimentação da sua IMU.
3. Para alterar o ID no código do seu projeto, modifique a lista `imus` no início do arquivo com o número do seu sensor. Exemplo:
   ```python
   imus = [9]
   ```

---

## Passo 4: Ajustando as Configurações da IMU

Na função de configuração (`configure_imu`), você pode alterar os parâmetros conforme a sua necessidade:

* **disableCompass:** Desabilita ou habilita o magnetômetro (bússola).
* **disableGyro:** Desabilita ou habilita o giroscópio.
* **disableAccelerometer:** Desabilita ou habilita o acelerômetro.
* **gyroAutoCalib:** Calibra o giroscópio automaticamente. Se ativado, deixe o sensor completamente parado ao iniciar o código.
* **tareSensor:** Tara a orientação do sensor usando o *quaternion* atual dele. Se ativado, deixe o sensor virado para cima e na sua direção em uma superfície reta ao iniciar.
* **tareWithQuaternion:** Se a função `tareSensor` não estiver ativada, você pode usar um *quaternion* específico para tarar.
* **filterMode:** Modo de filtro de orientação:
  * `0` - Sem filtro de orientação (frequência de até 1350 Hz)
  * `1` - Filtro de Kalman (padrão, até 250 Hz)
  * `2` e `3` - Filtros Q-COMP e Q-GRAD (até 850 Hz)
* **logical_ids:** Lista com os IDs das IMUs utilizadas (mesmo valor definido no Passo 3).
* **baudrate:** Velocidade da comunicação entre o computador e o Dongle (padrão recomendado: `115200`).
* **Opções de exibição de dados (`show_*`):** Ativam o envio de dados específicos (como quaternions, ângulos de Euler, matriz de rotação, acelerômetro, giroscópio, botão ou magnetômetro) ao iniciar o streaming.

---

## Passo 5: Alterando os Parâmetros do Streaming

* **duration:** Duração do streaming (por padrão, tempo indefinido).
* **delay:** Tempo de atraso em segundos para começar o streaming.
* **frequency:** Frequência de envio das informações (máximo de 1000 Hz, ou `0` para a máxima velocidade possível).

---

## Passo 6: Recebendo e Extraindo os Dados da IMU

O código limpa o buffer de entrada com `serial_port.reset_input_buffer()`. A função `read_data` lê as informações enviadas pelo sensor, enquanto a função `extract_data` recupera dados específicos informando o tipo desejado:

* `0` (0x00) - Quaternion
* `1` (0x01) - Ângulo de Euler
* `2` (0x02) - Matriz de rotação
* `38` (0x26) - Giroscópio
* `39` (0x27) - Acelerômetro
* `40` (0x28) - Magnetômetro
* `250` (0xfa) - Estado do botão

Lembre-se de que o tipo de dado precisa estar ativado nas configurações do Passo 4 para poder ser extraído.

---

## Passo 7: Executando o Código (e Fazendo a Calibração)

1. **Atenção especial se usar Linux:** Antes de executar o código no Linux, libere o acesso à porta USB rodando o comando:
   ```bash
   sudo chmod 666 /dev/ttyACM0
   ```
2. **Posição de calibração:** Quando o código estiver em execução, antes de apertar `Enter` para iniciar, deixe a IMU virada para cima e em sua direção sobre uma superfície plana e reta para garantir a calibração e a tara corretas.
