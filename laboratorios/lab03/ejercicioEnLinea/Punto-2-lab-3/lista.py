"""
Title: Linked List | Set 2 (Inserting a node)
Author: Manikantan Narasimhan 
Code version: 1.0
Availability: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
"""
# Node class 
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

# Linked List class contains a Node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Functio to insert a new node at the beginning 
	def push(self, new_data): 

		# 1 & 2: Allocate the Node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 3. Make next of new Node as head 
		new_node.next = self.head 

		# 4. Move the head to point to new Node 
		self.head = new_node
	# This function is in LinkedList class. Inserts a 
	# new node after the given prev_node. This method is 
	# defined inside LinkedList class shown above */ 
	 
	# This function is defined in Linked List class 
	# Appends a new node at the end. This method is 
	# defined inside LinkedList class shown above */ 
	def append(self, new_data): 

		# 1. Create a new node 
		# 2. Put in the data 
		# 3. Set next as None 
		new_node = Node(new_data) 

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while (last.next): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 

	# Utility function to print the linked list 
	def printList(self): 
		temp = self.head
		while (temp): 
			print (temp.data)
			temp = temp.next