import threading

# This class is used to make the (already quite simple) threading of python
# even easier. The thread class takes in the thread name and the functions
# that need threading.

# Use : 
# 1. define your functions
# 2. make thread objects with your functions
# 3. run the threads as needed

class thread(threading.Thread):
    def __init__(self, thread_name, function):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.function = function
    def run(self):
        self.function()


def printer():
    print("testings")

def printer2():
    print("testings2")

thread1 = thread('printtaaja', printer)
thread2 = thread('printtaaja', printer2)

thread2.start()
thread1.start()