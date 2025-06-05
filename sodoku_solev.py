def sudoku(puzzle):
    def is_valid(board, row, col, num):
        # Kiểm tra hàng
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Kiểm tra cột
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Kiểm tra ô 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True

    def solve(board):
        # Tìm ô trống
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    # Thử các số từ 1 đến 9
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            # Thử số này
                            board[row][col] = num
                            
                            # Đệ quy để giải tiếp
                            if solve(board):
                                return True
                            
                            # Nếu không được, quay lui
                            board[row][col] = 0
                    
                    # Nếu không tìm được số nào phù hợp
                    return False
        
        # Nếu không còn ô trống
        return True

    # Sao chép bảng để không thay đổi bảng gốc
    board = [row[:] for row in puzzle]
    
    # Giải Sudoku
    solve(board)
    
    return board

# Hàm in bảng Sudoku đẹp hơn
def print_sudoku(board):
    for i, row in enumerate(board):
        # In dòng phân cách sau mỗi 3 hàng
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        
        # In các số trong hàng
        for j, num in enumerate(row):
            # In dấu | sau mỗi 3 cột
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num, end=" ")
        print()  # Xuống dòng

# Test hàm
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# In bảng gốc
print("Bảng Sudoku ban đầu:")
print_sudoku(puzzle)

# Giải và in kết quả
print("\nBảng Sudoku sau khi giải:")
result = sudoku(puzzle)
print_sudoku(result)
