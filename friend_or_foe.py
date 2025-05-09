def friend(names, a = "fgfgfgf"):
    # Khai báo một hàm có tên 'friend' nhận đầu vào là danh sách tên
    
    # Danh sách để lưu trữ tên bạn bè
    friends_list = []
    
    # Vòng lặp để duyệt qua từng tên trong danh sách đầu vào
    for name in names:
        print(name)
        # Kiểm tra độ dài của tên, nếu đúng 4 chữ cái thì thêm vào danh sách bạn bè
        if len(name) == 4:
            print(2222)
            friends_list.append(name)
            print(friends_list)
    
    # Trả về danh sách bạn bè
    return friends_list

# Phần chạy thử nghiệm
def main():
    # Ví dụ 1
    input1 = ["Ryan", "Kieran", "Jason", "Yous"]
    print("Danh sách đầu vào 1:", input1)
    print("Bạn bè trong danh sách 1:", friend(input1))
    
    # Ví dụ 2
    # input2 = ["Peter", "Stephen", "Joe"]
    # print("\nDanh sách đầu vào 2:", input2)
    # print("Bạn bè trong danh sách 2:", friend(input2))

# Kiểm tra xem script có đang được chạy trực tiếp không
if __name__ == "__main__":
    main()