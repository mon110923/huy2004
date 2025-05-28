def cut_log(p, n):
    # Khởi tạo mảng lưu kết quả
    dp = [0] * (n + 1)
    
    # Tính toán từng độ dài
    for j in range(1, n + 1):
        q = 0
        for i in range(1, min(j + 1, len(p))):
            q = max(q, p[i] + dp[j - i])
        dp[j] = q
    
    return dp[n]

# Hàm main để kiểm tra
def main():
    # Ví dụ bảng giá
    p = [0, 1, 5, 8, 9, 10]
    
    # Các độ dài khác nhau để kiểm tra
    test_lengths = [0, 1, 2, 3, 4, 5, 6]
    
    # In kết quả cho từng độ dài
    for n in test_lengths:
        result = cut_log(p, n)
        print(f"Độ dài {n} feet: Giá trị tối đa = ${result}")

# Điều kiện để chạy hàm main
if __name__ == "__main__":
    main()
