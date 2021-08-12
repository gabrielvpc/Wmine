import wget
import os

num = 1
os.system("mkdir arquivos_baixados")
def limpar():
	print('\x1bc')
def baixar():
	print("\nInsira o link do download!")
	url = input(str("> "))
	arquivo = wget.download(url)
	os.system("mv *.jar arquivos_baixados/")
	print("\nArquivo baixado com sucesso!")
limpar()
while (num == 1):
	baixar()

