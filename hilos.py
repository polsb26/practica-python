#modulos necesarios para trabajar con hilos 
import threading
import time

# print(threading.active_count())
# print(threading.enumerate())

#definicion de hilos 
def accion1():
    print("Iniciando hilo 1")
    time.sleep(4)
    print("Terminando hilo 1")

def accion2():
    print("Iniciando hilo 2")
    time.sleep(6)
    print("Terminando hilo 2")

def accion3():
    print("Iniciando hilo 3")
    time.sleep(4)
    print("Terminando hilo 3")

inicio =time.perf_counter()

#Iniciando tareas por hilos 
x= threading.Thread(target=accion1)
x.start()
y= threading.Thread(target=accion2)
y.start()
z= threading.Thread(target=accion3)
z.start()

# accion1()
# accion2()
# accion3()

print(threading.active_count())
# print(threading.enumerate())    

fin = time.perf_counter()

print(f"Tiempo de ejecucion: {fin - inicio}")
