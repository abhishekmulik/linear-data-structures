class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.front=None
        self.rear=None
    
    def isEmpty(self):
        if self.head==None:
            return True
        return False
    
    def enqueue(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.front=newNode
            self.rear=newNode
            self.head=self.front
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            self.rear=newNode   
            
    def display(self):
        if self.isEmpty():
            print('Empty Queue')
        else:
            temp=self.front
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty!')
        else:
            temp=self.front
            self.front=temp.next
            self.head=self.front
        
        
#driver code 
if __name__ == '__main__':
    q=Queue()
    q.display()
    for i in range(1,6):     # to insert elements
        q.enqueue(i)
    q.display()
    print("remove first two elements")
    for _ in range(3):    #to remove elements
        q.dequeue()
    q.display()


            
        