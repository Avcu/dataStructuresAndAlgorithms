# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            my_node = TreeNode(val=nums[0])
            return my_node
        else:
            mid_point = len(nums)//2
            my_node = TreeNode(val=nums[mid_point])
            my_node.left = self.sortedArrayToBST(nums[:mid_point])
            my_node.right = self.sortedArrayToBST(nums[mid_point+1:])
            return my_node