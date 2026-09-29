"""
UVA 10057 - A mid-summer night's dream

題目中文意思：
給一堆數字，找所有能讓絕對距離總和最小的 A，輸出一個 A、原資料中等於可行 A 的數量、可行 A 的個數。

這題需要什麼資料：
多組資料，每組先給 n，再給 n 個整數。

解法重點：
排序後，中位區間 [arr[(n-1)//2], arr[n//2]] 都可行。

寫程式時可以照這個順序想：
1. 先把輸入讀進來，確認是一行一組、第一行有測資數，還是讀到 EOF。
2. 把題目要的規則轉成變數、迴圈、判斷式或函式。
3. 按照題目指定格式輸出，CPE/UVA 很常因為空格、空行、大小寫錯而 WA。
"""

# ===== 程式開始 =====
# 下面保留可以直接提交的 Python 解答。
# 註解會寫「這行在做什麼」以及「為什麼要這樣做」，
# 你用 Cursor 看時，可以先讀上面的題目說明，再對照下面程式。

# 匯入 sys：CPE/UVA 常用 sys.stdin 讀輸入，速度快，也能自然讀到 EOF。
import sys

# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
p = 0
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while p < len(data):
    n = data[p]; p += 1
    arr = sorted(data[p:p+n]); p += n
    lo = arr[(n - 1) // 2]
    hi = arr[n // 2]
    count = sum(lo <= x <= hi for x in arr)
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(lo, count, hi - lo + 1)
