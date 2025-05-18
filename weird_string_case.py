def to_weird_case(string):
    # Tạo danh sách các từ từ chuỗi
    words = string.split()
    
    # Danh sách để lưu các từ đã chuyển đổi
    result = []
    
    # Duyệt qua từng từ
    for word in words:
        # Biến để lưu từ đã chuyển đổi
        weird_word = ''
        
        # Duyệt qua từng ký tự trong từ
        for i in range(len(word)):
            # Nếu chỉ số chẵn (0, 2, 4...) thì viết hoa
            if i % 2 == 0:
                weird_word += word[i].upper()
            # Nếu chỉ số lẻ (1, 3, 5...) thì viết thường
            else:
                weird_word += word[i].lower()
        
        # Thêm từ đã chuyển đổi vào danh sách kết quả
        result.append(weird_word)
    
    # Nối các từ lại thành chuỗi
    return ' '.join(result)

# Kiểm tra
print(to_weird_case("String"))  # StRiNg
print(to_weird_case("Weird string case"))  # WeIrD StRiNg CaSe

# Chạy hàm kiểm tra nếu được chạy trực tiếp
if __name__ == "__main__":
    # Loại bỏ `main()` vì không có hàm main được định nghĩa
    pass  # hoặc bạn có thể thêm các lệnh kiểm tra trực tiếp ở đây
