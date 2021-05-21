class Queue:
  def __init__(self):
    self.queue = list()
  
  def add(self, dataval):
    if dataval not in self.queue:
      self.queue.insert(0, dataval)
      return True
    return False
  
  def size(self):
    return len(self.queue)

  def dequeue(self):
    if len(self.queue) > 0:
      return self.queue.pop()
    return ("No elements in Queue!")

TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Thu")
TheQueue.add("Wed")
print(TheQueue.size())
print(TheQueue.dequeue())
print(TheQueue.size())
