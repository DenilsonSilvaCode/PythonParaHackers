
# escrevendo no arquivo
arq = open('arquivo.txt', 'w')
arq.write('Python para Hackers')
arq.close()


#lendo o arquivo
arq = open('arquivo.txt', 'r')
texto = arq.read()
arq.close()

print(texto)