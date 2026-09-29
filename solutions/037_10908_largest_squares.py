"""
UVA 10908 - Largest Squares

題目中文意思：
對每個查詢中心點，找最大奇數邊長正方形，使整個正方形字元都和中心字元相同。

這題需要什麼資料：
第一行測資數；每組 M N Q，M 行字元矩陣，Q 個中心 r c。

解法重點：
從半徑 0 往外擴，邊界超出或新方框有不同字元就停止。

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
t = int(lines[0])
p = 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for _ in range(t):
    m, n, q = map(int, lines[p].split()); p += 1
    grid = lines[p:p+m]; p += m
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(m, n, q)
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for _ in range(q):
        r, c = map(int, lines[p].split()); p += 1
        ch = grid[r][c]
        radius = 0
        # while 迴圈適合「做到某個條件成立為止」的模擬題。
        while True:
            nr = radius + 1
            # if 判斷題目的特殊情況或規則分支。
            if r - nr < 0 or r + nr >= m or c - nr < 0 or c + nr >= n:
                # break 代表題目的結束條件成立，離開目前迴圈。
                break
            ok = True
            # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
            for i in range(r - nr, r + nr + 1):
                for j in range(c - nr, c + nr + 1):
                    # if 判斷題目的特殊情況或規則分支。
                    if grid[i][j] != ch:
                        ok = False
                        # break 代表題目的結束條件成立，離開目前迴圈。
                        break
                # if 判斷題目的特殊情況或規則分支。
                if not ok:
                    # break 代表題目的結束條件成立，離開目前迴圈。
                    break
            # if 判斷題目的特殊情況或規則分支。
            if not ok:
                # break 代表題目的結束條件成立，離開目前迴圈。
                break
            radius = nr
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(2 * radius + 1)
