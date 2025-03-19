import time
import os 
import multiprocessing
starting_time = time.time()
import threading
# processor in python works simentaniouslly 
# threds in python works in concurrent 

def india():
    print(f'CPU1 Processer id : {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')

def usa():
    print(f'CPU1 Processer id : {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'usa : {i}')

def paris():
    print(f'CPU1 Processer id : {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'paris : {i}')


def uk():
    print(f'CPU2 Processer id : {os.getpid()}')
    for j in range(1,11):
        time.sleep(0.5)
        print(f'Uk : {j}')

def common_1():
    t1 = threading.Thread(target=india,args=())
    t2 = threading.Thread(target=usa,args=())
    
    t1.start()
    t2.start()


def common_2():
   t3 = threading.Thread(target=uk,args=())
   t4 = threading.Thread(target=paris,args=())
    
   t3.start() 
   t4.start()
   
if __name__ == "__main__":
    print(f"Main Processor Id Number : {os.getpid()}")

    cpu1 = multiprocessing.Process(target=common_1,args=())
    cpu2 = multiprocessing.Process(target=common_2,args=())

    cpu1.start()
    cpu2.start()

    cpu1.join()
    cpu2.join()
    
    print(f'total time : {time.time() - starting_time}')
    print(f"Main Processor Exists")



