import dns.resolver
import sys 

try:
	dominio = sys.argv[1]
	nome_arquivo = sys.argv[2]
except:
	print("Argumentos invalidos")
	print("Usage: dns_brute.py <dominio> <wordlist>")
	sys.exit(1)

try:
	arquivo = open(nome_arquivo)
	subdominios = arquivo.read().splitlines()
except:
	print ("Falha na leitura do arquivo")
	sys.exit()


for subdominio in subdominios:
	try:
		domesub = subdominio + "." + dominio
		resultados = dns.resolver.resolve(domesub, 'a')
		for resultado in resultados:
			print (domesub, resultado)

	except:
		print ("Não encontrado nenhum subdominio")
		pass

