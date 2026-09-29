"""
UVA 10409 - Die Game

題目中文意思：
骰子初始 top=1, north=2, west=3，依指令滾動後輸出最上面的數字。

這題需要什麼資料：
多組，先給指令數 n，再給 n 行 north/south/east/west，以 0 結束。

解法重點：
維護 top,bottom,north,south,east,west 六面，照方向交換。

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
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while p < len(lines):
    n = int(lines[p]); p += 1
    # if 判斷題目的特殊情況或規則分支。
    if n == 0:
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    top, bottom, north, south, east, west = 1, 6, 2, 5, 4, 3
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for _ in range(n):
        cmd = lines[p]; p += 1
        # if 判斷題目的特殊情況或規則分支。
        if cmd == "north":
            top, south, bottom, north = south, bottom, north, top
        # elif 是第二種判斷情況，讓不同規則分開處理。
        elif cmd == "south":
            top, north, bottom, south = north, bottom, south, top
        # elif 是第二種判斷情況，讓不同規則分開處理。
        elif cmd == "east":
            top, west, bottom, east = west, bottom, east, top
        # elif 是第二種判斷情況，讓不同規則分開處理。
        elif cmd == "west":
            top, east, bottom, west = east, bottom, west, top
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(top)
