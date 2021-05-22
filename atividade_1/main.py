# script para contagem de palavras em texto

# input() é uma built-in function
# pede identificação do arquivo a ser processado
nomeArq = input('Entre o nome do arquivo: ')
palavraUsuario = input('Entre a palavra a ser encontrada: ')

# abre o arquivo para leitura
arqAberto = open(nomeArq, 'r')

# criar dicionário para processamento
contagem = dict()

# percorrer as linhas do arqAberto
for linha in arqAberto:
  # separar as palavras da linha pelo espaço
  palavras = linha.split()
  # percorrer a lista de palavras para calcular quantidades de ocorrências
  for palavra in palavras:
    #contagem[palavra] = contagem.get(palavra, 0) + 1
    contagem[palavra] = contagem.get(palavra, 0) + 1

# criar variáveis de controle para rankear palavras
maiorQtde = None
palavraMaiorQtde = None
encontrada = None
qtdeEncontrada = None

# percorrer o dicionário, item por item
for chave, valor in list(contagem.items()):
  # testar quantidade de ocorrências da chave e trocar se maior
  if maiorQtde is None or valor > maiorQtde:
    maiorQtde = valor
    palavraMaiorQtde = chave

  if chave == palavraUsuario:
    encontrada = chave
    qtdeEncontrada = valor
    
# mostrar resultado
print('RESULTADOS:')
print(palavraMaiorQtde, maiorQtde)
print('*******')
print(encontrada, qtdeEncontrada)
