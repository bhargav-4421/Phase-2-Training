class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        queue=[root]
        res=[]
        while queue:
            sublist=[]
            for i in range(len(queue)):
                cur=queue.pop(0)
                sublist.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(sublist)
        return res
