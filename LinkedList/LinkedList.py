# class to store the data adress and data
class Node:
    def __init__(self, data , next= None):
        self.data = data
        self.next = next

# class to design the linked list it self
# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

# insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
# treverse thorugh the array
    def traverse(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
#find element in linked list
    def find(self, data):
        current = self.head
        while(current):
            if(current.data == data):
                print("we find it")
            current = current.next
# delete element in linked list
    def delete(self, key):
        current = self.head
        # If head node itself holds the value to be deleted
        if (current is not None):
            if (current.data == key):
                self.head = current.next
                current = None
                return
        while(current is not None):
            if (current.data == key):
                break
            previous = current
            current = current.next
        if(current == None):
            return
        previous.next = current.next
        current = None
#delete at specfic position
    def deletePosition(self, index):
        current = self.head
        count = 0
        if(index == 0 and current is not None):
            self.head = current.next
            current = None
        current = current.next
        while(current is not None):
            count += count
            if count == index:
                break
        previous = current
        current = current.next
        if(current == None):
            return
        previous.next = current.next
        current = None


#   Linked List with a single node
LL = LinkedList()
LL.insert(4)
LL.insert(5)
LL.insert(5)
LL.insert(1)
LL.insert(9)
print(LL)
LL.traverse()
# LL.find(1)
LL.find(3)
LL.delete(9)
LL.delete(4)
print("the linked list after delete")
LL.traverse()
LL.deletePosition(0)
print("the linked list after delete")
LL.traverse()


