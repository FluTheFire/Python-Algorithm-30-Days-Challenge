class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class SLinkedList:
  def __init__(self):
    self.head = None

  # print the linked list
  def listprint(self):
    printval = self.head
    while printval is not None:
      print(printval.data)
      printval = printval.next

  # เพิ่ม node ที่จุดเริ่มต้น
  def AtBegining(self, newdata):
    NewNode = Node(newdata)
    # Update ค่า next ของ new node ให้ชี้ไปที่ node ต่อไป
    NewNode.next = self.head
    self.head = NewNode

  # เพิ่ม node ที่จุดสุดท้าย
  def AtEnd(self, newdata):
    NewNode = Node(newdata)
    # ถ้า Linked List ไม่มี head เลย (ว่าง)
    if self.head is None:
      self.head = NewNode
      return
    
    last = self.head
    # วนลูปหา last
    while(last.next):
      last = last.next
    last.next = NewNode

  def InBetween(self, middle_node, newdata):
    if middle_node is None:
      print("Need Middle Node")
      return
    
    NewNode = Node(newdata)
    NewNode.next = middle_node.next
    middle_node.next = NewNode

  def RemoveNode(self, Removekey):
    HeadVal = self.head
    
    if(HeadVal is not None):
      if(HeadVal.data == Removekey):
        self.head = HeadVal.next
        HeadVal = None
        return

    while(HeadVal is not None):
      if HeadVal.data == Removekey:
        break
      prev = HeadVal
      HeadVal = HeadVal.next
    
    if(HeadVal == None):
      return
    
    prev.next = HeadVal.next
    
    HeadVal = None



list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# next node1 ชี้ไป node2
list1.head.next = e2
# next node2 ชี้ไป node3
e2.next = e3

list1.AtBegining("Sun")
list1.AtEnd("Thu")
list1.InBetween(list1.head.next.next.next, "Fri")
list1.RemoveNode("Sun")

list1.listprint()