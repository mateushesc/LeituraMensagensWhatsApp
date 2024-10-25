import pandas as pd
import re
import matplotlib.pyplot as plt

# Função para processar cada linha do arquivo de exportação
def process_message(line):
    pattern = r'(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+): (.+)'  # Padrão regex para data, hora, remetente e mensagem
    match = re.match(pattern, line)
    if match:
        date, time, sender, message = match.groups()
        return date, time, sender, message
    else:
        return None

# Função para ler e processar o arquivo de conversas
def read_conversation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    messages = []
    current_message = None
    
    for line in lines:
        processed = process_message(line)
        if processed:
            if current_message:
                messages.append(current_message)
            current_message = processed
        else:
            if current_message:
                current_message = (current_message[0], current_message[1], current_message[2], current_message[3] + " " + line.strip())
    
    if current_message:
        messages.append(current_message)
    
    return messages

# Função para mostrar o resumo das conversas
def show_summary():
    summary = df['nome do remetente'].value_counts().reset_index()
    summary.columns = ['Remetente', 'Total de Mensagens']
    print("\nResumo das Conversas:")
    print(summary[['Remetente', 'Total de Mensagens']])

# Função para exibir o gráfico de pizza de distribuição de mensagens por remetente
def plot_pie_chart():
    df['nome do remetente'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
    plt.title('Distribuição de mensagens por remetente')
    plt.ylabel('')
    plt.show()

# Função para exibir o histograma do histórico de mensagens
def plot_histogram(remetente):
    historico = filter_by_sender(remetente)
    if historico.empty:
        print(f"Nenhuma mensagem encontrada para o remetente: {remetente}")
        return
    
    historico['data'] = pd.to_datetime(historico['data'], dayfirst=True)
    data_count = historico.groupby(historico['data'].dt.date).size()
    
    data_count.plot(kind='bar', figsize=(10, 5), color='skyblue')
    plt.title(f'Histórico de mensagens de {remetente}')
    plt.ylabel('Número de mensagens')
    plt.xlabel('Data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Função para filtrar mensagens por remetente
def filter_by_sender(remetente):
    return df[df['nome do remetente'] == remetente]

# Função para mostrar o histórico de mensagens de um remetente
def show_message_history(remetente, save_to_file=False):
    historico = filter_by_sender(remetente)
    if historico.empty:
        print(f"Nenhuma mensagem encontrada para o remetente: {remetente}")
        return

    if save_to_file:
        file_name = f"historico_{remetente}.txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            for index, row in historico.iterrows():
                f.write(f"{row['data']} {row['hora']} - {row['mensagem']}\n")
        print(f"Histórico salvo no arquivo: {file_name}")
    else:
        for index, row in historico.iterrows():
            print(f"{row['data']} {row['hora']} - {row['mensagem']}")

# Função para permitir a escolha de um remetente da lista
def choose_sender():
    unique_senders = df['nome do remetente'].unique()
    print("\nEscolha um remetente:")
    for idx, sender in enumerate(unique_senders):
        print(f"{idx + 1}. {sender}")
    choice = int(input("Digite o número do remetente: ")) - 1
    if 0 <= choice < len(unique_senders):
        return unique_senders[choice]
    else:
        print("Escolha inválida.")
        return None

# Função para interação com o usuário no terminal
def terminal_interaction():
    while True:
        print("\nOpções disponíveis:")
        print("1. Resumo das conversas")
        print("2. Gráfico de pizza de distribuição de mensagens por remetente")
        print("3. Gráfico do histórico de mensagens de um remetente")
        print("4. Histórico de mensagens de um remetente")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            show_summary()
        
        elif choice == '2':
            plot_pie_chart()
        
        elif choice == '3':
            remetente = choose_sender()
            if remetente:
                plot_histogram(remetente)
        
        elif choice == '4':
            remetente = choose_sender()
            if remetente:
                save_option = input("Deseja salvar o histórico em um arquivo .txt? (s/n): ").lower()
                show_message_history(remetente, save_to_file=(save_option == 's'))
        
        elif choice == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Carregar o arquivo de conversas e criar o DataFrame
file_path = 'Conversa do WhatsApp com [Censura] wins!.txt'
data = read_conversation(file_path)
df = pd.DataFrame(data, columns=['data', 'hora', 'nome do remetente', 'mensagem'])

# Iniciar a interação no terminal
terminal_interaction()
