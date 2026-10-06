class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # If this is a leaf node
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Subtract current value and check both sides
        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))