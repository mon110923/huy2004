import heapq
import random

def volume(heightmap):
    # Kiểm tra đầu vào rỗng hoặc không hợp lệ
    if not heightmap or len(heightmap) == 0 or len(heightmap[0]) == 0:
        return 0
    
    # Chuyển đổi sang list nếu là NumPy array hoặc array-like
    try:
        rows = len(heightmap)
        cols = len(heightmap[0])
        heightmap = [list(row) for row in heightmap]
    except TypeError:
        heightmap = list(map(list, heightmap))
    
    # Khởi tạo các biến để theo dõi
    visited = [[False] * cols for _ in range(rows)]
    water = 0
    heap = []
    
    # Thêm các ô biên vào hàng đợi ưu tiên
    for r in range(rows):
        heapq.heappush(heap, (heightmap[r][0], r, 0))
        heapq.heappush(heap, (heightmap[r][cols-1], r, cols-1))
        visited[r][0] = True
        visited[r][cols-1] = True
    
    for c in range(1, cols-1):
        heapq.heappush(heap, (heightmap[0][c], 0, c))
        heapq.heappush(heap, (heightmap[rows-1][c], rows-1, c))
        visited[0][c] = True
        visited[rows-1][c] = True
    
    # Các hướng di chuyển
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # Biến theo dõi chiều cao biên tối đa
    max_height = float('-inf')
    
    # Xử lý các ô từ thấp đến cao
    while heap:
        height, r, c = heapq.heappop(heap)
        max_height = max(max_height, height)
        
        # Kiểm tra các ô lân cận
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Kiểm tra ô mới có hợp lệ không
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                
                # Nếu ô thấp hơn chiều cao biên, nó có thể chứa nước
                if heightmap[nr][nc] < max_height:
                    water += max_height - heightmap[nr][nc]
                
                # Thêm ô vào hàng đợi
                heapq.heappush(heap, (heightmap[nr][nc], nr, nc))
    
    return water

# Hàm tạo bản đồ độ cao ngẫu nhiên
def generate_random_heightmap(rows, cols, min_height=0, max_height=10):
    return [[random.randint(min_height, max_height) for _ in range(cols)] for _ in range(rows)]

# Hàm main để kiểm tra
def main():
    # Tạo bản đồ độ cao 50x50
    heightmap = generate_random_heightmap(50, 50)
    
    # In ra một phần của bản đồ độ cao
    print("Một phần của bản đồ độ cao:")
    for row in heightmap[:5]:
        print(row)
    
    # Tính toán lượng nước
    water_volume = volume(heightmap)
    print(f"\nTổng lượng nước: {water_volume}")

# Chạy hàm main nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
