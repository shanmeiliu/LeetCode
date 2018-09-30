class Solution:
    """
    Iteration

    T: O(n), n == the number of total nodes
    S: O(k), k == the maximum tree height

    - preorder to create node, inorder to maintain order
    - there are 3 ways to iterate list by order:
      1. iter()
      2. reverse() and pop() in every level
      3. global i and increase it after access
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        stack = [root]
        i = 0

        for val in preorder[1:]:
            parent = stack[-1]

            if parent.val != inorder[i]:
                parent.left = TreeNode(val)
                stack.append(parent.left)
            else:
                while stack and stack[-1].val == inorder[i]:
                    parent = stack.pop()
                    i += 1

                parent.right = TreeNode(val)
                stack.append(parent.right)

        return root
