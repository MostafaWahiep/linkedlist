class Node:
    """
    Node class
    
    Attributes:
        value: value of the node
        next: pointer to the next node
    
    Methods:
        __init__(value, next): constructor
    """
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:

    """
    LinkedList class

    Attributes:
        __head__: head of the linked list
        __tail__: tail of the linked list
        __size__: size of the linked list

    Methods:
        add(value): add a node to the end of the linked list  
        size(): return the size of the linked list
        empty(): return True if the linked list is empty, False otherwise
        push_front(value): add a node to the front of the linked list
        insert(value, index): add a node to the linked list at the given index
        get_at(index): return the value of the node at the given index
        pop_front(): remove the first node of the linked list
        remove(index): remove the node at the given index
        pop_back(): remove the last node of the linked list
        get_list(): return a list of all the values in the linked list
        clear(): remove all the nodes from the linked list
        reverse(): reverse the linked list


    """

    def __init__(self):
        self.__head__ = None
        self.__tail__ = None
        self.__size__ = 0

    def push_back(self, value):
        if(self.__head__ == None):
            self.__head__ = Node(value)
            self.__tail__ = self.__head__
        else:
            self.__tail__.next = Node(value)
            self.__tail__ = self.__tail__.next
        self.__size__ += 1

    def size(self):
        return self.__size__
    
    def empty(self):
        return self.__size__ == 0
    
    def push_front(self, value):
        node = Node(value,self.__head__)
        self.__head__ = node
        self.__size__ += 1
    
    def insert(self, value, index):
        if index < 0 or index > self.size():
            exit(1)
        elif index == self.__size__:
            self.push_back(value)
        elif index == 0:
            self.push_front(value)
        else:
            ptr = self.__head__
            for i in range(index - 1):
                ptr = ptr.next
            node = Node(value, ptr.next)
            ptr.next = node
            self.__size__ += 1
    
    def get_at(self, index):
        if index < 0 or index > self.size():
            exit(1)
        elif index == self.size():
            return self.__tail__.value
        else:
            ptr = self.__head__
            for i in range(index):
                ptr = ptr.next
            return ptr.value
        
    def pop_front(self):
        if self.empty():
            exit(1)
        elif self.size() == 1:
            self.__head__ = None
            self.__tail__ = None
        else:
            self.__head__ = self.__head__.next
        self.__size__ -= 1
    
    def remove(self, index):
        if index < 0 or index > self.size():
            exit(1)
        elif index == 0 or self.size() == 1:
            self.pop_front()
        else:
            ptr = self.__head__
            for i in range(index - 1):
                ptr = ptr.next
            ptr.next = ptr.next.next
            self.__size__ -= 1

    def pop_back(self):
        self.remove(self.__size__ - 1)
    
    def get_list(self):
        # return the linked list as a list
        lst = []
        ptr = self.__head__
        while ptr != None:
            lst.append(ptr.value)
            ptr = ptr.next
        return lst
    
    def clear(self):
        # clear the linked list
        self.__head__ = None
        self.__tail__ = None
        self.__size__ = 0

    def reverse(self):
        # reverse the linked list
        ptr = self.__head__
        self.__tail__ = ptr
        prev = None
        while ptr != None:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        self.__head__ = prev
