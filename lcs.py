def LCS(s1, s2):
    # Tạo ma trận để lưu độ dài các subsequence
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Xây dựng ma trận động
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if s1[i-1] == s2[j-1] else max(dp[i-1][j], dp[i][j-1])
    
    # Truy vết để tìm subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

def main():
    # Các test case
    test_cases = [
        ("abcdef", "abc"),
        ("abcdef", "acf"),
        ("132535365", "123456789"),
        ("AGGTAB", "GXTXAYB"),
        ("", "abc"),
        ("abc", ""),
        ("", "")
    ]
    
    # In kết quả cho từng test case
    print("Các test case LCS:")
    for s1, s2 in test_cases:
        result = LCS(s1, s2)
        print(f"LCS({s1}, {s2}) = {result}")

# Kiểm tra nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
