def recover_secret(triplets):
    # Tạo tập hợp các ký tự duy nhất
    chars = set(char for triplet in triplets for char in triplet)
    
    # Xây dựng danh sách các ký tự đứng trước cho mỗi ký tự
    predecessors = {char: set() for char in chars}
    
    # Điền thông tin về các ký tự đứng trước
    for a, b, c in triplets:
        # Các ký tự trong bộ ba đầu tiên luôn đứng trước các ký tự sau nó
        predecessors[b].add(a)
        predecessors[c].add(a)
        predecessors[c].add(b)
    
    # Tiến hành khôi phục chuỗi
    secret = []
    
    # Lặp cho đến khi lấy hết các ký tự
    while chars:
        # Tìm ký tự không có ký tự nào đứng trước
        for char in list(chars):
            # Kiểm tra xem ký tự này có ký tự nào đứng trước không
            if not any(char in predecessors[other] for other in chars):
                # Thêm ký tự này vào đầu chuỗi
                secret.insert(0, char)
                # Loại bỏ ký tự khỏi tập
                chars.remove(char)
                break
    
    # Trả về chuỗi đã khôi phục
    return ''.join(secret)

# Các test case
def test_recover_secret():
    # Test case 1: Chuỗi "whatisup"
    triplets1 = [
        ['t','u','p'],
        ['w','h','i'],
        ['t','h','i'],
        ['h','i','p'],
        ['w','h','p'],
        ['t','n','i']
    ]
    result1 = recover_secret(triplets1)
    print("Test case 1:")
    print("Triplets:", triplets1)
    print("Recovered secret:", result1)
    print("Expected: whatisup")
    print("Passed:", result1 == "whatisup")
    print()

    # Test case 2: Một chuỗi khác
    triplets2 = [
        ['t','s','f'], 
        ['a','s','u'], 
        ['m','c','i'], 
        ['c','f','p']
    ]
    result2 = recover_secret(triplets2)
    print("Test case 2:")
    print("Triplets:", triplets2)
    print("Recovered secret:", result2)
    print()

    # Test case 3: Kiểm tra tính duy nhất
    def verify_triplets(secret, triplets):
        for a, b, c in triplets:
            if not (secret.index(a) < secret.index(b) < secret.index(c)):
                return False
        return True

    print("Test case 3: Verification")
    print("Verifying triplet constraints:", verify_triplets(result2, triplets2))

# Chạy các test case
if __name__ == "__main__":
    test_recover_secret()
