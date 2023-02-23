import threading
import time
import queue

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        qp = QProcess(self.name, self.q)
        print("Starting " + self.name)
        qp.mydata()
        print("Exiting " + self.name)

class QProcess:

    def __init__(self, name, q):
        self.tname = name
        self.q = q


    def mydata(self):
        while not exitFlag:
            queueLock.acquire()
            if not self.q.empty():
                data = self.q.get()
                queueLock.release()
                print("{} processing {}".format(self.tname, data))
            else:
                queueLock.release()
                time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print
"Exiting Main Thread"
