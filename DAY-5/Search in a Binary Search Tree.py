class Solution(object):
    def searchBST(self, root, val):
        res=[]
        if root is None:
            return None
        if root.val== val:
            return root
        if val <root.val:
            return self.searchBST(root.left,val)
        return self.searchBST(root.right,val)
        
