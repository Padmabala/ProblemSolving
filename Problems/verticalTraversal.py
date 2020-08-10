class Solution:
    def traverse(node, v, h, l, i):
        if node is none:
            return
        self.verticalTraversal(root.left, v - 1, h, l, i)
        if v not in h:
            h[v] = i
            l[h[v]] = []
            l[h[v]].append(root.val)
            i += 1
        self.verticalTraversal(root.right, v + 1, h, l, i)
        if v not in h:
            h[v] = i
            l[h[v]] = []
            l[h[v]].append(root.val)
            i += 1

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        h = {}
        l = []
        self.traverse(root, 0, h, l, 0)
s=Solution()
s.verticalTraversal()