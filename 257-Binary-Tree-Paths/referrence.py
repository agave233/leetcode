# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#变态python
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]

# 因为 node和pre是绑定的 所以其实bfs和dfs，处理顺序 没有区别
# bfs + queue
class Solution1(object):
    def binaryTreePaths(self, root):
        res = [] 
        
        if root: 
            queue = collections.deque([(root, str(root.val))])
            while queue: 
                node, pre = queue.popleft()
                if node.left: 
                    queue.append((node.left, '{}->{}'.format(pre, node.left.val)))
                if node.right: 
                    queue.append((node.right, '{}->{}'.format(pre, node.right.val)))
                if not node.left and not node.right: 
                    res.append(pre)
        
        return res

# dfs + stack
class Solution1(object):
    def binaryTreePaths(self, root):
        res = [] 
        
        if root: 
            stack = [(root, str(root.val))]
            while stack: 
                node, pre = stack.pop()
                if node.left: 
                    stack.append((node.left, '{}->{}'.format(pre, node.left.val)))
                if node.right: 
                    stack.append((node.right, '{}->{}'.format(pre, node.right.val)))
                if not node.left and not node.right: 
                    res.append(pre)
        
        return res
        
# recusive
class Solution2(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        self.res = []
        if root:
            self.helper(root, str(root.val))
            
        return self.res
    
    def helper(self, node, pre):
        if node.left: 
            self.helper(node.left, '{}->{}'.format(pre, node.left.val))
        if node.right: 
            self.helper(node.right, '{}->{}'.format(pre, node.right.val))
        if not node.left and not node.right:
            self.res.append(pre)