def decompose(n):
    def decompose_recursive(target, current_max):
        # Nếu target trở thành 0, nghĩa là chúng ta đã phân tích thành công
        if target == 0:
            return []
        
        # Thử các số từ current_max - 1 trở xuống
        for i in range(min(int(target**0.5), current_max - 1), 0, -1):
            # Kiểm tra nếu bình phương của i nhỏ hơn hoặc bằng target
            if i*i <= target:
                # Thử phân tích đệ quy với target mới
                sub_result = decompose_recursive(target - i*i, i)
                
                # Nếu tìm được phân tích hợp lệ
                if sub_result is not None:
                    return sub_result + [i]
        
        # Không tìm được phân tích
        return None

    # Gọi hàm đệ quy với target là n^2 và giới hạn ban đầu là n
    result = decompose_recursive(n*n, n)
    
    # Trả về kết quả, nếu không có thì trả về None
    return result if result else None

# Hàm kiểm tra kết quả
def verify_decomposition(n, result):
    if result is None:
        print(f"Không tìm thấy phân tích cho {n}")
        return False
    
    # Kiểm tra tổng bình phương
    total_square = sum(x*x for x in result)
    expected_square = n*n
    
    # Kiểm tra tính tăng dần
    is_increasing = all(result[i] < result[i+1] for i in range(len(result)-1))
    
    print(f"\nKiểm tra phân tích cho n = {n}:")
    print(f"Kết quả: {result}")
    print(f"Tổng bình phương: {total_square}")
    print(f"Mong đợi: {expected_square}")
    print(f"Tăng dần: {is_increasing}")
    
    return (total_square == expected_square) and is_increasing

# Các test case
test_cases = [11, 50, 4, 12, 25, 100]

# Chạy kiểm tra
for case in test_cases:
    result = decompose(case)
    verify_decomposition(case, result)
