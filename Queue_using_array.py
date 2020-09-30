
class Queue:
    def __init__(self,size):
        self.front=-1 
        self.rear=-1
        self.que=[None]*size   #create array of given size 
    
    def isEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False
    
    def check_full(self):
        if self.rear==len(self.que)-1:
            return True
        return False
    
    def display(self):
        return self.que
    
    def enqueue(self,data):
        if self.check_full():
            print('Queue is full ')
        else:
            if self.isEmpty():
                self.rear+=1
                self.front+=1
                self.que[self.rear]=data
            else:
                self.rear+=1 
                self.que[self.rear]=data
                
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        self.que[self.front]=None
        if self.front<self.rear:
            self.front+=1
        else:
            self.front=-1
            self.rear=-1
#Driver Code
if __name__ == '__main__':
    size_of=int(input('enter size length of queue: '))
    q=Queue(size_of)
    for i in range(1,size_of+1):
        q.enqueue(i)
    print('The Queue is ')
    print(q.display())
    print('Delete the element at front ')
    q.dequeue()
    print(q.display())


    