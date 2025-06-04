class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result

def smaller(arr):
    # Bước 1: Nén giá trị để làm việc với các chỉ số nhỏ hơn
    sorted_arr = sorted(set(arr))
    rank = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
    
    # Bước 2: Khởi tạo Fenwick Tree
    n = len(rank)
    fenwick = FenwickTree(n)
    
    # Bước 3: Đếm số phần tử nhỏ hơn từ phải sang trái
    result = []
    for num in reversed(arr):
        # Truy vấn số phần tử nhỏ hơn hiện tại
        count = fenwick.query(rank[num] - 1)
        result.append(count)
        
        # Cập nhật Fenwick Tree
        fenwick.update(rank[num], 1)
    
    # Đảo ngược kết quả để đúng thứ tự ban đầu
    return list(reversed(result))

# Hàm main để kiểm tra
def main():
    # Các test case
    test_cases = [
        [5, 4, 3, 2, 1],
        [1, 2, 0],
        [1, 1, -1, 0, 0],
        [],
        [1]
    ]
    
    # In kết quả cho từng test case
    for case in test_cases:
        print(f"Input: {case}")
        print(f"Output: {smaller(case)}\n")

# Kiểm tra nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
