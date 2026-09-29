"""
UVA 10242 - Fourth Point!!

題目中文意思：
平行四邊形給四個點，其中有一個點重複出現，求缺少的第四點。

這題需要什麼資料：
每組 8 個浮點數，代表四個點。

解法重點：
若 A 是重複點，答案 = 另外兩點相加 - A。

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

data = list(map(float, sys.stdin.read().split()))
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for i in range(0, len(data), 8):
    pts = [(data[i+j], data[i+j+1]) for j in range(0, 8, 2)]
    ans = None
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for a in range(4):
        for b in range(a + 1, 4):
            # if 判斷題目的特殊情況或規則分支。
            if pts[a] == pts[b]:
                others = [pts[k] for k in range(4) if k not in (a, b)]
                ans = (others[0][0] + others[1][0] - pts[a][0],
                       others[0][1] + others[1][1] - pts[a][1])
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{ans[0]:.3f} {ans[1]:.3f}")
