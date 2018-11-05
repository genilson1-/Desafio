#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo # manipulações no mongodb
import motor # Asynchronous Python driver for MongoDB
from tornado import httpserver 
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from bson.json_util import dumps 
import tornado
import json
import ast


#iniciando conexão com o banco de dados mongodb
client = motor.motor_tornado.MotorClient('localhost', 27017)
db = client['test_database']
db = motor.motor_tornado.MotorClient().test_database


class FindCpfHandler(tornado.web.RequestHandler):
    async def get(self):
        """Recebe a requisição GET com parâmetro CPF para fazer a busca no banco

        **parameters** and **return**::
        

        :param cpf: CPF que será buscado no banco
        :return: Retorna o json com os dados. Se o cpf não for informado, será enviado
        uma msg de erro 400: Bad Request ou se a requisição não for localhost o acesso será negado 
            
        """

        self.cpf =  self.get_argument('cpf')
        print(self.request.remote_ip)
        if (self.request.remote_ip == '::1'):
            dataAll = await self.do_find(self.cpf) 
            jsonData = [ast.literal_eval(data) for data in dataAll]
            self.write(json.dumps(jsonData))
        else:
            self.write('error, access deny')
        """Faz a busca no banco Mongodb pelo cpf informado                          
                                                                                                          
        **parameters** and **return**::                                                                   
                                                                                                          
                                                                                                          
        :param cpf: CPF que será buscado no banco                                                         
        :return: Retorna o json com os dados ou retorna uma lista vazia se o 
        cpf não for encontrado.
                                                                                                          
        """ 

    async def do_find(self, cpf: int):
        cursor = db.test_collection.find({'cpf' : int(cpf) }, {'_id':0} )
        dataAll = [dumps(document) for document in await cursor.to_list(length=int(1))]
        return(dataAll)

#Instanciando a aplicação e as rotas
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/base_client/?", FindCpfHandler),
           ]

        tornado.web.Application.__init__(self, handlers)


#configurações gerais da app
def main():
    # Verify the database exists and has the correct layout
    app = Application()
    app.listen(8000)
    IOLoop.current().start()


#start na app
if __name__ == "__main__":
    main()


