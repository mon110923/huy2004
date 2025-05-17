# Tên file: filter_numbers.py

def filter_list(input_list):
    """
    Hàm lọc các số nguyên từ một danh sách hỗn hợp
    
    Tham số:
    input_list - Danh sách đầu vào chứa số và chuỗi
    
    Trả về:
    Danh sách chỉ chứa các số nguyên
    """
    # Khởi tạo danh sách rỗng để lưu các số
    result = []
    
    # Duyệt qua từng phần tử trong danh sách
    for item in input_list:
        # Kiểm tra nếu phần tử là số nguyên
        if isinstance(item, int):
            # Thêm số nguyên vào danh sách kết quả
            result.append(item)
    
    # Trả về danh sách các số
    return result

# Phần kiểm tra và chạy chương trình
def main():
    # Các ví dụ kiểm tra
    test_cases = [
        [1, 2, 'a', 'b'],
        [1, 'a', 'b', 0, 15],
        [1, 2, 'aasf', '1', '123', 123]
    ]
    
    # Chạy và in kết quả từng test case
    for case in test_cases:
        print(f"Đầu vào: {case}")
        print(f"Kết quả: {filter_list(case)}\n")

# Kiểm tra xem file có đang được chạy trực tiếp không
if __name__ == "__main__":
    main()
