# Phần 1: Hàm tính giai thừa
def tinh_giai_thua(so):
    """
    Hàm tính giai thừa của một số nguyên
    
    Tham số:
    - so: Số nguyên cần tính giai thừa
    
    Trả về:
    - Giai thừa của số đó
    """
    # Kiểm tra số âm
    if so < 0:
        raise ValueError("Không thể tính giai thừa số âm")
    
    # Trường hợp đặc biệt cho 0 và 1
    if so <= 1:
        return 1
    
    # Tính giai thừa bằng vòng lặp (an toàn hơn đệ quy)
    ket_qua = 1
    for i in range(2, so + 1):
        ket_qua *= i
    
    return ket_qua

# Phần 2: Hàm nhập liệu từ người dùng
def nhap_so():
    """
    Hàm nhập số từ người dùng
    
    Trả về:
    - Số nguyên hợp lệ
    """
    while True:
        try:
            # Nhập số từ bàn phím
            so = int(input("Nhập số để tính giai thừa (0-12): "))
            
            # Kiểm tra giới hạn
            if 0 <= so <= 12:
                return so
            else:
                print("Vui lòng nhập số từ 0 đến 12")
        
        except ValueError:
            print("Bạn phải nhập một số nguyên!")

# Phần 3: Hàm chính (main) để chạy chương trình
def main():
    """
    Hàm chính điều khiển luồng chương trình
    """
    print("Chương trình tính giai thừa")
    print("==========================")
    
    # Lựa chọn chế độ
    while True:
        print("\nChọn chế độ:")
        print("1. Tính giai thừa")
        print("2. Thoát")
        
        lua_chon = input("Nhập lựa chọn (1/2): ")
        
        if lua_chon == '1':
            # Nhập và tính toán
            try:
                so = nhap_so()
                ket_qua = tinh_giai_thua(so)
                print(f"\n{so}! = {ket_qua}")
            
            except ValueError as loi:
                print(f"Lỗi: {loi}")
        
        elif lua_chon == '2':
            print("Cảm ơn bạn đã sử dụng!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Phần 4: Điều kiện để chạy chương trình
# Đảm bảo chỉ chạy khi file này được chạy trực tiếp
if __name__ == "__main__":
    main()
