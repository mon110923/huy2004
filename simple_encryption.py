def encrypt(text, n):
    # Kiểm tra điều kiện đầu vào không hợp lệ
    if not text or n <= 0:
        return text
    
    # Thực hiện mã hóa n lần
    for _ in range(n):
        # Tách và nối các ký tự lẻ và chẵn
        text = text[1::2] + text[::2]
    
    return text

def decrypt(encrypted_text, n):
    # Kiểm tra điều kiện đầu vào không hợp lệ
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    # Thực hiện giải mã n lần
    for _ in range(n):
        # Tính độ dài của nửa đầu
        half = len(encrypted_text) // 2
        
        # Khôi phục lại chuỗi
        decrypted = ''.join(
            encrypted_text[half + i] + encrypted_text[i] 
            for i in range(half)
        ) + (encrypted_text[-1] if len(encrypted_text) % 2 else '')
        
        encrypted_text = decrypted
    
    return encrypted_text

# Thêm hàm main
def main():
    # Các thao tác kiểm tra hoặc chạy chính
    print(encrypt("012345", 1))  # "135024"
    print(encrypt("012345", 2))  # "304152"
    print(encrypt("01234", 1))   # "13024"

    print(decrypt("135024", 1))  # "012345"
    print(decrypt("304152", 2))  # "012345"
    print(decrypt("13024", 1))   # "01234")

# Chạy main nếu file được thực thi trực tiếp
if __name__ == "__main__":
    main()
