class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            if cur is None:
                return -1
            cur = cur.next

        if cur is None:
            return -1
        
        return cur.val
            

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head

        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head

        if cur is None:
            self.head = new_node
            return
        
        while cur.next is not None:
            cur = cur.next
        
        cur.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        cur = self.head

        for _ in range(index - 1):
            if cur.next is None:
                return False
            cur = cur.next

        if cur.next is None:
            return False

        cur.next = cur.next.next
        return True
        

    def getValues(self) -> List[int]:
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next

        return result
        
