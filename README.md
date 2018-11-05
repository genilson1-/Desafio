# Desafio

Prerequisites
----------------------
Para rodar o WS é necessário ter o mongodb instalado e rodando na porta 27017.

Instalando as dependencias do python (lembrando, o python usado foi a versao 3.7)

### Instalando:

Fazer o clone do projeto:

	$ git clone https://github.com/genilson1-/Desafio.git	

Entrar no diretorio e criar um ambiente virtual com venv:

	$ python3.7 -m venv venv

Ativar o ambiente virtual:

	source venv/bin/activate

Instalando as dependencias do python com pip:

	$ pip install -r requeriments.txt


### Executando:

Dois códigos (api.py e bancoService.py) deverão ser executados, como mostrado abaixo (o sudo é necessário porque o serviço ta rodando na 443 https):

	$ sudo python api.py
	$ python bancoService.py


### Usando:

Se todos os passos acima tiverem ocorridos como sucesso, a aplicação está pronta para ser testada. Antes de começar, alguns considerações devem ser feitas:
* O bancoService.py (onde fica a conexao com o banco mongo) por motivo de segurança só aceita conexão local host. 

* E um certificado foi gerado. Talvez seja necessário utilizarum validate_cert=False. 

* Para diminiuir um pouco a complexidade de montar o ambiente, e por falta de tempo o usuário e senha estão declarados no início do código como texto limpo (user1, pass1).

* Para a utilização do serviço é necessário manipular cookies para manter a sessão aberta e ter acesso ao serviço.

* A ferramenta escolhida para demostração foi o requests do python.



