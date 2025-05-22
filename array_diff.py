def array_diff(a, b):
    """
    Loại bỏ các phần tử của list a có trong list b
    
    :param a: Danh sách đầu vào
    :param b: Danh sách các phần tử cần loại bỏ
    :return: Danh sách mới sau khi loại bỏ
    """
    return [x for x in a if x not in b]

# Hàm kiểm tra với nhiều test case
def test_array_diff():
    # Test case 1: Loại bỏ phần tử đơn giản
    print("Test 1:", array_diff([1, 2], [1]))  # [2]
    
    # Test case 2: Loại bỏ phần tử lặp
    print("Test 2:", array_diff([1, 2, 2, 2, 3], [2]))  # [1, 3]
    
    # Test case 3: Danh sách rỗng
    print("Test 3:", array_diff([], [1, 2, 3]))  # []
    
    # Test case 4: Không có phần tử nào bị loại bỏ
    print("Test 4:", array_diff([1, 2, 3], [4, 5]))  # [1, 2, 3]

# Chạy test khi file được chạy trực tiếp
if __name__ == "__main__":
    test_array_diff()
