#My Soluton below..scroll to see even simpler ones
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        index=1
        if(head==None):
            return None
        temp=head
        evenHead=head.next
        while(True):
            if (temp.next == None and index%2==0):
                prev.next = evenHead
                break
            elif (temp.next == None and index%2!=0):
                temp.next = evenHead
                break
            nextNode=temp.next
            temp.next=nextNode.next
            prev=temp
            temp=nextNode
            index+=1
            if(index==2):
                temp=evenHead
        # temp=head
        # while(temp!=None):
        #     print(temp.val)
        #     temp=temp.next
        return head



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         odds = ListNode(0)
#         evens = ListNode(0)
#
#         oddHead = odds
#         evenHead = evens
#
#         length = 1
#
#         while head:
#             if length % 2 == 0:
#                 evens.next = head
#                 evens = evens.next
#             else:
#                 odds.next = head
#                 odds = odds.next
#
#             length += 1
#             head = head.next
#
#         # need to cut the end of the lists
#         odds.next = None
#         evens.next = None
#
#         if odds:
#             odds.next = evenHead.next
#             return oddHead.next
#         else:
#             return evenHead.next


# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         ans = head
#         odd, even, d_o, d_e = head, head.next, head, head.next
#         while d_o or d_e:
#             if d_o:
#                 if d_o.next:
#                     d_o.next = d_o.next.next
#                     d_o = d_o.next
#                 else:
#                     d_o = None
#             if d_e:
#                 if d_e.next:
#                     d_e.next = d_e.next.next
#                     d_e = d_e.next
#                 else:
#                     d_e = None
#
#         while odd.next:
#             odd = odd.next
#
#         odd.next = even
#
#         return ans


