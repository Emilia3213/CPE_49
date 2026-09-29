"""
UVA 11461 - Square Numbers

題目中文意思：
計算閉區間 [a,b] 中有幾個完全平方數。

這題需要什麼資料：
多組 a b，以 0 0 結束。

解法重點：
答案是 floor(sqrt(b)) - ceil(sqrt(a)) + 1。

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
# 匯入 math：需要 sqrt、sin、radians、isqrt 這類數學函式時使用。
import math

# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for i in range(0, len(data), 2):
    a, b = data[i], data[i + 1]
    # if 判斷題目的特殊情況或規則分支。
    if a == 0 and b == 0:
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    lo = math.isqrt(a - 1) + 1
    hi = math.isqrt(b)
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(max(0, hi - lo + 1))
