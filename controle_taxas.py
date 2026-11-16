# Importa datetime e date, que permitem trabalhar com datas.
# datetime.strptime() transforma um texto em uma data.
# date.today() retorna a data atual.
from datetime import datetime, date


# Cria uma lista vazia chamada taxas.
# Nela serão armazenadas todas as taxas cadastradas.
taxas = []


# Define a função responsável por cadastrar uma nova taxa.
def cadastrar_taxa():

    # Solicita ao usuário o nome da taxa e guarda o texto digitado.
    nome = input("Nome da taxa: ")

    # Solicita a data de vencimento no formato dia/mês/ano.
    vencimento = input("Data de vencimento (DD/MM/AAAA): ")

    # Converte o texto digitado em uma data de verdade.
    # %d representa o dia, %m representa o mês e %Y representa o ano.
    # .date() mantém somente a parte da data, sem o horário.
    data = datetime.strptime(vencimento, "%d/%m/%Y").date()

    # Cria uma lista com três informações sobre a taxa:
    # posição 0: nome da taxa;
    # posição 1: data de vencimento;
    # posição 2: situação do pagamento (False = ainda não paga).
    taxa = [nome, data, False]

    # Adiciona a lista da nova taxa à lista principal taxas.
    taxas.append(taxa)

    # Informa ao usuário que o cadastro foi realizado.
    print("Taxa cadastrada com sucesso!")


# Define a função que verifica a situação dos vencimentos.
def verificar_vencimentos():

    # Obtém a data atual do computador.
    hoje = date.today()

    # Percorre cada taxa cadastrada na lista taxas.
    # A variável taxa representa uma taxa por vez.
    for taxa in taxas:

        # Obtém o nome da taxa, que está na posição 0.
        nome = taxa[0]

        # Obtém a data de vencimento, que está na posição 1.
        vencimento = taxa[1]

        # Obtém a situação do pagamento, que está na posição 2.
        # True significa paga; False significa não paga.
        paga = taxa[2]

        # Calcula a diferença entre o vencimento e a data atual.
        # .days retorna essa diferença em quantidade de dias.
        # O resultado pode ser positivo, zero ou negativo.
        dias = (vencimento - hoje).days

        # Verifica primeiro se a taxa já foi paga.
        if paga == True:

            # Exibe uma mensagem informando que a taxa foi paga.
            print(nome, "- Taxa já paga")

        # Verifica se a data de vencimento já passou.
        # Um número negativo significa que a taxa está vencida.
        elif dias < 0:

            # Exibe um alerta de vencimento.
            print(nome, "- Taxa vencida!")

        # Verifica se o vencimento é exatamente hoje.
        elif dias == 0:

            # Informa que a taxa vence na data atual.
            print(nome, "- Vence hoje!")

        # Verifica se faltam até 7 dias para o vencimento.
        # Essa condição também inclui o dia do vencimento,
        # mas dias == 0 já foi verificado anteriormente.
        elif dias <= 7:

            # Exibe quantos dias faltam para o vencimento.
            print(nome, "- Vence em", dias, "dias")

        # Executa quando nenhuma das condições anteriores é verdadeira.
        # Nesse caso, faltam mais de 7 dias para o vencimento.
        else:

            # Informa que a taxa ainda não está próxima de vencer.
            print(nome, "- Ainda não está próxima do vencimento")


# Define a função que registra o pagamento de uma taxa.
def marcar_como_paga():

    # Solicita ao usuário o nome da taxa cujo pagamento será registrado.
    nome = input("Nome da taxa paga: ")

    # Percorre todas as taxas cadastradas para procurar o nome informado.
    for taxa in taxas:

        # Compara o nome digitado com o nome da taxa atual.
        if taxa[0] == nome:

            # Altera a posição 2 para True, indicando que foi paga.
            taxa[2] = True

            # Confirma que o pagamento foi registrado.
            print("Pagamento registrado!")

            # Encerra a função imediatamente após encontrar a taxa.
            return

    # Se o laço terminar sem encontrar o nome, exibe esta mensagem.
    print("Taxa não encontrada.")


# Cria um laço infinito, que mantém o menu funcionando.
# Ele só será encerrado quando o comando break for executado.
while True:

    # Exibe o título do menu.
    # \n cria uma quebra de linha antes do título.
    print("\n--- CONTROLE DE TAXAS ---")

    # Exibe a opção para cadastrar uma taxa.
    print("1 - Cadastrar taxa")

    # Exibe a opção para verificar os vencimentos.
    print("2 - Verificar vencimentos")

    # Exibe a opção para registrar o pagamento de uma taxa.
    print("3 - Marcar taxa como paga")

    # Exibe a opção para sair do programa.
    print("0 - Sair")

    # Solicita ao usuário uma opção e guarda o resultado como texto.
    opcao = input("Escolha uma opção: ")

    # Verifica se o usuário escolheu a opção 1.
    if opcao == "1":

        # Chama a função que cadastra uma taxa.
        cadastrar_taxa()

    # Se não escolheu 1, verifica se escolheu a opção 2.
    elif opcao == "2":

        # Chama a função que verifica os vencimentos.
        verificar_vencimentos()

    # Se não escolheu 1 ou 2, verifica se escolheu a opção 3.
    elif opcao == "3":

        # Chama a função que marca uma taxa como paga.
        marcar_como_paga()

    # Verifica se o usuário escolheu a opção 0.
    elif opcao == "0":

        # Informa que o programa será encerrado.
        print("Programa encerrado!")

        # Interrompe o while True e finaliza o laço do menu.
        break

    # Executa se o usuário digitar uma opção diferente das disponíveis.
    else:

        # Informa que a opção digitada não é válida.
        print("Opção inválida!")