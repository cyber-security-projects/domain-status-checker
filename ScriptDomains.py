#Script para verificar a atividade de dominios (Se estao ativos ou nao)

import csv
from termcolor import colored
import time
import requests
import webbrowser
from pynput import keyboard
import sys
import termios


def on_press(key):
    global stop_flag
    try:
        if key.char == '+':
            print(colored("Você pressionou '+'.",'red'))
            stop_flag = True
    except AttributeError:
        if key == keyboard.Key.enter:
            if progress['count'] == 0:
                print(colored("Nenhum dominio foi verificado.",'red'))
            else:
                print(colored(f"Você pressionou Enter! {(progress['count'] - 1) / progress['total'] * 100:.2f}% dos dominios ja foram verificados!", 'blue'))

    


# Função para verificar os domínios
def check_domains(domains, active_domains, possible_active):
    official_site = "http://example.com"  # Site oficial para comparação

    for domain in domains:
        if stop_flag:  
            print(colored("Encerrando a verificação de domínios...", 'red'))
            break  
     
        progress['count'] += 1

        try:
            # Faz a requisição HTTP
            response = requests.get(f"http://{domain}", timeout=2)  
            status_code = response.status_code

            if status_code in [200, 201, 202, 204, 206]:
                if response.url.startswith(official_site):
                    print(f"[-] Inativo (redireciona para {official_site}): {domain}")
                else:
                    print(f"[+] Ativo: {domain}")
                    active_domains.append(domain)

            elif status_code in [301, 302, 303, 307, 308, 403]: # Codigo 403 indica permissao insuficiente (Forbidden), codigos 300 indicam redirecionamento
                if response.url.startswith(official_site):
                    print(f"[-] Inativo (redireciona para {official_site}): {domain}")
                else:
                    print(f"[+!] Possivelmente ativo: {domain} - Código: {status_code}")
                    possible_active.append(domain)

            else:
                print(f"[-] Inativo: {domain} - Domínio inválido ou não encontrado")

        except requests.exceptions.RequestException as e:
            print(f"[-] Inativo: {domain} - Erro: Domínio inválido ou não encontrado")


# Lista de domínios para testar
domains_to_check = [

]


# with open('/path/example.com.csv', 'r') as arquivo:
#     leitor_csv = csv.reader(arquivo)
#     for linha in leitor_csv:
#         domains_to_check.append(linha[0])

progress = {'count': 0, 'total': len(domains_to_check)}
stop_flag = False

total_domains = len(domains_to_check)

listener = keyboard.Listener(on_press=on_press)
listener.start()

print(colored("Aperte ENTER para mostrar o progresso!", 'blue'))
print(colored("Aperte '+' para encerrar o programa!", 'blue'))
time.sleep(2)


active_domains = []
possibleActiveDomains = []
# Verifica quais domínios estão ativos
check_domains(domains_to_check, active_domains, possibleActiveDomains)


listener.stop()


print(colored("Todos os dominios foram verificados ou o processo foi encerrado!", 'green'))
print(colored("\nDomínios ativos: ", 'blue'))
print(active_domains)

print(colored("\nDomínios possivelmente ativos: ", 'blue'))
print(possibleActiveDomains)

termios.tcflush(sys.stdin,termios.TCIFLUSH) # Limpar o buffer

inputt = input(colored("Digite 'o' para abrir os dominios ativos no navegador ou qualquer outra tecla para encerrar o programa: ",'blue'))


if inputt.strip().lower() == 'o':
    for dominio in active_domains:
        if not dominio.startswith(('http://','https://')):
            dominio = "http://" + dominio
        webbrowser.open(dominio)

    for dominio in possibleActiveDomains:
        if not dominio.startswith(('http://','https://')):
            dominio = "http://" + dominio
        webbrowser.open(dominio)

    print(colored("Programa finalizado.",'red'))
else:
    print(colored("Programa finalizado.",'red'))
