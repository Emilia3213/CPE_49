"""
UVA 10235 - Simply Emirp

題目中文意思：
判斷 n 是否為質數；若 n 與反轉後的數都是不同的質數，則是 emirp。

這題需要什麼資料：
多個整數，讀到 EOF。

解法重點：
試除到 sqrt(n)。先判 n，再判 reverse(n)。

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

# def 定義函式，把會重複使用的邏輯整理起來。
def is_prime(n):
    # if 判斷題目的特殊情況或規則分支。
    if n < 2:
        # return 把函式算出的結果交回呼叫它的地方。
        return False
    # if 判斷題目的特殊情況或規則分支。
    if n == 2:
        # return 把函式算出的結果交回呼叫它的地方。
        return True
    # if 判斷題目的特殊情況或規則分支。
    if n % 2 == 0:
        # return 把函式算出的結果交回呼叫它的地方。
        return False
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for d in range(3, int(math.isqrt(n)) + 1, 2):
        # if 判斷題目的特殊情況或規則分支。
        if n % d == 0:
            # return 把函式算出的結果交回呼叫它的地方。
            return False
    return True

# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for s in sys.stdin.read().split():
    n = int(s)
    r = int(s[::-1])
    # if 判斷題目的特殊情況或規則分支。
    if not is_prime(n):
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{n} is not prime.")
    # elif 是第二種判斷情況，讓不同規則分開處理。
    elif r != n and is_prime(r):
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{n} is emirp.")
    # else 處理前面條件都不成立時的情況。
    else:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{n} is prime.")
