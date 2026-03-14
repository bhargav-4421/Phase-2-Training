class Solution(object):
    def min(self ,root):
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root, data):
        if root is None:
            return None

        if data < root.val:
            root.left = self.deleteNode(root.left ,data)
        elif data >root.val:
            root.right = self.deleteNode(root.right ,data)
        else:

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.min(root.right)
            root.val = temp
            root.right = self.deleteNode(root.right ,temp)
        return root
