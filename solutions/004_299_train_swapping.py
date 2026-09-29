"""
UVA 299 - Train Swapping

題目中文意思：
計算火車車廂用相鄰交換排成遞增順序時，最少需要交換幾次。

這題需要什麼資料：
第一行測資數；每組給車廂數 n，再給 n 個車廂編號。

解法重點：
相鄰交換次數等於逆序數；n 小，雙迴圈數逆序即可。

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
p = 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for _ in range(t):
    n = int(tokens[p]); p += 1
    arr = list(map(int, tokens[p:p+n])); p += n
    swaps = 0
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for i in range(n):
        for j in range(i + 1, n):
            # if 判斷題目的特殊情況或規則分支。
            if arr[i] > arr[j]:
                swaps += 1
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"Optimal train swapping takes {swaps} swaps.")
