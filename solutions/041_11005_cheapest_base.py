"""
UVA 11005 - Cheapest Base

題目中文意思：
給每個數字 0-35 的印刷成本，對多個十進位數找出用哪個 base 2-36 表示時總成本最低。

這題需要什麼資料：
第一行測資數；每組 36 個成本、查詢數 q、q 個數字。

解法重點：
對每個 base 反覆取餘數計算成本，找最小值的所有 base。

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

# def 定義函式，把會重複使用的邏輯整理起來。
def cost_in_base(n, base, costs):
    # if 判斷題目的特殊情況或規則分支。
    if n == 0:
        # return 把函式算出的結果交回呼叫它的地方。
        return costs[0]
    total = 0
    # while 迴圈適合「做到某個條件成立為止」的模擬題。
    while n:
        total += costs[n % base]
        n //= base
    # return 把函式算出的結果交回呼叫它的地方。
    return total

# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for case in range(1, t + 1):
    costs = data[p:p+36]; p += 36
    q = data[p]; p += 1
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"Case {case}:")
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for _ in range(q):
        n = data[p]; p += 1
        vals = [(cost_in_base(n, b, costs), b) for b in range(2, 37)]
        best = min(v for v, _ in vals)
        bases = [str(b) for v, b in vals if v == best]
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"Cheapest base(s) for number {n}: {' '.join(bases)}")
    # if 判斷題目的特殊情況或規則分支。
    if case != t:
        # 題目要求測資之間空一行時，直接 print() 輸出空白行。
        print()
