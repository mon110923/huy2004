def triple_double(num1, num2):
    # Chuyển số thành chuỗi
    s1, s2 = str(num1), str(num2)
    
    # Kiểm tra điều kiện triple và double cho từng chữ số
    return any(
        digit * 3 in s1 and digit * 2 in s2 
        for digit in set(s1)
    )

# Test cases
test_cases = [
    (451999277, 41177722899),  # 1
    (1222345, 12345),          # 0
    (12345, 12345),            # 0
    (888, 77),                 # 0
    (88888, 88888),            # 1
    (123123123, 123)           # 0
]

# Chạy và in kết quả các test case
def main():
    for num1, num2 in test_cases:
        print(f"{num1}, {num2} --> {triple_double(num1, num2)}")

# Kiểm tra xem script có đang được chạy trực tiếp không
if __name__ == "__main__":
    main()
