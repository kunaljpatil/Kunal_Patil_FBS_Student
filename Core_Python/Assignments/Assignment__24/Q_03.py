# Write A Program Implement two threads to print lowercase and uppercase alphabets concurrently from 'a' to 'z' and 'A' to 'Z'.

from threading import Thread, Condition

cond = Condition()
ind = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'



def small():
    global ind
    global alpha
    with cond:
        while ind < 26:
            print(alpha[ind])
            cond.notify()
            cond.wait()

def upp():
    global ind
    global alpha
    with cond:
        while ind < 26:
            print(alpha[ind].upper())
            ind = ind + 1
            cond.notify()
            cond.wait()

if __name__ == '__main__':
    t1 = Thread(target=small)
    t2 = Thread(target=upp)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
            
            
        
