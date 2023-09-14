class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self, val):
        if self.is_empty():
            print("Warning: Queue is empty.")
            return None
        return self.queue.pop(val)

    def is_empty(self):
        length=len(self.queue)
        return length == None
    



q1 = Queue()
#is empty
print(q1.is_empty())  
iterate = int(input("inter the number of values you need to add:    "))
for i in range(iterate):
    valu = input("enter the value you need to insert:   ")
    intval= int(valu)
    q1.insert (intval)

print(q1.is_empty())  

# Pop values 
pop_val= int (input("what index you need to pop"))
print("poped value")
print(q1.pop(pop_val)) 
  
