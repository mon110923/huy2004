def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    
    # Tính số phần tử và kiểm tra tính hợp lệ
    n = (end - begin) // step + 1
    last = begin + (n - 1) * step
    
    # Loại bỏ phần tử cuối nếu không khớp
    if last > end:
        n -= 1
    
    # Đảm bảo số phần tử không âm
    n = max(0, n)
    
    # Tính tổng theo công thức tổng số học
    return n * (2 * begin + (n - 1) * step) // 2 

# Hàm kiểm tra
def main():
    print(sequence_sum(2, 2, 2))   # 2
    print(sequence_sum(2, 6, 2))   # 12
    print(sequence_sum(1, 5, 1))   # 15
    print(sequence_sum(1, 5, 3))   # 5

# Chạy hàm kiểm tra nếu được chạy trực tiếp
if __name__ == "__main__":
    main()
