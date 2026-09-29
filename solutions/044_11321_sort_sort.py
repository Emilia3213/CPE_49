"""
UVA 11321 - Sort! Sort!! and Sort!!!

題目中文意思：
依特殊規則排序：先按 n mod m 小到大；同餘時奇數排偶數前；奇數由大到小，偶數由小到大。

這題需要什麼資料：
多組 n m，接著 n 個整數；以 0 0 結束。每組要先原樣輸出 n m。

解法重點：
自訂排序 key：(x % m, odd/even rank, value rank)。Python 負數 % 結果和 C 不同，要自製 C 風格餘數。

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
def c_mod(x, m):
    # return 把函式算出的結果交回呼叫它的地方。
    return x % m if x >= 0 else -((-x) % m)

# def 定義函式，把會重複使用的邏輯整理起來。
def key(x, m):
    # if 判斷題目的特殊情況或規則分支。
    if x % 2:
        # return 把函式算出的結果交回呼叫它的地方。
        return (c_mod(x, m), 0, -x)
    return (c_mod(x, m), 1, x)

# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
p = 0
out = []
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while p < len(data):
    n, m = data[p], data[p + 1]; p += 2
    out.append(f"{n} {m}")
    # if 判斷題目的特殊情況或規則分支。
    if n == 0 and m == 0:
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    arr = data[p:p+n]; p += n
    out.extend(str(x) for x in sorted(arr, key=lambda x: key(x, m)))
# print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
print("\n".join(out))
