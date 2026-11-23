from aluno import Aluno
from professor import Professor
from coordenador import Coordenador
from escola import Escola
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")

def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um valor numérico válido.")

def cadastrar_pessoa(escola):
    print("\nTipo de cadastro:")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Coordenador")
    tipo = input("Escolha: ").strip()

    nome = input("Nome: ").strip()
    idade = ler_inteiro("Idade: ")

    try:
        if tipo == "1":
            curso = input("Curso: ").strip()
            mensalidade = ler_decimal("Mensalidade (R$): ")
            pessoa = Aluno(nome, idade, curso, mensalidade)
        elif tipo == "2":
            disciplina = input("Disciplina: ").strip()
            horas_aula = ler_decimal("Horas de aula no mês: ")
            valor_hora = ler_decimal("Valor por hora (R$): ")
            pessoa = Professor(nome, idade, disciplina, horas_aula, valor_hora)
        elif tipo == "3":
            area = input("Área de coordenação: ").strip()
            salario_base = ler_decimal("Salário-base (R$): ")
            bonus = ler_decimal("Bônus (R$): ")
            pessoa = Coordenador(nome, idade, area, salario_base, bonus)
        else:
            print("Tipo de cadastro inválido.")
            return

        escola.cadastrar(pessoa)
        print("\nCadastro realizado com sucesso!")
        print(pessoa)
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")

def listar_pessoas(escola):
    print("\n--- Pessoas cadastradas ---")
    escola.listar()


def buscar_pessoa(escola):
    termo = input("Digite o nome que deseja buscar: ").strip()
    resultados = escola.buscar_por_nome(termo)

    if resultados:
        print("\n--- Resultado da busca ---")
        for pessoa in resultados:
            print(pessoa)
    else:
        print("Nenhuma pessoa encontrada.")

def executar_acao(escola):
    print("\n--- Valores mensais (ação polimórfica) ---")
    escola.executar_acao_polimorfica()

def exibir_menu():
    print("\n========== ESCOLA DE CURSOS ==========")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Executar ação polimórfica")
    print("5 - Sair")
    print("======================================")

def main():
    escola = Escola("Escola de Cursos")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa(escola)
        elif opcao == "2":
            listar_pessoas(escola)
        elif opcao == "3":
            buscar_pessoa(escola)
        elif opcao == "4":
            executar_acao(escola)
        elif opcao == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()