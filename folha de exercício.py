"""
Questão 01
"""

# Forma 01

nome = input('Digite o seu nome: ')
idade = input('Quantos anos você tem? ')
if int(idade) < 18:
      print(f'{nome}, você é menor de idade. Não pode consumir bebidas alcólicas!')
else:
      print('Bora beber que essa vida de só pagar boleto está F@$%#!!')


# Forma 02

import datetime
nome = input('Digite o seu nome: ')
ano = int(input('Em que ano você nasceu? '))
idade = datetime.datetime.now().year - ano
if idade < 18:
      print(f'{nome}, você é menor de idade. Não pode consumir bebidas alcólicas!')
else:
      print('Bora beber que essa vida de só pagar boleto está F@$%#!!')

# Forma 03

nome = input('Digite o seu nome: ')
print( f"{nome}, você é menor de idade. Não pode consumir bebidas alcólicas!"
      if (idade := int(input('Digite a sua idade: ')) < 18)
      else f"Bora beber que essa vida de só pagar boleto está F@$%#!!")


"""
Questão 02
"""

# Forma 01

notas = []

for a in range(3):
      nota = float(input(f'Digite a sua {a + 1}º Nota: '))
      notas.append(nota)

media = round(sum(notas)/len(notas), 2)

if media > 8:
      print(f'Você está aprovado!')
else:
      print('Vish... vai fazer tudo denovo!')


# Forma 02


notas = []

for a in range(3):
      nota = float(input(f'Digite a sua {a + 1}º Nota: '))
      notas.append(nota)

print(f"Você está aprovado"
      if (round((sum(notas)/len(notas)), 2)) > 8
      else 'Vish... vai fazer tudo denovo!')


# Forma 03


notas = 0
for a in range(3):
      notas += float(input(f'Digite a sua {a + 1}º Nota: '))

print(f"Você está aprovado"
      if (round((notas/3), 2)) > 8
      else 'Vish... vai fazer tudo denovo!')



"""
Questão 03
"""


# Forma 01

alt = float(input('Digite a sua altura [m]: '))

if alt % 2 == 0:
      print('Você tem uma altura de número par.')
else:
      print('Você tem uma altura de número impar.')


# Forma 02

alt = float(input('Digite a sua altura [m]: '))

print("Você tem uma altura de número impar."
      if alt % 2 == 0
      else "Você tem uma altura de número impar.")


# Forma 03

print("Você tem uma altura de número impar."
      if (alt := float(input('Digite a sua altura [m]: '))) % 2 == 0
      else "Você tem uma altura de número impar.")


"""
Questão 04
"""

# Forma 01

import datetime
import math

delta_de_dias = (datetime.datetime.now() - datetime.datetime(2022, 1, 1)).days
print(f'Você está no {math.ceil(delta_de_dias/(365//4))}º trimestre do ano')


# Forma 02

dias = int(input('Informe quantos dias já se passaram neste ano: '))

if dias <= 365 / 4:
      print('Você está no 1º trimestre!')
elif 365 / 4 < dias <= (365 * 2) / 4:
      print('Você está no 2º trimestre!')
elif (2 * 365) / 4 < dias <= (365 * 3) / 4:
      print('Você está no 3º trimestre!')
else:
      print('Você está no 4º trimestre!')


# Forma 03

dias = int(input('Informe quantos dias já se passaram neste ano: '))
comparacao = [365/4, 365/2, (3 / 4) * 365, 365]
for a in range(3):
      if dias < comparacao[a]:
            print(f'Você está no {a + 1}º trimestre!')
            break


"""
Questão 05
"""

# Forma 01

lista = []

for a in range(3):
      lista.append(float(input(f'Digite o {a + 1}º número: ')))

lista.sort(reverse=True)

if lista.count(max(lista)) <= 1:
      print(f'O maior número digitato é: {max(lista)}')
else:
      print(f'Houve empate! Os maiores números digitados são: {lista[:lista.count(max(lista))]}')


# Forma 02

maior = 0
cont = 1
for a in range(3):
      num = float(input(f'Digite o {a + 1}º número, maior do que 0: '))
      if num > maior:
            maior = num
      elif num == maior:
            cont += 1

print(f'O maior número foi {maior} e ele apareceu {cont} veze(s).')

