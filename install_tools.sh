#!/bin/bash

# Atualizar Termux
pkg update -y
pkg upgrade -y

# Instalar ferramentas de pentest
pkg install -y nmap
pkg install -y unstable-repo
pkg install -y metasploit
pkg install -y hydra
pkg install -y sqlmap
pkg install -y nikto
pkg install -y john
pkg install -y netcat
pkg install -y dirb
pkg install -y wpscan
pkg install -y tsu

# Dependências
pkg install -y python

# Clonar e instalar Persux2 do GitHub
echo "Clonando e instalando Persux2..."
pkg install -y git
git clone https://github.com/Rfpds/Persux2
cd Persux2`
python Persux2.py

# Desenvolvido por Rfstudio

echo "Todas as ferramentas foram instaladas com sucesso."
