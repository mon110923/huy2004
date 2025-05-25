def make_looper(string):
    """
    Tạo một hàm lặp vòng qua các ký tự của chuỗi.
    
    Args:
        string (str): Chuỗi đầu vào để lặp.
    
    Returns:
        function: Hàm trả về từng ký tự của chuỗi theo thứ tự, 
                  quay lại từ đầu khi đến cuối chuỗi.
    
    Raises:
        ValueError: Nếu chuỗi đầu vào rỗng.
    """
    if not string:
        raise ValueError("Chuỗi không được rỗng")
    
    def looper():
        """
        Generator để lặp vòng qua các ký tự của chuỗi.
        
        Yields:
            str: Từng ký tự của chuỗi theo thứ tự.
        """
        index = 0
        while True:
            yield string[index]
            index = (index + 1) % len(string)
    
    gen = looper()
    return lambda: next(gen)

def main():
    # Kiểm tra với chuỗi 'abc'
    print("Kiểm tra với chuỗi 'abc':")
    abc = make_looper('abc')
    print(abc())  # 'a'
    print(abc())  # 'b'
    print(abc())  # 'c'
    print(abc())  # 'a'

    # Kiểm tra với chuỗi khác
    print("\nKiểm tra với chuỗi 'xyz':")
    xyz = make_looper('xyz')
    print(xyz())  # 'x'
    print(xyz())  # 'y'
    print(xyz())  # 'z'
    print(xyz())  # 'x'

    # Kiểm tra tính độc lập của các vòng lặp
    print("\nKiểm tra tính độc lập của các vòng lặp:")
    a1 = make_looper('abc')
    a2 = make_looper('abc')
    print(a1())  # 'a'
    print(a2())  # 'a'
    print(a1())  # 'b'
    print(a2())  # 'b'

    # Kiểm tra ngoại lệ với chuỗi rỗng
    try:
        make_looper('')
    except ValueError as e:
        print(f"\nLỗi được bắt: {e}")

if __name__ == "__main__":
    main()
