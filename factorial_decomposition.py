# Hàm phân tích số nguyên tố của giai thừa từ 2 đến n
def decomp(n):
    # Từ điển lưu số lần xuất hiện của các số nguyên tố
    factors = {}
    
    # Duyệt từng số từ 2 đến n
    for i in range(2, n + 1):
        # Biến tạm để phân tích số hiện tại
        x = i
        
        # Duyệt các số nguyên tố tiềm năng
        for p in range(2, int(x**0.5) + 2):
            # Chia hết và đếm số lần xuất hiện của số nguyên tố
            while x % p == 0:
                # Tăng số lần xuất hiện của số nguyên tố
                factors[p] = factors.get(p, 0) + 1
                # Chia số đang xét cho số nguyên tố
                x //= p
        
        # Nếu còn số lớn hơn 1 (là số nguyên tố lớn)
        if x > 1:
            # Thêm số nguyên tố này vào từ điển
            factors[x] = factors.get(x, 0) + 1
    
    # Chuyển kết quả thành chuỗi định dạng
    return ' * '.join(
        f"{p}" if k == 1 else f"{p}^{k}" 
        for p, k in sorted(factors.items())
    )

# Hàm kiểm tra và in kết quả
def test_decomp():
    # Các test case
    test_cases = [12, 22, 25, 30, 50]
    
    # Chạy từng test case
    for case in test_cases:
        print(f"Phân tích giai thừa {case}!:")
        print(decomp(case))
        print("-" * 40)

# Hàm main để chạy chương trình
def main():
    # Chạy các test case
    test_decomp()
    
    # Chế độ tương tác
    while True:
        try:
            # Nhập số từ người dùng
            n = int(input("\nNhập số n (nhập 0 để thoát): "))
            
            # Điều kiện thoát
            if n == 0:
                break
            
            # In kết quả phân tích
            print(f"Phân tích giai thừa {n}!:")
            print(decomp(n))
        
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

# Điều kiện chạy chính
if __name__ == "__main__":
    main()
