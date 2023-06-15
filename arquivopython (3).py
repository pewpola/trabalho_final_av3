def menu():
  print('Bem vindo a matriz dinâmica!')
  while True:
    print('\nEscolha um dos itens abaixo para realizar uma operação desejada por você:')
    print('1 - Cadastrar Matrizes/Vetores')
    print('2 - Multiplicar as matrizes/vetores por um inteiro')
    print('3 - Calcular a transposta de uma matriz/vetor')
    print('4 - Calcular a soma das duas matrizes/vetores cadastradas')
    print('5 - Exibir a diagonal principal e a secundária de A se ela for quadrada')
    print('6 - Exibir a diagonal principal de B e seus elementos acima e abaixo dela, se for quadrada')
    print('7 - Multiplicar as 2 matrizes/vetores cadastradas')
    print('8 - Ordenar as matrizes/vetores')
    print('0 - Para sair')

    opcao = int(input("Digite o item desejado: "))

    if opcao == 0:
       print('\nSaindo...\n')
       break

    if opcao == 1:
     A, B = cadastrar_valores()

     print(f'\nA = {A}')
     print(f'B = {B}\n')
      
    if opcao == 2:
      x = int(input('\nInsira o valor inteiro de x que irá multiplicar todos os elementos da matriz A: '))
      y = int(input('\nInsira o valor inteiro de y que irá multiplicar todos os elementos da matriz B: '))

      Ax, By = multiplicar_por_inteiro(A, B, x, y)
      print(f'\nAx = {Ax}')
      print(f'By = {By}\n')

    if opcao == 3:
      C = calcular_transposta(A)
      D = calcular_transposta(B)

      print(f'\nC = {C}')
      print(f'D = {D}\n')
    
    if opcao == 4:
       matriz_resultante = soma_matrizes(A, B)

       print(f'\nMatriz Resultante da Soma: {matriz_resultante}\n')
    
    if opcao == 5:
       printar_diagonais(A)
    
    if opcao == 6:
       acima_abaixo(B, A)
    
    if opcao == 7:
       multiplicar_matrizes(A, B)
    
    if opcao == 8:
       ordenacao(A, B)
    

def cadastrar_valores():
    A = []

    la = int(input('\nInsira aqui a quantidade de linhas da sua Matriz A: '))
    ca = int(input('Insira aqui a quantidade de colunas da sua Matriz A: '))

    for j in range(la):
        vetor_a = []
        for i in range(ca):
            a = int(input('Insira aqui os valores que vão compor a sua Matriz/Vetor A: '))
            vetor_a.append(a)
        A.append(vetor_a)
    
    B = []

    lb = int(input('\nInsira aqui a quantidade de linhas da sua Matriz B: '))
    cb = int(input('Insira aqui a quantidade de colunas da sua Matriz B: '))

    for j in range(lb):
        vetor_b = []
        for i in range(cb):
            b = int(input('Insira aqui os valores que vão compor a sua Matriz/Vetor B: '))
            vetor_b.append(b)
        B.append(vetor_b)
    
    return A, B

def multiplicar_por_inteiro(A, B, x, y):
    A_multiplicada = []

    for linha in A:
        vetor_multiplicado_a = []
        for numero in linha:
            numero *= x
            vetor_multiplicado_a.append(numero)
        A_multiplicada.append(vetor_multiplicado_a)

    B_multiplicada = []

    for linha in B:
        vetor_multiplicado_b = []
        for numero in linha:
            numero *= y
            vetor_multiplicado_b.append(numero)
        B_multiplicada.append(vetor_multiplicado_b)

    return A_multiplicada, B_multiplicada

def calcular_transposta(M):   
    M_transposta = []

    for j in range(len(M[0])):
        nova_linha = []
        for i in range(len(M)):
            nova_linha.append(M[i][j])
        M_transposta.append(nova_linha)
    
    return M_transposta

def soma_matrizes(A, B):
   if len(A) != len(B) and len(A[0]) != len(B[0]):
      print('\nAs linhas e colunas de A devem ser iguais as linhas e colunas de B!\n')
   
   matriz_resultante = []

   for j in range(len(A)):
      matriz_resultante.append([])
      for i in range(len(A[0])):
         sum = A[j][i] + B[j][i]
         matriz_resultante[j].append(sum)
    
   return matriz_resultante 

def printar_diagonais(A):
   if len(A) == len(A[0]):
       c = len(A)

       for i in range(c):
          print(f'D. Principal: {A[i][i]}')
       
       for i in range(c):
          print(f'D. Secundária: {A[i][c-i-1]}')
          
   else:
      maior = A[0][0]
      posicao = (0, 0)

      for j in range(len(A)):
         for i in range(len(A[0])):
            x = A[j][i]
            if x > maior:
               maior = x
               posicao = (i, j)

      print(f'\nMaior elemento de A: {maior}')
      print(f'Posição do maior elemento de A: {posicao}\n')

def acima_abaixo(B, A):
   if len(B) == len(B[0]):
       
       for i in range(len(B)):
          print(f'D. Principal: {B[i][i]}')
       
       for j in range(len(B)):
          for i in range(len(B[0])):
             if i > j:
                print(f'Acima da D. Principal: {B[j][i]}')
             if j > i:
                print(f'Abaixo da D. Principal: {B[j][i]}')
   else:
      menor = A[0][0]
      posicao = (0, 0)

      for j in range(len(A)):
         for i in range(len(A[0])):
            x = A[j][i]
            if x < menor:
               menor = x
               posicao = (i, j)

      print(f'\nMenor elemento de A: {menor}')
      print(f'Posição do menor elemento de A: {posicao}\n')

def multiplicar_matrizes(A, B):
   Y = []

   if len(A[0]) == len(B):
      for j in range(len(A)):
         vetor = []
         Y.append(vetor)
         for i in range(len(B[0])):
            Y[j].append(0)
      
      for j in range(len(A)):
         for i in range(len(B[0])):
            sum = 0
            for l in range(len(A[0])):
               sum += A[j][l] * B[l][i]
            Y[j][i] = sum

      print(f'\nY = {Y}\n')
   
   else:
      print('\nOrdens de matrizes não permite o produto matricial\n')

def ordenacao(A, B):
   vetor_a = []
   
   for linha in A:
      for numero in linha:
         vetor_a.append(numero)
   
   for j in range(len(vetor_a) - 1):
      for i in range(len(vetor_a) - 1):
         if vetor_a[i] > vetor_a[i+1]:
            aux = vetor_a[i]
            vetor_a[i] = vetor_a[i+1]
            vetor_a[i+1] = aux
   
   A_ordenada = []
   ca = len(A[0])

   for i in range(len(A)):
      la = vetor_a[i*ca:(i+1)*ca]
      A_ordenada.append(la)

   print(f'\nA Ordenada: {A_ordenada}')

   vetor_b = []
   for linha in B:
      for numero in linha:
         vetor_b.append(numero)
   
   for j in range(len(vetor_b) - 1):
      for i in range(len(vetor_b) - 1):
         if vetor_b[i] < vetor_b[i+1]:
            aux = vetor_b[i]
            vetor_b[i] = vetor_b[i+1]
            vetor_b[i+1] = aux
   
   B_ordenada = []
   cb = len(B[0])
   
   for i in range(len(B)):
      lb = vetor_b[i*cb:(i+1)*cb]
      B_ordenada.append(lb)

   print(f'B Ordenada: {B_ordenada}\n')
   
menu()