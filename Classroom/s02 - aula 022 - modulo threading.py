from threading import Thread
import time

def faz_algo(i):

    print('Executando thread {}...'.format(i))
    time.sleep(3)
    print('Finalizando a thread {}...'.format(i))


for i in range(5):
    t = Thread(target=faz_algo, args=(i,))
    t.start()