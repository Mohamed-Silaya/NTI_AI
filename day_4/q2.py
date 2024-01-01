class OutRangeException(Exception):
    pass

class Queue:
    queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.queue = []
        Queue.queues[name] =  self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise OutRangeException("Out Of Range Exception: Cannot insert more values than the queue's size.")
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: Cannot pop value from an empty queue.")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    @classmethod
    def get_queue(cls, name):
        return cls.queues.get(name, None)





# Create a new queue
q1 = Queue("Queue1", 3)

# Insert values into the queue1
q1.insert(5)
q1.insert(10)
q1.insert(15)

# Try to insert more values than the queue's size
try:
    q1.insert(30)
except OutRangeException as err:
    print(str(err)) 

# Create queue2
q2 = Queue("Queue2", 2)

# Insert values into the second queue
q2.insert(50)
q2.insert(60)

# Get a queue using its name
gett_queue = Queue.get_queue("Queue1")
print(gett_queue.name)  

# Remove and retrieve values from the first queue
print(q1.pop())  
print(q1.pop())  
print(q1.pop()) 
print(q1.pop()) 

# Check if the second queue is empty
print(q2.is_empty()) 

geet_queue2 = Queue.get_queue("Queue2")
print(geet_queue2.name) 
print(geet_queue2.queue)  