# Codigo Do Ricardo

# 1.1 Calculadora Simples
class Calculadora:
    # Método para somar dois números
    def soma(self, a, b):
        return a + b

    # Método para subtrair dois números
    def subtrai(self, a, b):
        return a - b

    # Método para multiplicar dois números
    def multiplica(self, a, b):
        return a * b

    # Método para dividir dois números
    def divide(self, a, b):
        if b == 0:
            return "Divisão por zero!"
        return a / b

# 1.2 Verificador de Palíndromos
def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto = texto.replace(" ", "").lower()
    # Verifica se é igual ao inverso
    return texto == texto[::-1]

# 1.3 Fatorial Recursivo
def fatorial(n):
    # Fatorial não existe para números negativos
    if n < 0:
        return "Número negativo não tem fatorial."
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Chamada recursiva
    return n * fatorial(n - 1)

# 1.4 Conversor de Temperaturas
class ConversorTemperatura:
    # Converte Celsius para Fahrenheit
    def c_para_f(self, c):
        return (c * 9/5) + 32

    # Converte Fahrenheit para Celsius
    def f_para_c(self, f):
        return (f - 32) * 5/9

# 2.1 Maior e Menor Elemento em uma Matriz
def maior_menor_matriz(matriz):
    # Inicializa maior e menor com o primeiro elemento
    maior = menor = matriz[0][0]
    for linha in matriz:
        for valor in linha:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
    return maior, menor

# 2.2 Soma das Diagonais de uma Matriz Quadrada
def soma_diagonais(matriz):
    n = len(matriz)
    # Soma da diagonal principal
    diag_principal = sum(matriz[i][i] for i in range(n))
    # Soma da diagonal secundária
    diag_secundaria = sum(matriz[i][n-1-i] for i in range(n))
    return diag_principal, diag_secundaria

# 3.1 Manipulando Dados de um Objeto
class Numero:
    def __init__(self, valor):
        self.valor = valor

    # Imprime o valor do atributo
    def imprime(self):
        print(f"Valor: {self.valor}")

# 3.2 Trocando Valores entre Objetos
class ValorContainer:
    def __init__(self, valor):
        self.valor = valor

# Função para trocar os valores entre dois objetos
def trocar_valores(refA, refB):
    refA.valor, refB.valor = refB.valor, refA.valor

# 4.1 Sistema de Gerenciamento de Funcionários
class Funcionario:
    def __init__(self, nome, id, salario, departamento):
        self.nome = nome
        self.id = id
        self.salario = salario
        self.departamento = departamento

    # Representação em string do funcionário
    def __str__(self):
        return f"{self.nome} | ID: {self.id} | Salário: {self.salario} | Dept: {self.departamento}"

# 4.2 Agenda de Contatos
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    # Representação em string do contato
    def __str__(self):
        return f"{self.nome} | Tel: {self.telefone} | Email: {self.email}"

# Programa principal (menu simples para testar as funcionalidades)
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Calculadora Simples")
        print("2 - Verificador de Palíndromos")
        print("3 - Fatorial Recursivo")
        print("4 - Conversor de Temperaturas")
        print("5 - Maior/Menor em Matriz")
        print("6 - Soma das Diagonais de Matriz Quadrada")
        print("7 - Manipulação de Objeto Numero")
        print("8 - Troca de Valores entre Objetos")
        print("9 - Gerenciamento de Funcionários")
        print("10 - Agenda de Contatos")
        print("0 - Sair")
        op = input("Opção: ")

        if op == "1":
            calc = Calculadora()
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Operações: 1-Soma 2-Subtração 3-Multiplicação 4-Divisão")
            escolha = input("Escolha a operação: ")
            if escolha == "1":
                print("Resultado:", calc.soma(a, b))
            elif escolha == "2":
                print("Resultado:", calc.subtrai(a, b))
            elif escolha == "3":
                print("Resultado:", calc.multiplica(a, b))
            elif escolha == "4":
                print("Resultado:", calc.divide(a, b))
            else:
                print("Opção inválida.")

        elif op == "2":
            palavra = input("Digite uma palavra ou frase: ")
            if eh_palindromo(palavra):
                print("É palíndromo!")
            else:
                print("Não é palíndromo.")

        elif op == "3":
            n = int(input("Digite um número inteiro não negativo: "))
            print("Fatorial:", fatorial(n))

        elif op == "4":
            conv = ConversorTemperatura()
            print("1 - Celsius para Fahrenheit")
            print("2 - Fahrenheit para Celsius")
            escolha = input("Escolha a conversão: ")
            if escolha == "1":
                c = float(input("Celsius: "))
                print("Fahrenheit:", conv.c_para_f(c))
            elif escolha == "2":
                f = float(input("Fahrenheit: "))
                print("Celsius:", conv.f_para_c(f))
            else:
                print("Opção inválida.")

        elif op == "5":
            m = int(input("Linhas da matriz: "))
            n = int(input("Colunas da matriz: "))
            matriz = []
            for i in range(m):
                linha = list(map(int, input(f"Digite {n} inteiros para a linha {i+1}: ").split()))
                matriz.append(linha)
            maior, menor = maior_menor_matriz(matriz)
            print(f"Maior: {maior}, Menor: {menor}")

        elif op == "6":
            n = int(input("Ordem da matriz quadrada: "))
            matriz = []
            for i in range(n):
                linha = list(map(int, input(f"Digite {n} inteiros para a linha {i+1}: ").split()))
                matriz.append(linha)
            diag1, diag2 = soma_diagonais(matriz)
            print(f"Soma diagonal principal: {diag1}")
            print(f"Soma diagonal secundária: {diag2}")

        elif op == "7":
            valor = int(input("Digite um valor inteiro: "))
            num = Numero(valor)
            num.imprime()
            print(f"Endereço simulado: {id(num)}")

        elif op == "8":
            a = int(input("Valor para objA: "))
            b = int(input("Valor para objB: "))
            objA = ValorContainer(a)
            objB = ValorContainer(b)
            print(f"Antes: objA={objA.valor}, objB={objB.valor}")
            trocar_valores(objA, objB)
            print(f"Depois: objA={objA.valor}, objB={objB.valor}")

        elif op == "9":
            funcionarios = []
            while True:
                print("1 - Cadastrar funcionário")
                print("2 - Total de salários por departamento")
                print("3 - Listar funcionários")
                print("0 - Voltar")
                subop = input("Opção: ")
                if subop == "1":
                    nome = input("Nome: ")
                    idf = int(input("ID: "))
                    salario = float(input("Salário: "))
                    dept = input("Departamento: ")
                    funcionarios.append(Funcionario(nome, idf, salario, dept))
                elif subop == "2":
                    dept = input("Departamento: ")
                    total = sum(f.salario for f in funcionarios if f.departamento == dept)
                    print(f"Total de salários do departamento {dept}: {total}")
                elif subop == "3":
                    for f in funcionarios:
                        print(f)
                elif subop == "0":
                    break

        elif op == "10":
            contatos = []
            while True:
                print("1 - Adicionar contato")
                print("2 - Listar contatos")
                print("3 - Procurar contato por nome")
                print("0 - Voltar")
                subop = input("Opção: ")
                if subop == "1":
                    if len(contatos) >= 10:
                        print("Agenda cheia!")
                        continue
                    nome = input("Nome: ")
                    tel = input("Telefone: ")
                    email = input("Email: ")
                    contatos.append(Contato(nome, tel, email))
                elif subop == "2":
                    for c in contatos:
                        print(c)
                elif subop == "3":
                    nome = input("Nome do contato: ")
                    achou = False
                    for c in contatos:
                        if c.nome.lower() == nome.lower():
                            print(f"Telefone: {c.telefone}, Email: {c.email}")
                            achou = True
                    if not achou:
                        print("Contato não encontrado.")
                elif subop == "0":
                    break

        elif op == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()