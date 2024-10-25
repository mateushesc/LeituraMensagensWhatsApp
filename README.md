#**Análise de Conversas do WhatsApp**


Este projeto é um script em Python para análise de conversas exportadas do WhatsApp, que permite exibir e salvar informações como histórico de mensagens, resumo de conversas e gráficos de análise. O script permite interagir com as conversas através do terminal, com funcionalidades para exibir gráficos e salvar históricos de um remetente específico.


##**Funcionalidades**


Resumo das Conversas: Exibe uma lista de remetentes e a quantidade total de mensagens enviadas por cada um.

Gráfico de Pizza: Mostra a distribuição percentual das mensagens de cada remetente.

Histograma do Histórico de Remetente: Exibe a quantidade de mensagens enviadas diariamente por um remetente específico.

Histórico de Mensagens do Remetente: Permite visualizar e salvar o histórico de mensagens de um remetente específico em um arquivo .txt.


##**Requisitos**


Python 3.x

Pandas para manipulação de dados

Matplotlib para visualização dos gráficos


##**Instale as dependências com o comando:**


pip install pandas matplotlib


##**Estrutura do Código**


process_message: Extrai a data, hora, remetente e mensagem de cada linha do arquivo de conversa.

read_conversation: Lê o arquivo de exportação do WhatsApp e processa as mensagens.

show_summary: Exibe o resumo das conversas.

plot_pie_chart: Gera um gráfico de pizza com a distribuição de mensagens por remetente.

plot_histogram: Exibe o histórico de mensagens em forma de histograma para um remetente específico.

show_message_history: Mostra o histórico de mensagens de um remetente e permite salvar em .txt.

choose_sender: Permite selecionar um remetente da lista de remetentes únicos.

terminal_interaction: Interface de interação no terminal, permitindo escolher entre as funcionalidades.


##**Como Usar**


**Exportar Conversa do WhatsApp:** Para usar o código, exporte a conversa de um grupo ou contato do WhatsApp e salve-a como .txt.

**Configurar Caminho do Arquivo:** No código, configure o caminho do arquivo na linha: file_path = 'Conversa do WhatsApp com [Nome].txt'

**Executar o Script:** Execute o script com: python app.py

**Interação no Terminal:** Escolha as opções exibidas no terminal para ver o resumo, gráficos ou histórico. Para exibir o histórico de um remetente específico, selecione-o na lista de remetentes.


##**Observações**


O arquivo exportado deve estar no formato de texto do WhatsApp, incluindo a data, hora e remetente no formato dd/mm/aaaa hh:mm - Nome do Remetente: Mensagem.
Certifique-se de que o arquivo .txt segue essa estrutura para que o script consiga ler as mensagens corretamente.


##**Licença**

Este projeto é livre para uso e modificação, conforme os termos da licença MIT.


##**Agradecimentos**

Este projeto foi desenvolvido com a assistência do ChatGPT, que ajudou a implementar e refinar as funcionalidades do script e a construir esta documentação.
