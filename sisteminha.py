def criarlista(): # colcar os dados
  print('\n~~~~~~~~~~/////=====\\\\\\\\\\~~~~~~~~~~\nAdicionar ')
  print('Digite:\n Sair: encerrar programa. \n Pesquisar: pesquisar nomes \n Remover: remover nomes')

  while True:
    nome = input('Digite um novo nome: ')
    if (nome.lower() == 'sair'):
      break
    elif (nome.lower() == 'pesquisar'):
      pesquisarlista()
      break
    elif (nome.lower() == 'remover'):
      removerlista()
      break
    else:
      dados.add(nome)

def pesquisarlista():
  print('\n~~~~~~~~~~/////=====\\\\\\\\\\~~~~~~~~~~\nPesquisar')
  print( 'Digite:\n Todos: Ver todos os nomes da lista. \n Sair: encerrar programa.\n Adicionar: adicionar nomes \n Remover: remover nomes')
  while True:
    nome = input('Digite um nome a ser pesquisado: ')
    if (nome.lower() == 'todos'):
      print(dados)
    elif (nome.lower() == 'sair'):
      break
    elif (nome.lower() == 'adicionar'):
      criarlista()
      break
    elif (nome.lower() == 'remover'):
      removerlista()
      break
    elif nome.lower() not in ['adicionar', 'todos', 'sair', 'remover']:
      if nome in dados:
        print('Esse nome foi achado')
      else:
        print('Esse nome nao foi achado:' )

def removerlista():
  print('\n~~~~~~~~~~/////=====\\\\\\\\\\~~~~~~~~~~\nRemover')
  print( 'Digite:\n Todos: Ver todos os nomes da lista. \n Sair: encerrar programa. \n Adicionar: adicionar nomes. \n Pesquisar: pesquisar nomes')
  while True:
    nome = input('Digite um nome a ser removido: ')
    if (nome.lower() == 'pesquisar'):
      pesquisarlista()
      break
    elif (nome.lower() == 'sair'):
      break
    elif (nome.lower() == 'todos'):
      print(dados)
    elif (nome.lower() == 'adicionar'):
      criarlista()
      break
    elif nome.lower() not in ['adicionar', 'todos', 'sair', 'pesquisar']:
      if nome in dados:
        print('nome removido com sucesso!')
        dados.remove(nome)
      else:
        print('nome não encontrado!')


dados = set()
print('~~~~~~~~~~/////== Bem Vindo ==\\\\\\\\\\~~~~~~~~~~')
print('\nDigite:\n Adicionar: adicionar nomes \n Pesquisar: pesquisar nomes \n Remover: remover nomes \n Sair: encerrar programa')
while True:
    opção = input('escolha = ')
    if opção.lower() == 'pesquisar':
        pesquisarlista()
        break
    elif opção.lower() == 'remover':
        removerlista()
        break
    elif opção.lower() == 'adicionar':
        criarlista()
        break
    elif opção.lower() == 'sair':
      break
    else:
        print('insira um valor valido')