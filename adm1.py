import os

def update_termux():
    print("Atualizando Termux...")
    os.system("pkg update -y")
    os.system("pkg upgrade -y")

def install_packages(packages):
    for pkg in packages:
        print(f"Instalando {pkg}...")
        os.system(f"pkg install -y {pkg}")

def clone_and_install_git_repos(repos):
    for repo in repos:
        print(f"Clonando e instalando {repo}...")
        os.system("pkg install -y git")
        os.system(f"git clone {repo}")
        repo_name = repo.split("/")[-1].split(".git")[0]
        os.chdir(repo_name)
        if os.path.exists("install.py"):
            os.system("python install.py")
        elif os.path.exists("setup.py"):
            os.system("python setup.py install")
        elif os.path.exists("requirements.txt"):
            os.system("pip install -r requirements.txt")
        os.chdir("..")

if __name__ == "__main__":
    # Defina suas listas de ferramentas Git e pacotes APT aqui
    git_repos = [
        "https://github.com/user/repo1.git",
        "https://github.com/user/repo2.git"
    ]

    apt_packages = [
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

    update_termux()
    install_packages(apt_packages)
    clone_and_install_git_repos(git_repos)

    print("Todas as ferramentas foram instaladas com sucesso.")
