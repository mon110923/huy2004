def solution(arr):
    # Kiểm tra nếu arr là None
    if arr is None:
        return []
    
    # Sắp xếp mảng
    return sorted(arr)

# Hàm chính để kiểm tra
def main():
    # Test case 1: Mảng bình thường
    print("Mảng số:", solution([3, 1, 4, 1, 5]))
    
    # Test case 2: Mảng None
    print("Mảng None:", solution(None))
    
    # Test case 3: Mảng rỗng
    print("Mảng rỗng:", solution([]))

# Chạy main nếu file được thực thi trực tiếp
if __name__ == "__main__":
    main()
