class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        ptr1 = node(data)
        temp = self.head
        ptr1.next = self.head
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        self.head = ptr1

    def deleteNode(self, key):
        if (self.head == None):
            return
        if ((self.head).data == key and (self.head).next == self.head):
            self.head = None
        last = self.head
        d = None
        if ((self.head).data == key):
            while (last.next != self.head):
                last = last.next
            last.next = (self.head).next
            self.head = last.next
        while (last.next != self.head and last.next.data != key):
            last = last.next
        if (last.next.data == key):
            d = last.next
            last.next = d.next
        #else:
          #  print("no such keyfound")
        return self.head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                break
llist = LinkedList()
llist.push(12)
llist.push(56)
llist.push(2)
print("Before Delete the Value")
llist.printList()
llist.deleteNode(2)
print("\nAfter Delete Linked List")
llist.printList()

