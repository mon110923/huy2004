from collections import deque

# Định nghĩa lớp Node
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

# Hàm duyệt cây theo mức
def tree_by_levels(node):
    if not node:
        return []
    
    queue = deque([node])
    result = []
    
    while queue:
        curr = queue.popleft()
        result.append(curr.value)
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    return result

# Hàm main để kiểm tra
def main():
    # Ví dụ 1: Cây đầy đủ
    # Cấu trúc cây:
    #        2
    #     /     \
    #    8       9
    #   / \     / \
    #  1   3   4   5
    root1 = Node(None, None, 2)
    root1.left = Node(None, None, 8)
    root1.right = Node(None, None, 9)
    root1.left.left = Node(None, None, 1)
    root1.left.right = Node(None, None, 3)
    root1.right.left = Node(None, None, 4)
    root1.right.right = Node(None, None, 5)
    
    print("Ví dụ 1 - Duyệt cây theo mức:")
    print(tree_by_levels(root1))
    
    # Ví dụ 2: Cây không đầy đủ
    # Cấu trúc cây:
    #        1
    #     /     \
    #    8       4
    #     \       \
    #      3       5
    #               \
    #                7
    root2 = Node(None, None, 1)
    root2.left = Node(None, None, 8)
    root2.right = Node(None, None, 4)
    root2.left.right = Node(None, None, 3)
    root2.right.right = Node(None, None, 5)
    root2.right.right.right = Node(None, None, 7)
    
    print("\nVí dụ 2 - Duyệt cây theo mức:")
    print(tree_by_levels(root2))
    
    # Ví dụ 3: Cây rỗng
    root3 = None
    print("\nVí dụ 3 - Cây rỗng:")
    print(tree_by_levels(root3))

# Kiểm tra nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
