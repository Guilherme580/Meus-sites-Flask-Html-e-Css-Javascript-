import subprocess
import time

print("muito sexooo")
def open_incognito(url):
    # Caminho comum para o executável do Chrome no Windows.
    # Pode ser diferente no Linux ou Mac.
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    # Adiciona a flag --incognito e a URL como argumentos
    args = [chrome_path, '--incognito', url]

    try:
        # Executa o comando no sistema operacional
        subprocess.Popen(args)
        print(f"Tentando abrir {url} em modo anônimo...")
    except FileNotFoundError:
        print(f"Erro: O Chrome não foi encontrado no caminho especificado: {chrome_path}")
        print("Verifique o caminho ou use um navegador diferente.")

# Exemplo de uso:
open_incognito("https://www.google.com/search?sca_esv=d340eac8d7c27e5b&udm=2&fbs=AIIjpHydJdUtNKrM02hj0s4nbm4yAFb4PvhjIUcDtaFHkK_tyqfYVx0lCBcCX38sg5LqgWMbBDpOpi-b87KRYaAlAzJqMvLYsSu7hLLf25XWG1b4MPTdvzAkT7sGwMYlgjGh85TMgA-P9Q4sr3Kt-vucX4pKWYYPcJDmJY_niZ5DvvnNTObGTWIhYxlEdeRQK3FBbbSG8Du6yi0S9Ua6cFRWxxVRyh1Gkg&q=sexo+roupa+rasgada&sa=X&ved=2ahUKEwj7zZ-89KyRAxV7LrkGHV8lAMIQtKgLegQIGxAB&biw=1358&bih=681&dpr=1")

# Manter o script rodando por um tempo
time.sleep(5)