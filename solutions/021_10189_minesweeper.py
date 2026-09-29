"""
UVA 10189 - Minesweeper

題目中文意思：
給踩地雷盤面，將非地雷格改成周圍八格地雷數。

這題需要什麼資料：
多組 n m 與 n 行盤面，以 0 0 結束；輸出 Field #k。

解法重點：
對每個非 * 格檢查八方向。

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
p = 0
case = 1
first = True
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while p < len(lines):
    n, m = map(int, lines[p].split()); p += 1
    # if 判斷題目的特殊情況或規則分支。
    if n == 0 and m == 0:
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    grid = lines[p:p+n]; p += n
    # if 判斷題目的特殊情況或規則分支。
    if not first:
        # 題目要求測資之間空一行時，直接 print() 輸出空白行。
        print()
    first = False
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"Field #{case}:")
    case += 1
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for r in range(n):
        row = []
        # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
        for c in range(m):
            # if 判斷題目的特殊情況或規則分支。
            if grid[r][c] == "*":
                row.append("*")
            # else 處理前面條件都不成立時的情況。
            else:
                count = 0
                # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    # if 判斷題目的特殊情況或規則分支。
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                        count += 1
                row.append(str(count))
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print("".join(row))
