def simple_assembler(program):
    # Khởi tạo từ điển để lưu trữ giá trị của các thanh ghi
    registers = {}
    
    # Biến để theo dõi vị trí lệnh hiện tại
    pc = 0
    
    # Tiếp tục thực thi cho đến khi hết lệnh
    while pc < len(program):
        # Tách lệnh thành các phần
        instruction = program[pc].split()
        
        # Lệnh mov: gán giá trị cho thanh ghi
        if instruction[0] == 'mov':
            # Nếu giá trị là số, chuyển đổi sang số nguyên
            if instruction[2].lstrip('-').isdigit():
                registers[instruction[1]] = int(instruction[2])
            # Nếu là tham chiếu đến thanh ghi khác
            else:
                registers[instruction[1]] = registers[instruction[2]]
        
        # Lệnh inc: tăng giá trị của thanh ghi
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        
        # Lệnh dec: giảm giá trị của thanh ghi
        elif instruction[0] == 'dec':
            registers[instruction[1]] -= 1
        
        # Lệnh jnz: nhảy có điều kiện
        elif instruction[0] == 'jnz':
            # Kiểm tra điều kiện nhảy
            value = registers[instruction[1]] if instruction[1] in registers else int(instruction[1])
            
            # Nếu giá trị không phải 0, thực hiện nhảy
            if value != 0:
                # Tính toán offset (có thể là số hoặc giá trị thanh ghi)
                offset = registers[instruction[2]] if instruction[2] in registers else int(instruction[2])
                pc += offset
                # Trừ 1 vì vòng lặp while sẽ tăng pc
                pc -= 1
        
        # Chuyển đến lệnh tiếp theo
        pc += 1
    
    # Trả về từ điển các thanh ghi
    return registers

# Chạy trực tiếp để kiểm tra
def main():
    # Ví dụ sử dụng
    program = ["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"]
    result = simple_assembler(program)
    print(result)  # Kết quả: {'a': 1}

# Chạy main nếu file được thực thi trực tiếp
if __name__ == "__main__":
    main()
