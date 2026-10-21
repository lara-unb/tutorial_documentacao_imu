# tutorial_documentacao_imu

# Bem vindo ao tutorial de uso da IMU.

### Antes de iniciar, por favor verifique alguns materiais presentes neste repositório dentro das pastas.

Dentro destas pastas você encontrará instaladores e também manuais do fabricante para melhor entendimento. Entretanto não é totalmente necessário a leitura em primeiro momento, somente o download dos instaladores, como descrito abaixo:

# Guia Passo a Passo: Primeira Coleta com as IMUs

Este tutorial explica como instalar o **3-Space Sensor Suite**, conectar os dongles e as IMUs, calibrar os sensores e realizar a primeira coleta de dados.

Os números entre parênteses correspondem às marcações nas imagens de cada etapa.

---

## Passo 1: Instalando o Software

Os instaladores do **3-Space Sensor Suite** estão disponíveis na pasta `executaveis` deste repositório.

1. **Baixe o instalador:** Se o seu sistema operacional for Windows, baixe e execute o [3SpaceSuite.exe](https://github.com/lara-unb/tutorial_documentacao_imu/blob/main/executaveis/3SpaceSuite.exe). Se for macOS, utilize o [3Space_Sensor_Suite-Mac-1.1.5.dmg](https://github.com/lara-unb/tutorial_documentacao_imu/blob/main/executaveis/3Space_Sensor_Suite-Mac-1.1.5.dmg).
2. **Conclua a instalação:** No Windows, clique em **Install (1)** e, ao finalizar, em **Finish (2)**, conforme a imagem abaixo.

![Telas de instalação no Windows, com os botões Install 1 e Finish 2](/tutoriais/primeira_coleta/imagens/instalacao.png)

---

## Passo 2: Conectando os Dongles

Existem dois dongles: o **Wi-Fi**, à esquerda na imagem, e o **Bluetooth**, à direita. Eles são responsáveis pela comunicação sem fio com as IMUs.

1. **Conecte os dongles ao computador:** Utilize cabos USB com conector **Mini USB (1)** na entrada dos dongles.
2. **Confira a conexão:** Ao conectar, o **LED (2)** de cada dongle acende na cor azul.

![Dongles WiFi e Bluetooth, com a entrada Mini USB 1 e os LEDs 2 destacados](/tutoriais/primeira_coleta/imagens/dongles.png)

---

## Passo 3: Ligando a IMU

Existem dois modelos de IMU: o **Mini (modelo novo)**, à esquerda na imagem, e o **Wireless (modelo antigo)**, à direita.

1. **Para ligar a IMU Mini:** Pressione e segure o **botão superior (1)** por 1 a 2 segundos, até que o LED acenda. Para desligar, segure o mesmo botão por cerca de 2 segundos, até que o LED desligue.
1.1. **Para ligar a IMU Wireless:** Primeiro, coloque a alavanca localizada na lateral inferior esquerda do sensor na posição superior. Em seguida, pressione o **botão da direita (3)** por cerca de 2 segundos, até o LED acender. Para desligar, abaixe a alavanca lateral.
2. **Carregue a bateria, se necessário:** Caso a IMU não ligue, conecte-a ao computador com um cabo USB. A IMU Mini possui entrada Micro USB, enquanto a Wireless possui entrada **Mini USB (2)**. O LED do sensor pisca durante o carregamento. Quando a carga estiver completa, o LED para de piscar e permanece verde. Desconecte o cabo e ligue o sensor.

![IMUs Mini e Wireless, com o botão superior da Mini 1, a entrada Mini USB da Wireless 2 e seu botão direito 3](/tutoriais/primeira_coleta/imagens/imus.png)

---

## Passo 4: Conectando o Aplicativo ao Sensor

1. **Abra o aplicativo:** Inicie o **3-Space Sensor Suite**.
2. **Conecte o dongle:** No canto inferior esquerdo, localize **COM Port (1)**, selecione a porta com a descrição **3 Space Dongle** e clique em **Connect**, na mesma área. Após a conexão, o botão passa a mostrar **Disconnect**, como na imagem.
3. **Selecione o sensor:** Na caixa **Sensor Select (2)**, escolha o número indicado na etiqueta da IMU.
4. **Confira a comunicação:** O modelo do sensor deve aparecer na área central da tela e acompanhar os movimentos da IMU.

![Tela principal do aplicativo, com a conexão em COM Port 1, a seleção do sensor 2, Tare 3, Auto Calibrate Gyros 4 e Data Charts 5](/tutoriais/primeira_coleta/imagens/software.png)

---

## Passo 5: Calibrando o Sensor

Utilize os botões destacados na imagem da etapa anterior.

1. **Posicione a IMU:** Coloque o sensor de frente para você, virado para cima, sobre uma superfície plana e reta.
2. **Defina a posição inicial:** Clique em **Tare (3)** para definir essa orientação como referência.
3. **Calibre o giroscópio:** Mantenha o sensor na mesma posição, completamente parado, e clique em **Auto Calibrate Gyros (4)**.

---

## Passo 6: Iniciando a Coleta

1. **Abra os gráficos:** Na tela principal, clique em **Data Charts (5)**, destacado na imagem do Passo 4. Será aberta uma janela com quatro gráficos.
2. **Escolha os dados exibidos:** Por padrão, os gráficos mostram ângulos de Euler, giroscópio corrigido, acelerômetro corrigido e magnetômetro corrigido. Para alterar as informações, utilize as **caixas de seleção no canto superior esquerdo de cada gráfico (1)**.
3. **Abra as opções de gravação:** Clique em **Logging Options (2)**, no canto inferior direito da janela de gráficos.

![Janela Data Charts, com as seleções dos dados 1, Logging Options 2 e Start Logging 6](/tutoriais/primeira_coleta/imagens/graficos_coleta.png)

![Janela Logging Options, com File Pathname na parte superior, Use system timestamp 4 e Save 5](/tutoriais/primeira_coleta/imagens/configuracao_coleta.png)

4. **Defina o arquivo de saída:** Na janela **Logging Options**, utilize o campo **File Pathname** e o botão **...** para escolher a pasta e o nome do arquivo `.txt` em que deseja salvar os dados.
5. **Configure o registro de tempo:** Na seção **Timestamping**, selecione **Use system timestamp (4)**.
6. **Salve as configurações:** Clique em **Save (5)**.

7. **Inicie a gravação:** De volta à janela de gráficos, clique em **Start Logging (6)**, destacado na imagem dos gráficos.
8. **Encerre a gravação:** Quando terminar a coleta, clique em **Stop Logging**, que aparece na mesma posição do botão **Start Logging**.
