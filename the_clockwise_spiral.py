def createSpiral(N):
    # Kiểm tra đầu vào
    if not isinstance(N, int) or N < 1:
        return []
    
    # Khởi tạo ma trận và các biến điều khiển
    matrix = [[0] * N for _ in range(N)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, direction = 0, 0, 0
    
    # Điền số từ 1 đến N^2
    for num in range(1, N*N + 1):
        matrix[x][y] = num
        
        # Thử di chuyển
        nx, ny = x + dx[direction], y + dy[direction]
        
        # Đổi hướng nếu ra ngoài hoặc ô đã điền
        if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny]:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
        
        x, y = nx, ny
    
    return matrix

# Test cases
print(createSpiral(3))
print(createSpiral(4))
print(createSpiral(5))