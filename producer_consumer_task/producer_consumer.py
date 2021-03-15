
from threading import Thread, Semaphore, Event
import time
import random       

queue = []
MAX_NUM = 10
sem = Semaphore()

def is_consume_allowed():
    num = 10
    while num > 0:
        yield num
        num -= 1

def is_produce_allowed():
    num = 10
    while num > 0:
        yield num
        num -= 1

class ProducerThread(Thread):
    def __init__(self):
        super(ProducerThread, self).__init__()
        self.certificate = is_produce_allowed()
        self._stop_event = Event()
    
    def stop(self):
        self._stop_event.set()

    def run(self):
        nums = range(5) # [0 1 2 3 4]
        global queue
        if self._stop_event.is_set():
            return
        while True:
            try:
                x = next(self.certificate)
            
                sem.acquire()  # wait operation to stop consuming 
                while len(queue) == MAX_NUM:
                    
                    print ("List is full, producer will wait")
                    sem.release() # signal operation only when when queue is full and allow consumer to consume data

                    print ("Space in queue, Consumer notified the producer")
                    time.sleep(5)
                
                num = random.choice(nums) 
                queue.append(num) #added any random number from 0 to 4 to the list
                print ("Produced", num) 
                sem.release() #signal operation to allow consumer to consume data

                time.sleep(random.random()) #to allow program to run a bit slower
            except:
                print('Certificate expired. Can\'t produce anything')
                self.stop()
                break

class ConsumerThread(Thread):

    def __init__(self):
        super(ConsumerThread, self).__init__()
        self.certificate = is_consume_allowed()
        self._stop_event = Event()
    
    def stop(self):
        self._stop_event.set()

    def run(self):
        global queue
        if self._stop_event.is_set():
            return
        while True:
            try:
                x = next(self.certificate)
                if not x: 
                    return
                sem.acquire()   #wait operation to stop producing
                while not queue:
                    print ("List is empty, consumer waiting")
                    sem.release()  #signal operation only when when queue is empty and allow producer to produce data
                    
                    print ("Producer added something to queue and notified the consumer")
                    time.sleep(5)
                
                num = queue.pop(0)
            
                print ("Consumed", num)
                sem.release()  #signal operation to allow producer to produce

                time.sleep(random.random())
            except:
                print('Unauthorized consumer. Go away')
                self.stop()
                break

def main():
    ProducerThread().start()    #start producer thread
    ConsumerThread().start()    #start consumer thread

if __name__ == '__main__':
    main()

