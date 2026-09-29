"""
UVA 10268 - 498-bis

題目中文意思：
給 x 與多項式係數，求多項式在 x 的導數值。

這題需要什麼資料：
每組兩行：第一行 x，第二行從高次到常數項係數。

解法重點：
若係數有 n 個，第一個係數次方是 n-1；導數係數為 coef*power，用 Horner 算導數值。

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

# splitlines() 逐行保留資料，適合每一行都有意義的題目。
lines = sys.stdin.read().splitlines()
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for i in range(0, len(lines), 2):
    x = int(lines[i])
    coeffs = list(map(int, lines[i + 1].split()))
    degree = len(coeffs) - 1
    ans = 0
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for idx, coef in enumerate(coeffs[:-1]):
        power = degree - idx
        ans = ans * x + coef * power
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(ans)
