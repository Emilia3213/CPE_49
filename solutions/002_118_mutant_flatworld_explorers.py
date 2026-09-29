"""
UVA 118 - Mutant Flatworld Explorers

題目中文意思：
機器人在矩形世界中依指令移動；若走出邊界會掉落並留下氣味，之後其他機器人在同位置同方向會忽略該掉落指令。

這題需要什麼資料：
第一行右上角座標；之後每組為 x y 方向與一行指令。方向 N/E/S/W，指令 L/R/F。

解法重點：
模擬方向轉換與前進。掉落位置用 set 記錄 (x,y,dir)。

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

data = [line.strip() for line in sys.stdin if line.strip()]
max_x, max_y = map(int, data[0].split())
dirs = "NESW"
move = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
scents = set()

i = 1
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while i < len(data):
    x, y, d = data[i].split()
    x, y = int(x), int(y)
    commands = data[i + 1]
    lost = False
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for c in commands:
        # if 判斷題目的特殊情況或規則分支。
        if c == "L":
            d = dirs[(dirs.index(d) - 1) % 4]
        # elif 是第二種判斷情況，讓不同規則分開處理。
        elif c == "R":
            d = dirs[(dirs.index(d) + 1) % 4]
        # else 處理前面條件都不成立時的情況。
        else:
            dx, dy = move[d]
            nx, ny = x + dx, y + dy
            # if 判斷題目的特殊情況或規則分支。
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                # 同格同方向曾經掉過，就忽略這次前進。
                # if 判斷題目的特殊情況或規則分支。
                if (x, y, d) not in scents:
                    scents.add((x, y, d))
                    lost = True
                    # break 代表題目的結束條件成立，離開目前迴圈。
                    break
            # else 處理前面條件都不成立時的情況。
            else:
                x, y = nx, ny
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{x} {y} {d}" + (" LOST" if lost else ""))
    i += 2
