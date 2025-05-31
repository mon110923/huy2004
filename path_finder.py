from heapq import heappush, heappop

def path_finder(area_map):
    # Chuyển map thành ma trận độ cao
    heights = [list(map(int, list(row))) for row in area_map.split('\n')]
    N = len(heights)
    
    # Các hướng di chuyển
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # Khởi tạo
    heap = [(0, 0, 0)]  # (climb_rounds, x, y)
    visited = set()
    
    while heap:
        climb_rounds, x, y = heappop(heap)
        
        # Đã đến đích
        if x == N-1 and y == N-1:
            return climb_rounds
        
        # Bỏ qua nếu đã thăm
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Thử các hướng di chuyển
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Kiểm tra trong biên
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                # Tính climb rounds
                rounds = abs(heights[nx][ny] - heights[x][y])
                heappush(heap, (climb_rounds + rounds, nx, ny))
    
    return -1  # Không tìm được đường

def main():
    # Test case 1
    map1 = """012
345
678"""
    print("Test case 1:")
    print(path_finder(map1))  # Kỳ vọng: 2
    
    # Test case 2
    map2 = """000
999
999"""
    print("\nTest case 2:")
    print(path_finder(map2))  # Kỳ vọng: 18
    
    # Test case 3
    map3 = """010
101
010"""
    print("\nTest case 3:")
    print(path_finder(map3))  # Kỳ vọng: 4
    
    # Test case 4 - Map lớn hơn
    map4 = """01234
56789
01234
56789
01234"""
    print("\nTest case 4:")
    print(path_finder(map4))  # Kết quả sẽ khác nhau

if __name__ == "__main__":
    main()
