from LinkedList import LinkedList

# testing with assertions
ll = LinkedList()
assert ll.size() == 0
assert ll.empty() == True
print("test 1 passed")

ll.push_back(1)
assert ll.size() == 1
assert ll.empty() == False
print("test 2 passed")

ll.pop_back()
assert ll.size() == 0
assert ll.empty() == True
print("test 3 passed")

ll.push_front(1)
assert ll.size() == 1
assert ll.empty() == False
print("test 4 passed")

ll.pop_front()
assert ll.size() == 0
assert ll.empty() == True
print("test 5 passed")

ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
assert ll.size() == 3
assert ll.empty() == False
print("test 6 passed")

ll.pop_front()
assert ll.size() == 2
assert ll.empty() == False
print("test 7 passed")

ll.pop_back()
assert ll.size() == 1
assert ll.empty() == False
print("test 8 passed")

ll.pop_back()
assert ll.size() == 0
assert ll.empty() == True
print("test 9 passed")

ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_front(0)
assert ll.size() == 4
assert ll.empty() == False
print("test 10 passed")

ll.pop_front()
assert ll.size() == 3
assert ll.empty() == False
print("test 11 passed")

ll.pop_back()
assert ll.size() == 2
assert ll.empty() == False
print("test 12 passed")

ll.pop_back()
assert ll.size() == 1
assert ll.empty() == False
print("test 13 passed")

ll.pop_back()
assert ll.size() == 0
assert ll.empty() == True
print("test 14 passed")

ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_front(0)
ll.push_front(-1)
assert ll.size() == 5
assert ll.empty() == False
assert ll.get_list() == [-1, 0, 1, 2, 3]
print("test 15 passed")

ll.pop_front()
assert ll.size() == 4
assert ll.empty() == False
assert ll.get_list() == [0, 1, 2, 3]
print("test 16 passed")

ll.pop_back()
assert ll.size() == 3
assert ll.empty() == False
assert ll.get_list() == [0, 1, 2]
print("test 17 passed")

ll.clear()
assert ll.size() == 0
assert ll.empty() == True
assert ll.get_list() == []
print("test 18 passed")

ll.insert(1, 0)
assert ll.size() == 1
assert ll.empty() == False
assert ll.get_list() == [1]
print("test 19 passed")

ll.insert(2, 1)
assert ll.size() == 2
assert ll.empty() == False
assert ll.get_list() == [1, 2]
print("test 20 passed")

ll.insert(0, 0)
assert ll.size() == 3
assert ll.empty() == False
assert ll.get_list() == [0, 1, 2]
print("test 21 passed")

ll.insert(3, 3)
assert ll.size() == 4
assert ll.empty() == False
assert ll.get_list() == [0, 1, 2, 3]
print("test 22 passed")

ll.insert(4, 4)
assert ll.size() == 5
assert ll.empty() == False
assert ll.get_list() == [0, 1, 2, 3, 4]
print("test 23 passed")

ll.remove(0)
assert ll.size() == 4
assert ll.empty() == False
assert ll.get_list() == [1, 2, 3, 4]
print("test 24 passed")

ll.remove(1)
assert ll.size() == 3   
assert ll.empty() == False
assert ll.get_list() == [1, 3, 4]
print("test 25 passed")

ll.remove(2)    
assert ll.size() == 2
assert ll.empty() == False
assert ll.get_list() == [1, 3]
print("test 26 passed")

ll.clear()
assert ll.size() == 0
assert ll.empty() == True
assert ll.get_list() == []
print("test 27 passed")

ll.push_back(1)
ll.reverse()
assert ll.size() == 1
assert ll.empty() == False
assert ll.get_list() == [1]
print("test 28 passed")

ll.push_back(2)
ll.reverse()
assert ll.size() == 2
assert ll.empty() == False
assert ll.get_list() == [2, 1]
print("test 29 passed")

ll.push_back(3)
ll.reverse()
assert ll.size() == 3
assert ll.empty() == False
assert ll.get_list() == [3, 1, 2]
print("test 30 passed")

ll.push_back(4)
ll.reverse()
assert ll.size() == 4
assert ll.empty() == False
assert ll.get_list() == [4, 2, 1, 3]
print("test 31 passed")

ll.clear()
ll.reverse()
assert ll.size() == 0
assert ll.empty() == True
assert ll.get_list() == []
print("test 32 passed")

ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_back(4)
ll.push_back(5)
assert ll.get_at(0) == 1
assert ll.get_at(1) == 2
assert ll.get_at(2) == 3
assert ll.get_at(3) == 4
assert ll.get_at(4) == 5
print("test 33 passed")
