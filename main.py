# AGENDA TELEFÔNICA - AlgProg
lista_contatos = []


def add_contact():
    print("\n--- CADASTRO DE CONTATO ---")
    
    nome = input("Nome: ").strip()
    while not nome:
        nome = input("O nome não pode ser vazio. Nome: ").strip()

    # Validação da Data de Nascimento (Formato e Tamanho)
    dn = input("Data de Nascimento (DD/MM/AAAA): ").strip()
    while len(dn) != 10 or dn[2] != '/' or dn[5] != '/':
        print("Formato inválido! Use DD/MM/AAAA.")
        dn = input("Data de Nascimento: ").strip()

    # Verificar Duplicados (Nome + DN)
    for contato in lista_contatos:
        if contato["nome"].lower() == nome.lower() and contato["nascimento"] == dn:
            print(f"Erro: {nome} nascido em {dn} já está cadastrado.")
            return

    # Validação de Telefone e E-mail (Não vazios)
    telefone = input("Telefone: ").strip()
    while not telefone:
        telefone = input("Telefone é obrigatório: ").strip()

    email = input("E-mail: ").strip()
    while not email:
        email = input("E-mail é obrigatório: ").strip()

    sexo = input("Sexo (M/F): ").upper()
    while sexo not in ["M", "F"]:
        sexo = input("Inválido. Digite 'M' ou 'F': ").upper()

    rua = input("Rua: ")
    casa = input("Número da casa: ")
    bairro = input("Bairro: ").strip()

    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "nascimento": dn,
        "sexo": sexo,
        "rua": rua,
        "casa": casa,
        "bairro": bairro
    }
    lista_contatos.append(novo_contato)
    print(f"Contato {nome} cadastrado com sucesso!")

def listar_contatos():
    if not lista_contatos:
        print("\n[Agenda vazia]")
        return

    # ORDENAÇÃO MANUAL (Bubble Sort por Nome)
    # Criamos uma cópia para não alterar a ordem original de cadastro se não quiser
    contatos_ordenados = lista_contatos[:]
    n = len(contatos_ordenados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contatos_ordenados[j]["nome"].lower() > contatos_ordenados[j+1]["nome"].lower():
                contatos_ordenados[j], contatos_ordenados[j+1] = contatos_ordenados[j+1], contatos_ordenados[j]

    print("\n--- LISTA DE CONTATOS (ORDEM ALFABÉTICA) ---")
    for c in contatos_ordenados:
        print(f"Nome: {c['nome']} | Tel: {c['telefone']} | DN: {c['nascimento']} | Bairro: {c['bairro']}")


def calcular_idade(data_nasc):
    # Consideramos o ano atual como 2026
    # Fatiamento da string DD/MM/AAAA
    try:
        ano_nascimento = int(data_nasc[6:])
        return 2026 - ano_nascimento
    except:
        return 0

        
def mostrar_estatisticas():
    if not lista_contatos:
        print("\nSem dados para estatísticas.")
        return

    masc = 0
    fem = 0
    bairros = {}
    meses = [0] * 12
    nomes_meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    mais_velho = lista_contatos[0]
    mais_novo = lista_contatos[0]

    for c in lista_contatos:
        # A: Sexo
        if c["sexo"] == "M": masc += 1
        else: fem += 1

        # B: Bairros
        b = c["bairro"]
        if b in bairros: bairros[b] += 1
        else: bairros[b] = 1

        # C: Meses (DD/MM/AAAA -> MM é índice 3 e 4)
        m_idx = int(c["nascimento"][3:5]) - 1
        if 0 <= m_idx <= 11:
            meses[m_idx] += 1

        # D e E: Idades
        idade_c = calcular_idade(c["nascimento"])
        if idade_c > calcular_idade(mais_velho["nascimento"]): mais_velho = c
        if idade_c < calcular_idade(mais_novo["nascimento"]): mais_novo = c

    print("\n--- ESTATÍSTICAS ---")
    print(f"A: Masculino: {masc} | Feminino: {fem}")
    print("B: Pessoas por bairro:")
    for b, qtd in bairros.items():
        print(f"   - {b}: {qtd}")
    print("C: Aniversariantes por mês:")
    for i in range(12):
        print(f"   - {nomes_meses[i]}: {meses[i]}")
    print(f"D: Mais velho: {mais_velho['nome']} ({calcular_idade(mais_velho['nascimento'])} anos)")
    print(f"E: Idade do mais novo: {calcular_idade(mais_novo['nascimento'])} anos")

def consultar_contato():
    nome_busca = input("Nome para consulta: ").strip().lower()
    encontrado = False
    for c in lista_contatos:
        if c["nome"].lower() == nome_busca:
            print(f"\nDados de {c['nome']}:")
            for chave, valor in c.items():
                print(f"{chave.capitalize()}: {valor}")
            encontrado = True
    if not encontrado:
        print("Contato não encontrado.")

def remover_contato():
    nome_busca = input("Nome para excluir: ").strip().lower()
    indices_para_remover = []
    
    for i, c in enumerate(lista_contatos):
        if c["nome"].lower() == nome_busca:
            indices_para_remover.append(i)

    if not indices_para_remover:
        print("Nenhum contato encontrado.")
    elif len(indices_para_remover) == 1:
        idx = indices_para_remover[0]
        removido = lista_contatos.pop(idx)
        print(f"Contato {removido['nome']} removido!")
    else:
        print("Vários contatos com esse nome encontrados:")
        for idx in indices_para_remover:
            print(f"ID: {idx} | DN: {lista_contatos[idx]['nascimento']}")
        escolha = int(input("Digite o ID exato para remover: "))
        lista_contatos.pop(escolha)
        print("Removido com sucesso!")

def main():
    while True:
        print("\n" + "="*30)
        print("      AGENDA TELEFÔNICA")
        print("="*30)
        print("1 - Cadastrar\n2 - Consultar\n3 - Excluir\n4 - Listar Todos\n5 - Estatística\n6 - Sair")
        
        op = input("Opção: ")
        if op == "1": add_contact()
        elif op == "2": consultar_contato()
        elif op == "3": remover_contato()
        elif op == "4": listar_contatos()
        elif op == "5": mostrar_estatisticas()
        elif op == "6": break
        else: print("Opção inválida.")

if __name__ == "__main__":
    main()
