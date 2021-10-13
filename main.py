class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## PRE ORDER TRAVERSAL
# Implementation using stacks
def preorderTraversal(root):

    if root is None:
        return []
    stack = [root]
    out = []

    while stack:
        node = stack.pop()
        if node:
            out.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    stack.append(child)
    return out


# Implementation using recursion
def preorderTraversalrec(root):
    if root is None:
        return []

    out = [root.val]
    out += preorderTraversalrec(root.left)
    out += preorderTraversalrec(root.right)

    return out

## IN ORDER TRAVERSAL

# Implementation using stacks
def inorderTraversal(root):
    if root is None:
        return []

    node = root
    stack = []
    out = []

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out

# Implementation using recursion
def inorderTraversalrec(root):
    if root is None:
        return []

    out = inorderTraversalrec(root.left)
    out += [root.val]
    out += inorderTraversalrec(root.right)

    return out

## POST ORDER TRAVERSAL
# Implementation using stacks
def postorderTraversal(root):

    if root is None:
        return []

    stack = []
    node = root
    out = []

    while True:
        while node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left

        node = stack.pop()

        if node.right and stack and node.right == stack[-1]:
            r = stack.pop()
            stack.append(node)
            node = r
        else:
            out.append(node.val)
            node = None

        if not stack:
            break
    return out


# Implementation using recursion
def postorderTraversalrec(root):
    if root is None:
        return []

    out = postorderTraversalrec(root.left)
    out += postorderTraversalrec(root.right)
    out += [root.val]

    return out




c = TreeNode('c')
d = TreeNode('d')
b = TreeNode('b', left=c, right=d)

h = TreeNode('h')
i = TreeNode('i')
g = TreeNode('g', left=h, right=i)

f = TreeNode('f')
e = TreeNode('e', left=f, right=g)

a = TreeNode('a', left=b, right=e)

print(preorderTraversal(a))
print(preorderTraversalrec(a))
print("\n \n")
print(inorderTraversal(a))
print(inorderTraversalrec(a))
print("\n \n")
print(postorderTraversal(a))
print(postorderTraversalrec(a))
