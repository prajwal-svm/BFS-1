# 102. Binary Tree Level Order Traversal

# Time Complexity: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Intuition:
# Use a queue to store the nodes in the BST.
# Use a dfs function to traverse the BST and push the nodes onto the queue.
# Use the next function to return the next smallest element in the BST.
# Use the hasNext function to check if there is a next smallest element in the BST.

# BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.dfs(root, 0, result)
        return result
    
    def dfs(self, root, level, result):
        if not root:
            return
        if len(result) == level:
            result.append([])   
        result[level].append(root.val)
        self.dfs(root.left, level + 1, result)
        self.dfs(root.right, level + 1, result)

