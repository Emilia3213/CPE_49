"""
UVA 10038 - Jolly Jumpers

題目中文意思：
長度 n 的序列若相鄰差的絕對值剛好包含 1 到 n-1 各一次，就是 Jolly。

這題需要什麼資料：
每行一組：n 後面接 n 個整數。

解法重點：
建立相鄰差集合，檢查是否等於 {1..n-1}。

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

# 逐行讀到 EOF：不知道有幾筆測資時最常用這種寫法。
for line in sys.stdin:
    nums = list(map(int, line.split()))
    # if 判斷題目的特殊情況或規則分支。
    if not nums:
        # continue 代表跳過這一輪，直接讀下一行或下一筆資料。
        continue
    n, arr = nums[0], nums[1:]
    diffs = {abs(arr[i] - arr[i - 1]) for i in range(1, n)}
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print("Jolly" if diffs == set(range(1, n)) else "Not jolly")
