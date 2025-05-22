def tower_builder(n_floors):
    """
    Xây dựng tháp kim tự tháp với số tầng cho trước
    
    Args:
        n_floors (int): Số tầng của tháp
    
    Returns:
        list: Danh sách các tầng của tháp
    """
    tower = []
    
    # Vòng lặp để tạo từng tầng
    for i in range(n_floors):
        # Tính toán số khoảng trắng ở hai bên
        spaces = " " * (n_floors - i - 1)
        
        # Tính toán số sao ở giữa
        stars = "*" * (2 * i + 1)
        
        # Tạo tầng bằng cách nối spaces + stars + spaces
        floor = spaces + stars + spaces
        
        # Thêm tầng vào tháp
        tower.append(floor)
    
    return tower

# Hàm in tháp ra màn hình
def print_tower(tower):
    for floor in tower:
        print(floor)

# Chương trình chính
def main():
    # Nhập số tầng từ người dùng
    try:
        num_floors = int(input("Nhập số tầng của tháp (1-20): "))
        
        # Kiểm tra giới hạn số tầng
        if num_floors < 1 or num_floors > 20:
            print("Vui lòng nhập số tầng từ 1 đến 20!")
            return
        
        # Xây dựng và in tháp
        tower = tower_builder(num_floors)
        print(f"\nTháp {num_floors} tầng:\n")
        print_tower(tower)
        
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

# Điều kiện để chạy hàm main
if __name__ == "__main__":
    main()
