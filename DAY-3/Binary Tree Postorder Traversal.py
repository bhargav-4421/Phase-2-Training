class Solution(object):
    def postorderTraversal(self, root):

        res = []

        def postorder(node):
            if node:
               
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)
        postorder(root)
        return res
        
