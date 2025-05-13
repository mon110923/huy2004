# Hàm chuyển đổi số sang nhị phân
def decimal_to_binary(decimal_num):
    """
    Chuyển đổi số thập phân sang nhị phân
    
    Tham số:
    decimal_num (int): Số thập phân cần chuyển đổi
    
    Trả về:
    str: Chuỗi nhị phân
    """
    # Nếu số là 0, trả về "0"
    if decimal_num == 0:
        return "0"
    
    # Danh sách lưu các chữ số nhị phân
    binary_digits = []
    
    # Quá trình chuyển đổi
    while decimal_num > 0:
        # Lấy số dư khi chia cho 2 (0 hoặc 1)
        remainder = decimal_num % 2
        
        # Thêm số dư vào đầu danh sách
        binary_digits.insert(0, str(remainder))
        
        # Chia số cho 2 để tiếp tục chuyển đổi
        decimal_num //= 2
    
    # Ghép các chữ số thành chuỗi
    return ''.join(binary_digits)

# Hàm chính để cộng và chuyển sang nhị phân
def add_binary(num1, num2):
    """
    Cộng hai số và trả về kết quả dưới dạng nhị phân
    
    Tham số:
    num1 (int): Số thứ nhất
    num2 (int): Số thứ hai
    
    Trả về:
    str: Tổng hai số ở dạng nhị phân
    """
    # Bước 1: Cộng hai số
    total = num1 + num2
    
    # Bước 2: Chuyển tổng sang nhị phân
    binary_result = decimal_to_binary(total)
    
    return binary_result

# Phần kiểm tra và chạy chương trình
def main():
    """
    Hàm chính để kiểm tra chức năng
    """
    # Các test case
    test_cases = [
        (1, 1),    # 1 + 1
        (5, 9),    # 5 + 9
        (10, 20),  # 10 + 20
        (0, 0)     # Trường hợp đặc biệt
    ]
    
    # Chạy và in kết quả các test case
    print("Kiểm tra chức năng chuyển đổi và cộng nhị phân:")
    for a, b in test_cases:
        result = add_binary(a, b)
        print(f"{a} + {b} = {result} (nhị phân)")

# Kiểm tra xem file có đang chạy trực tiếp không
if __name__ == "__main__":
    main()
