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
    def exchangeNodes(self):
        head=self.head
        if head == None or head.next == head:
            return head
        elif head.next.next == head:
            head = head.next
            return head
        else:
            prev = None
            curr = head
            temp = head
            while curr.next != head:
                prev = curr
                curr = curr.next
            curr.next = temp.next
            prev.next = temp
            temp.next = curr
            head = curr
            return head
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
print("\nAfter Swaping")
llist.exchangeNodes()
llist.printlist()
