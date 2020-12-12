import dns.resolver
import sys 

try:
	domain = sys.argv[1]
	nome_arquivo = sys.argv[2]
except:
	print("Invalid arguments")
	print("Usage: dns_brute.py <domain> <wordlist>")
	sys.exit(1)

try:
	arquivo = open(nome_arquivo)
	subdomains = arquivo.read().splitlines()
except:
	print ("Failed to read the file")
	sys.exit()


for subdomain in subdomains:
	try:
		domesub = subdomain + "." + domain
		resultados = dns.resolver.resolve(domesub, 'a')
		for resultado in resultados:
			print (domesub, resultado)

	except:
		print ("No subdomains of: " + subdomain)
		pass

