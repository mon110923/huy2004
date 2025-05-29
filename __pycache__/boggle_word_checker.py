def find_word(board, word):
    """
    Tìm kiếm từ trong bảng Boggle
    
    :param board: Ma trận ký tự 2D
    :param word: Từ cần tìm
    :return: True nếu tìm thấy từ, False nếu không
    """
    # Kiểm tra đầu vào rỗng
    if not board or not word:
        return False
    
    # Kích thước bảng
    rows, cols = len(board), len(board[0])
    
    def dfs(row, col, index):
        """
        Thuật toán tìm kiếm theo chiều sâu
        
        :param row: Vị trí hàng hiện tại
        :param col: Vị trí cột hiện tại
        :param index: Chỉ số ký tự trong từ
        :return: True nếu tìm thấy từ
        """
        # Điều kiện dừng và kiểm tra tính hợp lệ
        if (
            # Đã tìm thấy toàn bộ từ
            index == len(word) or 
            # Ngoài biên bảng
            row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            # Ký tự không khớp
            board[row][col] != word[index]
        ):
            # Trả về True nếu đã tìm thấy toàn bộ từ
            return index == len(word)
        
        # Lưu ký tự hiện tại và đánh dấu đã thăm
        temp = board[row][col]
        board[row][col] = '#'  # Ký hiệu đã thăm
        
        # Các hướng di chuyển (8 hướng)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Hàng trên
            (0, -1),           (0, 1),    # Hàng ngang
            (1, -1), (1, 0),   (1, 1)     # Hàng dưới
        ]
        
        # Kiểm tra các hướng
        found = any(
            dfs(row + dx, col + dy, index + 1) 
            for dx, dy in directions
        )
        
        # Khôi phục lại ký tự
        board[row][col] = temp
        
        return found
    
    # Thử tìm kiếm từ mọi ô trong bảng
    return any(
        dfs(r, c, 0) 
        for r in range(rows) 
        for c in range(cols)
    )

# Hàm main để kiểm tra
def main():
    # Bảng Boggle mẫu
    board = [
        ["I", "L", "A", "W"],
        ["B", "N", "G", "E"],
        ["I", "U", "A", "O"],
        ["A", "S", "R", "L"]
    ]
    
    # Danh sách từ kiểm tra
    test_words = [
        "BINGO",    # Có trong bảng
        "LINGO",    # Có trong bảng
        "BUNGIE",   # Không có trong bảng
        "BINS",     # Không có trong bảng
        "ILNBIA"    # Có trong bảng
    ]
    
    # In kết quả
    print("Kết quả tìm kiếm từ:")
    for word in test_words:
        result = find_word(board, word)
        print(f"{word}: {result}")

# Chạy chương trình
if __name__ == "__main__":
    main()
