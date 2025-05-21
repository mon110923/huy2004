def clean_string(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)

def main():
    # Các test case
    print("Test case 1:")
    print(clean_string('abc#d##c'))   # Kết quả: 'ac'
    
    print("\nTest case 2:")
    print(clean_string('abc##d######'))  # Kết quả: ''
    
    print("\nTest case 3:")
    print(clean_string('bcdc'))  # Xử lý các trường hợp khác
    
    # Thêm các test case khác nếu muốn
    print("\nAdditional test cases:")
    print(clean_string('a#c'))  # Kết quả: 'c'
    print(clean_string('a##c'))  # Kết quả: 'c'
    print(clean_string(''))  # Kết quả: ''

# Kiểm tra xem file có đang được chạy trực tiếp không
if __name__ == "__main__":
    main()
