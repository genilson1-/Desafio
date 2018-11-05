# Desafio

Pré-requisitos
----------------------
Para rodar o WS é necessário ter o mongodb instalado e rodando na porta 27017.

Instalando as dependencias do python (lembrando, o python usado foi a versao 3.7)

### Instalando:

Depois de instalar o mongodb, e colocar ele para rodar, é necessário criar o payload que será consultado pela nossa aplicação.
Um script python com nome dadosMongo.py estará disponível para ser executado:
	

Fazer o clone do projeto:

	$ git clone https://github.com/genilson1-/Desafio.git	

Entrar no diretorio e criar um ambiente virtual com venv:

	$ python3.7 -m venv venv

Ativar o ambiente virtual:

	source venv/bin/activate

Instalando as dependencias do python com pip:

	$ pip install -r requeriments.txt

Populando o banco:

	$ python dadosMongo.py


### Executando:

Dois códigos (api.py e bancoService.py) deverão ser executados, como mostrado abaixo (o sudo é necessário porque o serviço ta rodando na 443 https):

	$ sudo python api.py
	$ python bancoService.py


### Usando:

Se todos os passos acima tiverem ocorridos com sucesso, a aplicação está pronta para ser testada. Antes de começar, algumas considerações devem ser feitas:
* O bancoService.py (onde fica a conexao com o banco mongo) por motivo de segurança só aceita conexão local host. 

* E um certificado foi gerado. Talvez seja necessário utilizar algo como validate_cert=False. 

* Para diminiuir um pouco a complexidade de montar o ambiente e por falta de tempo, o usuário e senha estão declarados no início do código como texto limpo (user1, pass1).

* Para a utilização do serviço é necessário manipular cookies para manter a sessão aberta e ter acesso ao serviço.

* No banco foram cadastrados 2000 entradas que seguem o seguinte modelo: {"maria1900": 1900, "cpf": 10000001900, "dividas": [1901, 1902, 1903]}]'.

* A chave de busca será o cpf que pode variar de 10000000000 até 10000001999.

* A ferramenta escolhida para demonstração foi o requests do python.

### Autenticação

* Autenticando e capturando o cookie:

```python	

	import requests
	from requests.auth import HTTPBasicAuth
	import json	

	login = requests.get('https://localhost/login', auth=HTTPBasicAuth('user1', 'pass1'), verify=False)

```

#### Setando o Cookie

* Pegando o cookie:

```python

	cookie = {'Cookie': login.headers['Set-Cookie']}

```

#### Consumindo API

* Fazendo nova requisição para consumir os dados:

```python

	 dados = requests.get('https://localhost/?cpf=10000001000', headers=cookie, verify=False)

```

#### Manipulando os dados como Dict

* Convertendo os dados para um dict:

```python

	 dadosDict = json.loads(dados.content)

```

* Acessando o campo cpf:

```python

	cpf = dadosDict[0]['cpf']

```

### Teste

* Para executar os teste basta executar o código tests.py:
	
	$ python tests.py
	
