"""
UVA 948 - Fibonaccimal Base

題目中文意思：
把十進位正整數轉成 Fibonacci 進位表示法，也就是用不相鄰的 Fibonacci 數相加。

這題需要什麼資料：
第一行測資數；每行一個 n，輸出 `n = bits (fib)`。

解法重點：
預先產生 1,2,3,5...，由大到小貪心取用。

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

nums = list(map(int, sys.stdin.read().split()))
# if 判斷題目的特殊情況或規則分支。
if not nums:
    sys.exit()
fib = [1, 2]
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while fib[-1] <= 100000000:
    fib.append(fib[-1] + fib[-2])

t = nums[0]
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for n in nums[1:1+t]:
    started = False
    rem = n
    bits = []
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for f in reversed(fib):
        # if 判斷題目的特殊情況或規則分支。
        if f <= rem:
            bits.append("1")
            rem -= f
            started = True
        # elif 是第二種判斷情況，讓不同規則分開處理。
        elif started:
            bits.append("0")
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{n} = {''.join(bits)} (fib)")
