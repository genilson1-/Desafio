import pymongo 
import motor
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient('localhost', 27017)
db = client['test_database'] 
db = motor.motor_tornado.MotorClient().test_database


async def do_insert(): 
        result = await db.test_collection.insert_many( 
            [{'name' : 'maria'+str(i), 'cpf':10000000000+i, 'dividas':[1+i, 2+i, 3+i]} for i in range(2000)]) 
        print('inserted %d docs' % (len(result.inserted_ids),)) 

IOLoop.current().run_sync(do_insert)
