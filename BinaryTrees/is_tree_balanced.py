import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


node3_1 = BinaryTreeNode(6)
node3_2 = BinaryTreeNode(7)
node3_3 = BinaryTreeNode(8)
node3_4 = BinaryTreeNode(9)

node2_1 = BinaryTreeNode(4, node3_1, node3_2)
node2_2 = BinaryTreeNode(5, node3_3, node3_4)

node1_1 = BinaryTreeNode(2, node2_1, node2_2)
node1_2 = BinaryTreeNode(3)

rootNode = BinaryTreeNode(0, node1_1, node1_2)

result = is_balanced_binary_tree(rootNode)
print(result)
