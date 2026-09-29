"""
UVA 10056 - What is the Probability?

題目中文意思：
n 個人輪流嘗試成功機率 p 的事件，求第 i 個人最先成功的機率。

這題需要什麼資料：
第一行測資數；每組 n p i。

解法重點：
第 i 人第一次輪到就成功或前面整輪都失敗後成功：p*(1-p)^(i-1) / (1-(1-p)^n)。若 p=0 則 0。

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

# 一次讀完所有 token：保留字串型態，之後需要時再轉 int/float。
tokens = sys.stdin.read().split()
t = int(tokens[0])
pidx = 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for _ in range(t):
    n = int(tokens[pidx])
    p = float(tokens[pidx + 1])
    i = int(tokens[pidx + 2])
    pidx += 3
    # if 判斷題目的特殊情況或規則分支。
    if p == 0:
        ans = 0.0
    # else 處理前面條件都不成立時的情況。
    else:
        q = 1 - p
        ans = (q ** (i - 1) * p) / (1 - q ** n)
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{ans:.4f}")
