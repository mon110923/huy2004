def next_bigger(n):
    # Chuyển số thành danh sách các chữ số
    digits = list(str(n))
    
    # Tìm vị trí đầu tiên từ phải sang trái mà số nhỏ hơn số bên phải
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            # Tìm số nhỏ nhất lớn hơn digits[i] từ phía bên phải
            for j in range(len(digits) - 1, i, -1):
                if digits[j] > digits[i]:
                    # Hoán đổi và sắp xếp lại phần còn lại
                    digits[i], digits[j] = digits[j], digits[i]
                    digits[i+1:] = sorted(digits[i+1:])
                    return int(''.join(digits))
    
    # Nếu không tìm thấy số lớn hơn
    return -1

# Hàm main để kiểm tra
def main():
    # Các test case
    test_cases = [
        12,      # Kết quả mong đợi: 21
        513,     # Kết quả mong đợi: 531
        2017,    # Kết quả mong đợi: 2071
        9,       # Kết quả mong đợi: -1
        111,     # Kết quả mong đợi: -1
        531,     # Kết quả mong đợi: -1
        1234,    # Kết quả mong đợi: 1243
        4321     # Kết quả mong đợi: -1
    ]
    
    # In kết quả cho từng test case
    for num in test_cases:
        result = next_bigger(num)
        print(f"next_bigger({num}) = {result}")

# Kiểm tra nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
