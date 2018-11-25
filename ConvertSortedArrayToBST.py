# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, left_ind, right_ind):
            if left_ind > right_ind:
                return None
            if left_ind == right_ind:
                return TreeNode(nums[left_ind])
            mid = left_ind + (right_ind - left_ind) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, left_ind, mid -1)
            root.right = helper(nums, mid+1, right_ind)
            
            return root
        return helper(nums, 0, len(nums)-1)
            
