from multiprocessing import Process
import time



def say():
    for i in range(100):
        
        time.sleep(1)  
        print("aaaaaaaaaaa")
def say2():
    for i in range(10):
        
        time.sleep(1)
        print("*********************************************************")
def together():
    p1 = Process(target=say)
    p2 = Process(target=say2)
    p1.start()
    p2.start()

    
if __name__ == '__main__':
    together()