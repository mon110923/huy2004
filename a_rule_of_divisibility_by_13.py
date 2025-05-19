def check_divisibility(number):
    # Tính các số dư của lũy thừa 10 mod 13
    remainders = [(10 ** i) % 13 for i in range(6)]
    
    # Tính tổng với các số dư
    total = sum(int(digit) * remainders[i] for i, digit in enumerate(str(number)[::-1]))

    # Kiểm tra tính chia hết
    return total % 13 == 0

# Ví dụ sử dụng
number = 123456  # Thay đổi số này để kiểm tra
if check_divisibility(number):
    print(f"{number} chia hết cho 13.")
else:
    print(f"{number} không chia hết cho 13.")

if __name__ == "__main__":
    # Gọi hàm main nếu cần
    pass  # Thay thế bằng mã khác nếu cần
