class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root.val==p.val or root.val==q.val:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left is None and right is None:
            return None
        if left is None:
            return right
        if right is None:
            return left
        return root
