# Escola de Cursos – Sistema Orientado a Objetos
 Escola de cursos
Programação de Aplicativos:Peterson Macedo
Integrantes:**Matheus Hugo, Nicholas Uber, Matheus Andrei , Gabriel Kurtz
Repositório: poo-grupoX-escola-de-cursos

## Descrição
Protótipo em Python, executado no terminal, para controlar alunos, professores e
coordenadores de uma escola de cursos. Aplica **encapsulamento**, **herança** e
**polimorfismo**.

Classes
| Classe | Arquivo | Descrição |
|---|---|---|
| `Pessoa` | `pessoa.py` | Classe base: nome, idade e e-mail (privados, com validação). Método `calcular_valor_mensal()`. |
| `Aluno` | `aluno.py` | Filha de Pessoa. Próprios: `curso`, `mensalidade`, notas, `registrar_nota()`, `calcular_media()`. Paga a mensalidade (10% de desconto se média ≥ 9). |
| `Professor` | `professor.py` | Filha de Pessoa. Próprios: `disciplina`, `valor_hora`, `registrar_horas()`. Recebe horas × valor da hora. |
| `Coordenador` | `coordenador.py` | Filha de Pessoa. Próprios: `area`, `salario_base`, `definir_equipe()`. Recebe salário + R$ 150 por professor da equipe. |
| `Escola` | `escola.py` | Gerenciadora: guarda a lista de pessoas; cadastra, busca e executa o método polimórfico. |

Validações nos setters: nome vazio, idade fora de 0–120, e-mail sem `@`,
mensalidade/valor da hora/salário ≤ 0, nota fora de 0–10.
