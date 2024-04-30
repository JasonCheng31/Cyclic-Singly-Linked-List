class Single_Node():
  def __init__(self, data, next = None):
    # Stores data in the node and reference to the next node
    self.data = data 
    self.next = next 
class Cyclic_list():
  # Initializing the cylic linked list with head, tail, and size 
  def __init__(self):
    self.list_head = None
    self.list_tail = None
    self.list_size = 0

  def size(self):
    # Returns the size of the linked list
    return self.list_size

  def empty(self):
    # Checks if the linked list is empty
    return self.list_size ==0

  def front(self):
    # Returns the data of the first node
    if self.empty():
      raise Exception("Linked list is empty")
    return self.list_head.data

  def back(self):
    # Returns the data of the last node
    if self.empty():
      raise Exception("Linked list is empty")
    return self.list_tail.data

  def head(self):
    # Returns the head node
    return self.list_head

  def tail(self):
    # Returns the tail node
    return self.list_tail

  def count(self, obj):
    # Counts how many objects are in the linked list.
    if self.size()==0:
      raise Exception("Linked list is empty")
    current = self.list_head
    counter = 0
    while current:
      if current.data == obj:
        counter+=1
      current = current.next
      if current == self.list_head:
        break
    return counter

  def push_front(self, obj):
    # Inserts a new node to the front of the list
    Node = Single_Node(obj)
    if self.empty(): # When the linked list is empty, we must set the node as head and tail.
      self.list_head = Node
      self.list_tail = Node
      self.list_size +=1
      Node.next = Node
    else:
      Node.next = self.list_head
      self.list_tail.next = Node
      self.list_size +=1
      self.list_head = Node


  def push_back(self, obj):
    # Inserts a new node to the back of the list
    Node = Single_Node(obj)
    if self.empty():
      self.list_tail = Node
      self.list_head = Node
      self.list_size +=1
      Node.next = Node
    else:
      Node.next = self.list_head
      self.list_tail.next = Node
      self.list_size +=1
      self.list_tail = Node

  def pop_front(self):
    # Removes the first node 
    if self.size()==0:
      raise Exception("Linked list is empty")
    front = self.list_head.data
    if self.size() == 1:
      # If the size is 1, the node is a head and tail, therefore it must be set to None
      self.list_head = None
      self.list_tail = None
      self.list_size -=1
    else:
      self.list_tail.next = self.list_head.next
      self.list_head = self.list_head.next
      self.list_size -=1
    return front


  def erase(self, obj):
    current = self.list_head
    prev = None
    # Removes all nodes with the specified data from the linked list. Takes care of all edge cases
    for _ in range(self.list_size):
      if current.data == obj:
        if prev == None:
          # If prev is None, then we don't use prev within this if statement because we are removing the first node or the linked list size is 1. 
          if self.size() == 1:
            self.list_head = None
            self.list_tail = None
          else:
            self.list_head = current.next
            self.list_tail.next = self.list_head
            current = self.list_head

        elif current == self.list_tail:
          prev.next = current.next
          current = current.next
          self.list_tail = prev
        else:
          prev.next = current.next
          current = current.next
        self.list_size -=1
      else:
        prev = current
        current = current.next

    if self.size()== 0:
      return None





