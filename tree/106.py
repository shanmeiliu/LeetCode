# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder or len(inorder)!= len(postorder):
            return None
        root=TreeNode(postorder[-1])
        rootind=inorder.index(postorder[-1])        
        
        def dfs(pos, inor):
            if len(pos)==0:
                return None
            root=TreeNode(pos[-1])
            ind=inor.index(pos[-1])
            root.left=dfs(pos[0:ind],inor[0:ind])
            root.right=dfs(pos[ind:-1],inor[ind+1:])
            return root
        
            
        root.left=dfs(postorder[0:rootind],inorder[0:rootind])
        root.right=dfs(postorder[rootind:-1],inorder[rootind+1:])
        return root
