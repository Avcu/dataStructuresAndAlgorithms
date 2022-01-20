## Similar to the merge sort, lists of similar sizes are merged two by two until we have only one list. 
## This reduces the runtime complexity from O(KN) to O(log(k)N).

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = ListNode(val=-1)
        ite_node = root
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                new_node = ListNode(val=list1.val)
                ite_node.next = new_node
                ite_node = new_node
                list1 = list1.next
            else:
                new_node = ListNode(val=list2.val)
                ite_node.next = new_node
                ite_node = new_node
                list2 = list2.next                
        
        if list1 is None:
            ite_node.next = list2
        else:
            ite_node.next = list1
        return root.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # delete the empty lists
        idx = 0
        while idx < len(lists):
            if lists[idx] == None:
                lists.pop(idx)
            else:
                idx += 1
        if len(lists) == 0:
            return None
        
        # merge the lists two by two
        while len(lists) > 1:
            new_list = self.mergeTwoLists(lists[-1], lists[-2])
            lists.pop(-1)
            lists.pop(-1)
            lists.insert(0, new_list)
        
        return lists[0]