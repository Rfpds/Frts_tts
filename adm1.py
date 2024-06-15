import os

# Atualizar Termux
os.system("pkg update -y")
os.system("pkg upgrade -y")

# Instalar ferramentas de pentest
packages = [
    "nmap", 
    "metasploit", 
    "hydra", 
    "sqlmap", 
    "nikto", 
    "john", 
    "netcat", 
    "dirb", 
    "wpscan", 
    "tsu"
]

for pkg in packages:
    os.system(f"pkg install -y {pkg}")

# Dependências
os.system("pkg install -y python")
os.system("pkg install -y python2")
os.system("pkg install -y python3")

# Clonar e instalar Pacotes do GitHub
print("Clonando e instalando Persux2...")
os.system("pkg install -y git")
os.system("git clone https://github.com/Rfpds/Persux2")
os.chdir("Persux2")
os.system("python Persux2.py")

print("Clonando e instalando Sml...")
os.system("git clone https://github.com/Rfpds/Sml")
os.chdir("Sml")
os.system("python Sml.py")


print("Todas as ferramentas foram instaladas com sucesso.")
