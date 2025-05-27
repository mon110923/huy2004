# Tên file: partitions.py

def partitions(n):
    '''
    Hàm tính số lượng phân hoạch của số nguyên n
    
    Tham số:
    n (int): Số nguyên dương cần tính số lượng phân hoạch
    
    Trả về:
    int: Số lượng phân hoạch của n
    '''
    # Khởi tạo mảng lưu số lượng phân hoạch
    p = [1] + [0] * n
    
    # Duyệt qua các số từ 1 đến n
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            # Tính toán số hạng Pentagonal
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2
            
            # Nếu số hạng Pentagonal lớn hơn i thì dừng
            if pentagonal1 > i:
                break
            
            # Xác định dấu dựa trên k
            sign = 1 if (k % 2 != 0) else -1
            
            # Cập nhật số lượng phân hoạch
            p[i] += sign * p[i - pentagonal1]
            
            # Kiểm tra và cập nhật số hạng Pentagonal thứ hai
            if pentagonal2 <= i:
                p[i] += sign * p[i - pentagonal2]
    
    # Trả về số lượng phân hoạch của n
    return p[n]

# Hàm kiểm tra và in kết quả
def test_partitions():
    # Các test case
    test_cases = [5, 10, 20, 50, 100]
    
    print("Kiểm tra số lượng phân hoạch:")
    for n in test_cases:
        result = partitions(n)
        print(f"Số lượng phân hoạch của {n}: {result}")

# Hàm main để chạy chương trình
def main():
    # Chạy các test case
    test_partitions()
    
    # Nhập số từ người dùng
    try:
        while True:
            n = int(input("\nNhập số nguyên để tính số lượng phân hoạch (nhập 0 để thoát): "))
            
            # Điều kiện thoát
            if n == 0:
                print("Kết thúc chương trình.")
                break
            
            # Kiểm tra đầu vào
            if n < 0:
                print("Vui lòng nhập số nguyên dương.")
                continue
            
            # Tính và hiển thị kết quả
            result = partitions(n)
            print(f"Số lượng phân hoạch của {n}: {result}")
    
    except ValueError:
        print("Đã xảy ra lỗi. Vui lòng nhập một số nguyên hợp lệ.")

# Kiểm tra nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
