#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import httpclient
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, authenticated
from tornado_http_auth import BasicAuthMixin, auth_required

CREDENTIALS = {'user1': 'pass1'}


class BaseHandler(RequestHandler):
    """Override the get_current_user() method in your request handlers to 
    determine the current user based on, e.g., the value of a cookie

    """

    def get_current_user(self):
        return self.get_secure_cookie("user")


class LoginHandler(BaseHandler, BasicAuthMixin):
    """ Gerencia o login na aplicação e gera o cookie para manter 
    a conexão

    """

    @auth_required(realm='Protected', auth_func=CREDENTIALS.get)
    def get(self):
        self.set_secure_cookie("user", self._current_user)
        self.write('login ok')

class GetCpfHandler(BaseHandler, RequestHandler, BasicAuthMixin):

    """Recebe a requisição GET(usuario) com parâmetro CPF para fazer a busca no banco

    **parameters** and **return**::
        

    :param cpf: CPF que será buscado no banco
    :return: Retorna o Json com os dados se o cpf existir na base, ou uma lista vazia se nao existir
            
    """



    @authenticated
    async def get(self):
        self.cpf =  self.get_argument('cpf')
        self.cpfSearch = await self.getCpf(self.cpf)
        self.write(self.cpfSearch)



    @authenticated
    async def getCpf(self, cpf: int):
        http_client = httpclient.AsyncHTTPClient()
        try:
            response = await http_client.fetch(f'http://localhost:8000/base_client?cpf={self.cpf}')
        except Exception as e:
            print("Error: %s" % e)
        else:
            print(response.body)
            return(response.body)
    
    
settings = {
"cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
"login_url": "/login",
}


def main():

    # Verify the database exists and has the correct layout

    app = Application([
        (r"/?", GetCpfHandler),
        (r"/login/?", LoginHandler),
], **settings)

    server = httpserver.HTTPServer(app, ssl_options={
        "certfile": "./certificate.pem",
        "keyfile": "./key.pem"})
    server.bind(443)
    server.start(4) # forks one process per cpu
    IOLoop.instance().start()



if __name__ == "__main__":
    main()


