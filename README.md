# Escola de Cursos

Projeto desenvolvido para a disciplina **Programação de Aplicativos**, com o professor Peterson Macedo.

**Integrantes:** Matheus Hugo, Nicholas Uber, Matheus Andrei e Gabriel Kurtz  
**Repositório:** `poo-grupoX-escola-de-cursos`

## Sobre o projeto

Este é um protótipo em Python que roda no terminal. Ele ajuda a organizar as informações de alunos, professores e coordenadores de uma escola de cursos.

A estrutura foi feita com orientação a objetos, usando encapsulamento, herança e polimorfismo. Cada tipo de pessoa tem seus próprios dados e regras para calcular o valor que recebe ou paga.

## Classes do sistema

| Classe | Arquivo | O que faz |
|---|---|---|
| `Pessoa` | `pessoa.py` | Classe base com nome, idade e e-mail. Os atributos são privados e validados. Também define o método `calcular_valor_mensal()`. |
| `Aluno` | `aluno.py` | Herda de `Pessoa` e guarda curso, mensalidade e notas. Permite registrar notas e calcular a média. Se a média for 9 ou mais, o aluno recebe 10% de desconto na mensalidade. |
| `Professor` | `professor.py` | Herda de `Pessoa` e guarda disciplina e valor por hora. As horas trabalhadas são registradas para calcular o pagamento. |
| `Coordenador` | `coordenador.py` | Herda de `Pessoa` e guarda área e salário-base. Também permite definir a equipe; o salário inclui R$ 150 por professor na equipe. |
| `Escola` | `escola.py` | Mantém a lista de pessoas cadastradas e permite cadastrar, buscar e calcular valores usando o método de cada tipo de pessoa. |

## Validações

Os dados são verificados ao serem definidos: o nome não pode ficar vazio, a idade deve estar entre 0 e 120 anos e o e-mail precisa conter `@`. Mensalidade, valor por hora e salário-base devem ser maiores que zero. As notas devem ficar entre 0 e 10.
