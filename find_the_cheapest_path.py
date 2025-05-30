# file: cheapest_path.py
from typing import List, Tuple
from heapq import heappush, heappop

def cheapest_path(t: List[List[int]], start: Tuple[int, int], finish: Tuple[int, int]) -> List[str]:
    """
    Tìm đường đi có chi phí thấp nhất trong ma trận chi phí.
    
    Args:
    - t: Ma trận chi phí
    - start: Tọa độ bắt đầu
    - finish: Tọa độ kết thúc
    
    Returns:
    - Danh sách các hướng di chuyển
    """
    # Các hướng di chuyển: lên, xuống, trái, phải
    directions = [
        (-1, 0, "up"),
        (1, 0, "down"),
        (0, -1, "left"), 
        (0, 1, "right")
    ]
    
    rows, cols = len(t), len(t[0])
    
    # Khởi tạo các tập để theo dõi
    visited = set()
    # Heap lưu (chi phí, x, y, đường đi)
    heap = [(0, start[0], start[1], [])]
    
    while heap:
        cost, x, y, path = heappop(heap)
        
        # Đã đến đích
        if (x, y) == finish:
            return path
        
        # Bỏ qua nếu đã duyệt điểm này
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Thử các hướng di chuyển
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            
            # Kiểm tra điểm mới có hợp lệ không
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = cost + t[nx][ny]
                new_path = path + [direction]
                heappush(heap, (new_cost, nx, ny, new_path))
    
    # Không tìm thấy đường đi
    return []

# Các test cases
def test_cheapest_path():
    # Test case 1: Ví dụ cơ bản
    t1 = [
        [1, 9, 1],
        [2, 9, 1],
        [2, 1, 1]
    ]
    start1 = (0, 0)
    finish1 = (0, 2)
    result1 = cheapest_path(t1, start1, finish1)
    print("Test case 1:")
    print("Input:", t1)
    print("Start:", start1)
    print("Finish:", finish1)
    print("Result:", result1)
    print()

    # Test case 2: Ma trận phức tạp hơn
    t2 = [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 3, 2, 3],
        [1, 4, 3, 2]
    ]
    start2 = (0, 0)
    finish2 = (3, 3)
    result2 = cheapest_path(t2, start2, finish2)
    print("Test case 2:")
    print("Input:", t2)
    print("Start:", start2)
    print("Finish:", finish2)
    print("Result:", result2)
    print()

    # Test case 3: Không có đường đi
    t3 = [
        [float('inf'), float('inf')],
        [float('inf'), float('inf')]
    ]
    start3 = (0, 0)
    finish3 = (1, 1)
    result3 = cheapest_path(t3, start3, finish3)
    print("Test case 3:")
    print("Input:", t3)
    print("Start:", start3)
    print("Finish:", finish3)
    print("Result:", result3)

# Hàm main để chạy chương trình
def main():
    print("Bắt đầu kiểm tra cheapest_path...")
    test_cheapest_path()

# Kiểm tra nếu file được chạy trực tiếp
if __name__ == "__main__":
    main()
