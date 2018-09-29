# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n=len(preorder)
        m=len(inorder)
        if m!=n or n==0:
            return None
        root=TreeNode(preorder[0])
        rootind=inorder.index(preorder[0])

       
        
        def dfs(pre, inor):
            if len(pre)==0:
                return None
            root=TreeNode(pre[0])
            ind=inor.index(pre[0])
            root.left=dfs(pre[1:ind+1],inor[0:ind])
            root.right=dfs(pre[ind+1:],inor[ind+1:])
            return root
        
            
        root.left=dfs(preorder[1:rootind+1],inorder[0:rootind])
        root.right=dfs(preorder[rootind+1:],inorder[rootind+1:])
        return root
