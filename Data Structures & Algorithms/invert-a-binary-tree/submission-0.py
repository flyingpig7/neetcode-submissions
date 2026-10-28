# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def voidInvert(self, root: Optional[TreeNode]):
        curr = root
        if not curr:
            return
        else:
            left = curr.left
            curr.left = curr.right
            curr.right = left
            self.voidInvert(curr.left)
            self.voidInvert(curr.right)
            
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.voidInvert(root)
        return root
        
        