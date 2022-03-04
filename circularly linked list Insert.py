class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def addToEmpty(self, data):
        if self.head != None:
            return self.head
        temp = node(data)
        self.head = temp
        self.head.next = self.head
        return self.head
    def addbegin(self, data):
        if self.head is None:
            return self.addToEmpty(data)
        temp =node(data)
        temp.next=self.head.next
        self.head.next=temp
        return self.head
    def addend(self,data):
        if self.head is None:
            self.addToEmpty(data)
        temp = node(data)
        temp.next=self.head.next
        self.head.next=temp
        self.head=temp
        return self.head
    def addafter(self,data,item):
        if self.head is None:
            return None
        temp =node(data)
        p=self.head.next
        while p:
            if p.data is item:
                temp.next=p.next
                p.next=temp
                if p is self.head:
                    self.head=temp
                    return self.head
                else:
                    return self.head
            p = p.next
            if p == self.head.next:
                print(item,"Not present in the List")
                break
    def printlist(self):
        temp = self.head.next
        while(temp):
            print(temp.data, end=",")
            temp = temp.next
            if temp == self.head.next:
                break
if __name__ == "__main__":
    llist=linkedlist()
    llist.addToEmpty(7)
    llist.addbegin(6)
    llist.addend(5)
    llist.addend(8)
    llist.addbegin(2)
    llist.addafter(8,7)
    llist.printlist()



