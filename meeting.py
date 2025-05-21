def meeting(s):
    # Bước 1: Tách chuỗi thành danh sách các khách mời
    guests = s.split(';')
    
    # Bước 2: Tách tên và họ, chuyển sang chữ IN HOA
    formatted_guests = []
    for guest in guests:
        first_name, last_name = guest.split(':')
        formatted_guests.append((last_name.upper(), first_name.upper()))
    
    # Bước 3: Sắp xếp danh sách 
    # Sắp xếp theo họ trước, sau đó đến tên
    sorted_guests = sorted(formatted_guests)
    
    # Bước 4: Định dạng kết quả cuối cùng
    result = ''.join(f"({last_name}, {first_name})" for last_name, first_name in sorted_guests)
    
    return result



# Nếu muốn có main, có thể viết như sau:
def main():
    s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    result = meeting(s)
    print(result)

# Chạy main nếu file được thực thi trực tiếp
if __name__ == "__main__":
    main()