class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sort:
    def __init__(self):
        self.head=None
    def push(self,data):
            ptr = node(data)
            temp = self.head
            ptr.next=self.head
            if self.head is not None:
                while temp.next is not self.head:
                    temp=temp.next
                temp.next=ptr
            else:
                ptr.next=ptr
            self.head=ptr
    def sorting(self):
        if self.head is None:
            return self.head
        current = self.head.next
        index=None
        if self.head is not None:
            while current is not self.head:
                index = current.next
                while index is not current:
                    if (current.data < index.data):
                        temp = current.data
                        current.data=index.data
                        index.data=temp
                    index=index.next
                current=current.next
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=",")
            temp=temp.next
            if (temp is self.head):
                break
llist=sort()
llist.push(6)
llist.push(8)
llist.push(3)
llist.push(9)
print("Before Sorting")
llist.printlist()
print("\nAfter Sorting")
llist.sorting()
llist.printlist()
