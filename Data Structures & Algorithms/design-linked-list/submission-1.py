class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head

        for i in range(index):
            if current is None:
                return -1 
            current = current.next
        
        return current.val if current is not None else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
            
        self.head = node
        
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.prev = self.tail

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node 
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        current = self.head

        if index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
            return

        for i in range(index):
            if current is None:
                return
            current = current.next
        
        if current is not None:
            prev_node = current.prev

            prev_node.next = node
            node.prev = prev_node
            node.next = current
            current.prev = node
        else:
            self.addAtTail(val)

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        current = self.head

        

        for i in range(index):
            if current is None:
                return
            current = current.next

        if current is not None:
            prev = current.prev
            next = current.next

            if prev is None:
                self.head = next
            else:
                prev.next = next
            if next is None:
                self.tail = prev
            else:
                next.prev = prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)