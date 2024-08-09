class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(12)
node3 = Node(2)
node4 = Node(8)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("forward linked list print : /n")

currentNode = node1
while currentNode:
    print(currentNode.data ,end = " ==>")
    currentNode = currentNode.next
print("null")

print("reverese maping of linkedlist node")
currentNode = node4
while currentNode:
    print(currentNode.data , end = "=>")
    currentNode = currentNode.prev
print("Null")

# this is for duoble linked list