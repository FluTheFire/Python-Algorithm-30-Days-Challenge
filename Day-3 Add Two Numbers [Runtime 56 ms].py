class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        
        # ใส่ head เพื่อที่จะให้ return ค่าออกมาเป็นตัวแรก 
        # ถ้า return เป็น cur เลยจะไม่เป็นตัวแรก เพราะถูกทำให้ .next แล้ว
        head = cur = ListNode(0)
        carry=0
        
        # while loop เมื่อเป็น None หรือ 0 จะไม่ run ต่อ
        while l1 or l2 or carry:
            if l1:
                # เอาค่า val l1 นั้นๆ
                carry += l1.val
                l1=l1.next
            
            if l2:
                # เอาค่า val l2 นั้นๆ
                carry += l2.val
                l2=l2.next
            # เพิ่ม ListNode
            cur.next=ListNode(carry%10) # %10 เพื่อเอาเลขหลักเดียว เช่นถ้าได้ 12 ก็เอาแค่ 2 มาใส่ในหลักนี้
            # set ให้รองรับ ListNode อันต่อไป
            cur=cur.next
            # เช็คว่า ต้องทดเลขหลักในต่อไปไหม
            # เช่นถ้าได้ 12 หาร10 ก็จะเหลือ 1 เป็นเลขเอาไว้ทดหลักต่อไป 
            carry = carry//10
        # ใส่ .next เพราะว่า val headอันแรก setไว้เป็น 0 เพื่อให้ cur,head ได้ยืนยันการเป็นtype class ListNode 
        return head.next
            
# วิธีประกาศ ListNode
# Linked-List -> class(val, class(val, class(val, None)))
# [ class in class in class ]
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

print(Solution().addTwoNumbers(l1, l2))
#Solution().addTwoNumbers(l1, l2)
