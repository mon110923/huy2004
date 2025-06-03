def solve(board):
    # Tìm ô trống với ít khả năng nhất
    def find_most_constrained_cell(board):
        min_options = 10
        cell = None
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    options = get_possible_values(board, r, c)
                    if len(options) < min_options:
                        min_options = len(options)
                        cell = (r, c)
        return cell

    # Lấy các giá trị có thể cho ô
    def get_possible_values(board, row, col):
        used = set()
        
        # Kiểm tra hàng
        used.update(board[row])
        
        # Kiểm tra cột
        for r in range(9):
            used.add(board[r][col])
        
        # Kiểm tra ô 3x3
        box_r, box_c = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                used.add(board[box_r + i][box_c + j])
        
        # Loại bỏ số 0 (ô trống)
        used.discard(0)
        
        # Trả về các số chưa được sử dụng
        return [num for num in range(1, 10) if num not in used]

    # Giải Sudoku với backtracking nâng cao
    def backtrack(board):
        # Tìm ô trống với ít khả năng nhất
        cell = find_most_constrained_cell(board)
        
        # Nếu không còn ô trống, đã giải xong
        if not cell:
            return board
        
        row, col = cell
        
        # Lấy các giá trị có thể
        possible_values = get_possible_values(board, row, col)
        
        # Thử các giá trị có thể
        for num in possible_values:
            board[row][col] = num
            
            # Đệ quy
            result = backtrack(board)
            if result:
                return result
            
            # Quay lui
            board[row][col] = 0
        
        return None

    # Tạo bản sao của bảng để không thay đổi bảng gốc
    board_copy = [row[:] for row in board]
    return backtrack(board_copy)

# Hàm in bảng Sudoku
def print_board(board):
    for row in board:
        print(row)

# Hàm kiểm tra tính hợp lệ của bảng Sudoku
def is_valid_solution(board):
    # Kiểm tra hàng
    for row in board:
        if len(set(row)) != 9 or 0 in row:
            return False
    
    # Kiểm tra cột
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9 or 0 in column:
            return False
    
    # Kiểm tra ô 3x3
    for box_r in range(0, 9, 3):
        for box_c in range(0, 9, 3):
            box = [board[box_r + i][box_c + j] 
                   for i in range(3) 
                   for j in range(3)]
            if len(set(box)) != 9 or 0 in box:
                return False
    
    return True

# Ví dụ sử dụng
def main():
    # Bảng Sudoku mẫu
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

    print("Bảng ban đầu:")
    print_board(puzzle)
    
    # Giải Sudoku
    solution = solve(puzzle)
    
    # In kết quả
    if solution:
        print("\nGiải pháp:")
        print_board(solution)
        
        # Kiểm tra tính hợp lệ
        if is_valid_solution(solution):
            print("\nGiải pháp hợp lệ!")
        else:
            print("\nGiải pháp KHÔNG hợp lệ!")
    else:
        print("Không tìm được giải pháp")

# Chạy chương trình
if __name__ == "__main__":
    main()
