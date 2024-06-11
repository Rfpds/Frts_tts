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

# Clonar e instalar Tool-X do GitHub
echo "Clonando e instalando Tool-X..."
pkg install -y git
git clone https://github.com/Rajkumrdusad/Tool-X.git
cd Tool-X
chmod +x install.aex
sh install.aex

echo "Todas as ferramentas foram instaladas com sucesso."
