"""
UVA 11417 - GCD

題目中文意思：
對 1 <= i < j <= N 的所有配對，計算 gcd(i,j) 總和。

這題需要什麼資料：
多個 N，以 0 結束。

解法重點：
N 最大不大，雙迴圈加 math.gcd 最簡單。

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
# gcd 用來求最大公因數，直接用內建函式比自己寫更快更不容易錯。
from math import gcd

# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for n in map(int, sys.stdin.read().split()):
    # if 判斷題目的特殊情況或規則分支。
    if n == 0:
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    total = 0
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(total)
