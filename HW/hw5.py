# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 03:10:05 2022

@author: Tita
"""

class Node: #O(1)initialazing a node has a constant complexity
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self):#set the head: none value
        self.head = None
        
                
    #get the number of nodes in Linked List (lenght)   
    def lenghtNodes(self):
        h_node = self.head 
        count = 0 
  
        
        while (h_node):
            count += 1
            h_node = h_node.next
        return count
    
    #takes a number and adds it to the end of the list
    def addNode(self, new_value):#O(n) because the new node will iterate over other nodes until find its place
        if self.head is None:
            self.tail = self.head = Node(new_value) #If there is no nodes, then the head and tail will be the new value
            
        else:
            self.tail.next = Node(new_value) #if there is a tail, then the new node will be added next to the tail
            self.tail = self.tail.next
            
        return self.tail
    
    #this function will help me with the addNodeAfter function
    def getPosition(self, position):
        if position < 1:  #if is the position the first one, then will be the head
            return 
        current = self.head
    
        while current and position > 1:#if it is not the head, then will be find the position
            position -= 1
            current = current.next
        return current

    #takes a number and adds it after the after_node
    def addNodeAfter(self, new_value, after_node): 
        #using the position to insert the new node
        current = self.getPosition(after_node)
        new_node = Node(new_value)       
        new_node.next = current.next
        current.next = new_node
    #Takes a value and adds before the before_node
    def addNodeBefore(self, new_value, before_node):#O(1) in contrast to addNode, add a node before or after do not iterate over each node to find its place, it goes directly to its place. So the complexity is constant
        new_node = Node(new_value)
        
        if (before_node < 1):        
            print("That's an invalid node")
        
        if before_node == 0: #the node will be the head
            new_node.next = self.head
            self.head = new_node
        else: 
         current = before_node.next
         new_node.next = current
         before_node.next = new_node
         
         
    def removeNode(self, node_to_remove):#O(n) similar to addNode because need to iterate over the other nodes
        if node_to_remove == 0: #in case to remove head, then next node will be head
            self.head = self.head.next
        else:

            prev = self.getNode(node_to_remove)
            current = prev.next
            prev.next = current.next
            current = None
 
    
    #reverse linked list.
    def reverse(self): #O(n) because it changes node by node
        prev_node = None
        current_node = self.head
        while(current_node is not None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        
    
link_list = LinkedList()
link_list.addNode(5)
link_list.addNode(12)
link_list.addNode(9)
link_list.addNode(2)

link_list.lenghtNodes() 
link_list.reverse()
