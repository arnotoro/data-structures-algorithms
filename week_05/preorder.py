# A O(n^2) Python3 program for
# construction of BST from preorder traversal

# A binary tree node


class Node():

	# A constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# constructTreeUtil.preIndex is a static variable of
# function constructTreeUtil

# Function to get the value of static variable
# constructTreeUtil.preIndex
def getPreIndex():
	return constructTreeUtil.preIndex

# Function to increment the value of static variable
# constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1

# A recursive function to construct Full from pre[].
# preIndex is used to keep track of index in pre[[].


def constructTreeUtil(pre, low, high):

		# Base Case
	if(low > high):
		return None

	# The first node in preorder traversal is root. So take
	# the node at preIndex from pre[] and make it root,
	# and increment preIndex
	root = Node(pre[getPreIndex()])
	incrementPreIndex()

	# If the current subarray has only one element,
	# no need to recur
	if low == high:
		return root

	r_root = -1

	# Search for the first element greater than root
	for i in range(low, high+1):
		if (pre[i] > root.data):
			r_root = i
			break

	# If no elements are greater than the current root,
	# all elements are left children
	# so assign root appropriately
	if r_root == -1:
		r_root = getPreIndex() + (high - low)

	# Use the index of element found in preorder to divide
	# preorder array in two parts. Left subtree and right
	# subtree
	root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)

	root.right = constructTreeUtil(pre, r_root, high)

	return root

# The main function to construct BST from given preorder
# traversal. This function mainly uses constructTreeUtil()


def constructTree(pre):
	size = len(pre)
	constructTreeUtil.preIndex = 0
	return constructTreeUtil(pre, 0, size-1)


def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.data, end=' ')
	printInorder(root.right)


# Driver code
if __name__ == '__main__':
    pre = [1, 2, 4, 3, 5, 7, 6, 8, 9]


    root = constructTree(pre)

    printInorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) and Rhys Compton
