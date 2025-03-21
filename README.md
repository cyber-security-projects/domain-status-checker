# domain-status-checker
Script em Python para verificar a atividade de domínios via requisições HTTP, com foco em identificação de possíveis sites de phishing. Permite checagem manual ou via arquivo CSV, exibe progresso em tempo real e oferece opção de abrir domínios suspeitos no navegador.

# 🔍 Verificador de Atividade de Domínios (com foco em Phishing)

Este script em Python automatiza a verificação da atividade de domínios por meio de requisições HTTP, com o objetivo de identificar possíveis sites de phishing ou domínios ativos.

---

## ⚙️ Como funciona

- Faz uma requisição HTTP para cada domínio listado.
- Considera o domínio **ativo** se responder com um código `2xx` e **não redirecionar** para o site oficial.
- Considera **possivelmente ativo** se responder com códigos `3xx` ou `403` e **não redirecionar** para o site oficial.
- Considera **inativo** se:
  - Redireciona para o site oficial
  - Retorna erro
  - Não responde

Durante a execução:
- Pressione `ENTER` para exibir o progresso.
- Pressione `+` para interromper a verificação.

---

## 📝 Pré-requisitos

- Python 3
- Instalar dependências:

```bash
pip install requests termcolor pynput
```

---

## 🚀 Como usar

1. Clone o repositório ou copie o script.

2. Edite a variável `official_site` no código:

```python
official_site = "http://example.com"  # Substitua pelo domínio legítimo se for conveniente
```

3. Forneça a lista de domínios:

### Opção A: Manual

Adicione diretamente no script:

```python
domains_to_check = [
    'dominio1.com',
    'dominio2.com.br',
    ...
]
```

### Opção B: A partir de um arquivo `.csv` ou semelhantes

Descomente e edite este trecho no código:

```python
with open('/caminho/para/arquivo.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        domains_to_check.append(linha[0])
```

---

## 📥 Saída

Ao final da execução:

- Exibe domínios **ativos** e **possivelmente ativos**.
- Permite ao usuário abrir esses domínios no navegador pressionando `'o'`.

---

## 📌 Observações

- Não é necessário executar como `sudo`.

---

## 📁 Tecnologias utilizadas

- `requests`
- `pynput`
- `termcolor`
- `csv`
- `webbrowser`

---

## 👨‍💻 Autor

**Threat Intelligence**

