from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "solutions"


PROBLEMS = [
    {
        "no": 1,
        "uva": "100",
        "title": "The 3n + 1 problem",
        "zh": "給兩個整數 i, j，找出區間內每個數做 Collatz 規則後的循環長度，輸出最大循環長度。",
        "need": "每行兩個整數；輸出原本順序的 i j 與閉區間 [min(i,j), max(i,j)] 的最大 cycle length。",
        "idea": "逐數計算 Collatz 長度並用快取避免重算。注意輸入順序要原樣輸出。",
        "file": "001_100_3n_plus_1.py",
        "code": r'''
"""
UVA 100 - The 3n + 1 problem

題目中文意思：
給你兩個整數 i 和 j，請看 i 到 j 之間每一個數字的 3n+1 循環長度，
最後輸出這個區間裡「最大的循環長度」。

3n+1 規則：
1. 如果 n 是奇數，下一個數字變成 3*n + 1
2. 如果 n 是偶數，下一個數字變成 n / 2
3. 一直做到 n 變成 1 為止
4. 循環長度 = 從原本的 n 到 1 總共出現幾個數字

例子：
n = 22
22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
所以 22 的循環長度是 16。

輸入：
每一行有兩個整數 i j，可能有很多行，讀到 EOF 結束。

輸出：
每一行輸出：原本的 i 原本的 j 區間內最大循環長度
注意：就算 i > j，輸出時也要照原本輸入順序印出 i j。

解法：
1. 對區間 min(i,j) 到 max(i,j) 每個數字都算 cycle length。
2. 取最大的 cycle length。
3. 使用 cache 記憶化，算過的數字不用再重算，速度會快很多。
"""

import sys


# cache 用來記錄「某個數字的循環長度」。
# 因為很多數字在做 3n+1 時會走到同樣的中間數字，
# 例如 22 會走到 11，別的數字也可能走到 11。
# 如果 11 的答案已經算過，就可以直接拿來用，不用整段重算。
cache = {1: 1}  # 1 的循環長度就是 1，這是遞迴停止點。


def cycle_len(n):
    """回傳 n 的 3n+1 循環長度。"""

    # 如果 n 已經算過，直接回傳。
    # 這就是「記憶化」：用空間換時間，避免重複計算。
    if n in cache:
        return cache[n]

    # 題目規則：奇數下一步是 3*n + 1。
    # 目前這個 n 也算一個數字，所以長度要 +1。
    if n % 2 == 1:
        cache[n] = 1 + cycle_len(3 * n + 1)

    # 題目規則：偶數下一步是 n / 2。
    # Python 的 // 是整數除法，這裡要用 //，不要用 /，
    # 因為 / 會變成小數 float，後面當整數處理會比較麻煩。
    else:
        cache[n] = 1 + cycle_len(n // 2)

    return cache[n]


# sys.stdin 會一行一行讀取輸入，適合 UVA / CPE 這種「讀到 EOF」的題目。
for line in sys.stdin:
    # 避免空白行造成 split 後沒有資料。
    if not line.strip():
        continue

    # map(int, line.split())：
    # line.split() 先把一行切成字串，例如 "1 10" -> ["1", "10"]
    # map(int, ...) 再把它們轉成整數。
    a, b = map(int, line.split())

    # 題目要求 i 到 j 的區間，但輸入可能是 10 1。
    # 所以計算時要用小的當開頭、大的當結尾。
    lo, hi = min(a, b), max(a, b)

    # 逐一計算區間內每個 x 的循環長度，max 取最大值。
    # range(lo, hi + 1) 要 +1，因為 Python range 的尾端不包含 hi。
    ans = max(cycle_len(x) for x in range(lo, hi + 1))

    # 輸出時必須印原本輸入的 a b，不能印排序後的 lo hi。
    print(a, b, ans)
''',
        "tests": [("1 10\n100 200\n201 210\n900 1000\n", "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")],
    },
    {
        "no": 2,
        "uva": "118",
        "title": "Mutant Flatworld Explorers",
        "zh": "機器人在矩形世界中依指令移動；若走出邊界會掉落並留下氣味，之後其他機器人在同位置同方向會忽略該掉落指令。",
        "need": "第一行右上角座標；之後每組為 x y 方向與一行指令。方向 N/E/S/W，指令 L/R/F。",
        "idea": "模擬方向轉換與前進。掉落位置用 set 記錄 (x,y,dir)。",
        "file": "002_118_mutant_flatworld_explorers.py",
        "code": r'''
import sys

data = [line.strip() for line in sys.stdin if line.strip()]
max_x, max_y = map(int, data[0].split())
dirs = "NESW"
move = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
scents = set()

i = 1
while i < len(data):
    x, y, d = data[i].split()
    x, y = int(x), int(y)
    commands = data[i + 1]
    lost = False
    for c in commands:
        if c == "L":
            d = dirs[(dirs.index(d) - 1) % 4]
        elif c == "R":
            d = dirs[(dirs.index(d) + 1) % 4]
        else:
            dx, dy = move[d]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                # 同格同方向曾經掉過，就忽略這次前進。
                if (x, y, d) not in scents:
                    scents.add((x, y, d))
                    lost = True
                    break
            else:
                x, y = nx, ny
    print(f"{x} {y} {d}" + (" LOST" if lost else ""))
    i += 2
''',
        "tests": [("5 3\n1 1 E\nRFRFRFRF\n3 2 N\nFRRFLLFFRRFLL\n0 3 W\nLLFFFLFLFL\n", "1 1 E\n3 3 N LOST\n2 3 S\n")],
    },
    {
        "no": 3,
        "uva": "272",
        "title": "TeX Quotes",
        "zh": "把文章中的雙引號依序替換成 TeX 的左引號 `` 與右引號 ''。",
        "need": "任意多行文字，保留其他字元與換行。",
        "idea": "遇到 `\"` 時用布林值交替輸出開引號與關引號。",
        "file": "003_272_tex_quotes.py",
        "code": r'''
import sys

open_quote = True
out = []
for ch in sys.stdin.read():
    if ch == '"':
        out.append("``" if open_quote else "''")
        open_quote = not open_quote
    else:
        out.append(ch)
print("".join(out), end="")
''',
        "tests": [('"To be or not to be," quoth.\n', "``To be or not to be,'' quoth.\n")],
    },
    {
        "no": 4,
        "uva": "299",
        "title": "Train Swapping",
        "zh": "計算火車車廂用相鄰交換排成遞增順序時，最少需要交換幾次。",
        "need": "第一行測資數；每組給車廂數 n，再給 n 個車廂編號。",
        "idea": "相鄰交換次數等於逆序數；n 小，雙迴圈數逆序即可。",
        "file": "004_299_train_swapping.py",
        "code": r'''
import sys

tokens = sys.stdin.read().split()
t = int(tokens[0])
p = 1
for _ in range(t):
    n = int(tokens[p]); p += 1
    arr = list(map(int, tokens[p:p+n])); p += n
    swaps = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps += 1
    print(f"Optimal train swapping takes {swaps} swaps.")
''',
        "tests": [("1\n3\n3 2 1\n", "Optimal train swapping takes 3 swaps.\n")],
    },
    {
        "no": 5,
        "uva": "490",
        "title": "Rotating Sentences",
        "zh": "把多行文字順時針旋轉 90 度，短行缺的地方用空白補齊。",
        "need": "讀到 EOF 的所有行；輸出旋轉後文字。",
        "idea": "找到最大寬度，將每行右側補空白，再從左欄到右欄、由下往上輸出。",
        "file": "005_490_rotating_sentences.py",
        "code": r'''
import sys

lines = sys.stdin.read().splitlines()
if not lines:
    sys.exit()
w = max(len(s) for s in lines)
grid = [s.ljust(w) for s in lines]
for c in range(w):
    print("".join(grid[r][c] for r in range(len(grid) - 1, -1, -1)))
''',
        "tests": [("Rene Decartes once said,\nI think, therefore I am.\n", "IR\n e\ntn\nhe\ni \nnD\nke\n,c\n a\ntr\nht\nee\nrs\ne \nfo\non\nrc\nee\n  \nIs\n a\nai\nmd\n.,\n")],
    },
    {
        "no": 6,
        "uva": "948",
        "title": "Fibonaccimal Base",
        "zh": "把十進位正整數轉成 Fibonacci 進位表示法，也就是用不相鄰的 Fibonacci 數相加。",
        "need": "第一行測資數；每行一個 n，輸出 `n = bits (fib)`。",
        "idea": "預先產生 1,2,3,5...，由大到小貪心取用。",
        "file": "006_948_fibonaccimal_base.py",
        "code": r'''
import sys

nums = list(map(int, sys.stdin.read().split()))
if not nums:
    sys.exit()
fib = [1, 2]
while fib[-1] <= 100000000:
    fib.append(fib[-1] + fib[-2])

t = nums[0]
for n in nums[1:1+t]:
    started = False
    rem = n
    bits = []
    for f in reversed(fib):
        if f <= rem:
            bits.append("1")
            rem -= f
            started = True
        elif started:
            bits.append("0")
    print(f"{n} = {''.join(bits)} (fib)")
''',
        "tests": [("3\n1\n2\n10\n", "1 = 1 (fib)\n2 = 10 (fib)\n10 = 10010 (fib)\n")],
    },
    {
        "no": 7,
        "uva": "10008",
        "title": "What's Cryptanalysis",
        "zh": "統計文章中英文字母出現次數，不分大小寫，依次數多到少、同次數按字母 A-Z 輸出。",
        "need": "第一行 n，接著 n 行文字。",
        "idea": "只統計 A-Z；排序 key 使用 (-count, letter)。",
        "file": "007_10008_whats_cryptanalysis.py",
        "code": r'''
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
cnt = Counter()
for line in lines[1:]:
    for ch in line.upper():
        if "A" <= ch <= "Z":
            cnt[ch] += 1
for ch, c in sorted(cnt.items(), key=lambda item: (-item[1], item[0])):
    print(ch, c)
''',
        "tests": [("3\nThis is a test.\nCount me 1 more.\nAA\n", "T 4\nA 3\nE 3\nS 3\nI 2\nM 2\nO 2\nC 1\nH 1\nN 1\nR 1\nU 1\n")],
    },
    {
        "no": 8,
        "uva": "10019",
        "title": "Funny Encryption Method",
        "zh": "對每個十進位數 n，分別計算 n 的二進位 1 的數量，以及把 n 的十進位每位當作十六進位字串後的 1 的數量。",
        "need": "第一行測資數；每行一個整數。",
        "idea": "b1 = bin(n).count('1')；b2 = bin(int(str(n),16)).count('1')。",
        "file": "008_10019_funny_encryption_method.py",
        "code": r'''
import sys

nums = sys.stdin.read().split()
for s in nums[1:]:
    b1 = bin(int(s)).count("1")
    b2 = bin(int(s, 16)).count("1")
    print(b1, b2)
''',
        "tests": [("3\n10\n15\n999\n", "2 1\n4 3\n8 6\n")],
    },
    {
        "no": 9,
        "uva": "10035",
        "title": "Primary Arithmetic",
        "zh": "計算兩個非負整數直式加法時產生幾次進位。",
        "need": "多組 a b，以 `0 0` 結束。",
        "idea": "從個位數往前加，記錄 carry，每次和 >=10 就多一次進位。",
        "file": "009_10035_primary_arithmetic.py",
        "code": r'''
import sys

for line in sys.stdin:
    a, b = line.split()
    if a == "0" and b == "0":
        break
    i, j, carry, ans = len(a) - 1, len(b) - 1, 0, 0
    while i >= 0 or j >= 0:
        da = ord(a[i]) - 48 if i >= 0 else 0
        db = ord(b[j]) - 48 if j >= 0 else 0
        carry = 1 if da + db + carry >= 10 else 0
        ans += carry
        i -= 1
        j -= 1
    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")
''',
        "tests": [("123 456\n555 555\n123 594\n0 0\n", "No carry operation.\n3 carry operations.\n1 carry operation.\n")],
    },
    {
        "no": 10,
        "uva": "10038",
        "title": "Jolly Jumpers",
        "zh": "長度 n 的序列若相鄰差的絕對值剛好包含 1 到 n-1 各一次，就是 Jolly。",
        "need": "每行一組：n 後面接 n 個整數。",
        "idea": "建立相鄰差集合，檢查是否等於 {1..n-1}。",
        "file": "010_10038_jolly_jumpers.py",
        "code": r'''
import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    if not nums:
        continue
    n, arr = nums[0], nums[1:]
    diffs = {abs(arr[i] - arr[i - 1]) for i in range(1, n)}
    print("Jolly" if diffs == set(range(1, n)) else "Not jolly")
''',
        "tests": [("4 1 4 2 3\n5 1 4 2 -1 6\n", "Jolly\nNot jolly\n")],
    },
    {
        "no": 11,
        "uva": "10041",
        "title": "Vito's family",
        "zh": "找一個街號讓所有親戚到該處的距離總和最小。",
        "need": "第一行測資數；每組第一個數是親戚數 r，後面 r 個街號。",
        "idea": "一維絕對距離總和最小點是中位數。",
        "file": "011_10041_vitos_family.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for _ in range(t):
    r = data[p]; p += 1
    streets = sorted(data[p:p+r]); p += r
    mid = streets[r // 2]
    print(sum(abs(x - mid) for x in streets))
''',
        "tests": [("2\n2 2 4\n3 2 4 6\n", "2\n4\n")],
    },
    {
        "no": 12,
        "uva": "10050",
        "title": "Hartals",
        "zh": "多個政黨每隔 h 天罷工，計算 n 天內有多少工作日受罷工影響；週五、週六不算。",
        "need": "第一行測資數；每組 n、政黨數 p、接著 p 個 hartal 參數。",
        "idea": "逐天檢查是否非週末且能被任一 h 整除。UVA 的第 6、7 天是週五、週六。",
        "file": "012_10050_hartals.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for _ in range(t):
    n = data[p]; parties = data[p + 1]; p += 2
    hs = data[p:p+parties]; p += parties
    lost = 0
    for day in range(1, n + 1):
        if day % 7 in (6, 0):
            continue
        if any(day % h == 0 for h in hs):
            lost += 1
    print(lost)
''',
        "tests": [("1\n14\n3\n3\n4\n8\n", "5\n")],
    },
    {
        "no": 13,
        "uva": "10055",
        "title": "Hashmat the Brave Warrior",
        "zh": "給兩個軍隊人數，輸出差的絕對值。",
        "need": "每行兩個非負整數，讀到 EOF。",
        "idea": "直接 abs(a-b)。",
        "file": "013_10055_hashmat.py",
        "code": r'''
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(abs(a - b))
''',
        "tests": [("10 12\n10 14\n100 200\n", "2\n4\n100\n")],
    },
    {
        "no": 14,
        "uva": "10056",
        "title": "What is the Probability?",
        "zh": "n 個人輪流嘗試成功機率 p 的事件，求第 i 個人最先成功的機率。",
        "need": "第一行測資數；每組 n p i。",
        "idea": "第 i 人第一次輪到就成功或前面整輪都失敗後成功：p*(1-p)^(i-1) / (1-(1-p)^n)。若 p=0 則 0。",
        "file": "014_10056_probability.py",
        "code": r'''
import sys

tokens = sys.stdin.read().split()
t = int(tokens[0])
pidx = 1
for _ in range(t):
    n = int(tokens[pidx])
    p = float(tokens[pidx + 1])
    i = int(tokens[pidx + 2])
    pidx += 3
    if p == 0:
        ans = 0.0
    else:
        q = 1 - p
        ans = (q ** (i - 1) * p) / (1 - q ** n)
    print(f"{ans:.4f}")
''',
        "tests": [("1\n2 0.166666 1\n", "0.5455\n")],
    },
    {
        "no": 15,
        "uva": "10057",
        "title": "A mid-summer night's dream",
        "zh": "給一堆數字，找所有能讓絕對距離總和最小的 A，輸出一個 A、原資料中等於可行 A 的數量、可行 A 的個數。",
        "need": "多組資料，每組先給 n，再給 n 個整數。",
        "idea": "排序後，中位區間 [arr[(n-1)//2], arr[n//2]] 都可行。",
        "file": "015_10057_midsummer.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
p = 0
while p < len(data):
    n = data[p]; p += 1
    arr = sorted(data[p:p+n]); p += n
    lo = arr[(n - 1) // 2]
    hi = arr[n // 2]
    count = sum(lo <= x <= hi for x in arr)
    print(lo, count, hi - lo + 1)
''',
        "tests": [("2\n1\n2\n4\n1\n2\n2\n4\n", "1 2 2\n2 2 1\n")],
    },
    {
        "no": 16,
        "uva": "10062",
        "title": "Tell me the frequencies!",
        "zh": "統計每行文字中各 ASCII 字元出現次數，依次數小到大，次數相同 ASCII 大到小輸出。",
        "need": "多行文字；不同輸入行的答案間要空一行。",
        "idea": "Counter 每行，排序 key=(count, -ord)。",
        "file": "016_10062_frequencies.py",
        "code": r'''
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
for idx, line in enumerate(lines):
    if idx:
        print()
    cnt = Counter(line)
    for ch, c in sorted(cnt.items(), key=lambda item: (item[1], -ord(item[0]))):
        print(ord(ch), c)
''',
        "tests": [("AAABBC\n", "67 1\n66 2\n65 3\n")],
    },
    {
        "no": 17,
        "uva": "10071",
        "title": "Back to High School Physics",
        "zh": "已知速度 v 和時間 t，求等加速度對稱運動在 2t 時的位移。",
        "need": "每行兩個整數 v t。",
        "idea": "題目公式就是 2*v*t。",
        "file": "017_10071_physics.py",
        "code": r'''
import sys

for line in sys.stdin:
    v, t = map(int, line.split())
    print(2 * v * t)
''',
        "tests": [("0 0\n5 12\n", "0\n120\n")],
    },
    {
        "no": 18,
        "uva": "10093",
        "title": "An Easy Problem!",
        "zh": "給一串由 0-9、A-Z、a-z 組成的數，找最小進位 base，使這個數能被 base-1 整除。",
        "need": "多行字串，讀到 EOF；忽略非英數字元。",
        "idea": "字元值最大值 + 1 是最低 base；base 範圍至少 2 到 62。利用 N mod (base-1) 等於各位值總和 mod (base-1)。",
        "file": "018_10093_easy_problem.py",
        "code": r'''
import sys

def val(ch):
    if ch.isdigit():
        return ord(ch) - ord("0")
    if "A" <= ch <= "Z":
        return ord(ch) - ord("A") + 10
    if "a" <= ch <= "z":
        return ord(ch) - ord("a") + 36
    return -1

for line in sys.stdin:
    digits = [val(ch) for ch in line.strip() if val(ch) >= 0]
    if not digits:
        continue
    start = max(2, max(digits) + 1)
    s = sum(digits)
    for base in range(start, 63):
        if s % (base - 1) == 0:
            print(base)
            break
    else:
        print("such number is impossible!")
''',
        "tests": [("3\n5\nA\n", "4\n6\n11\n")],
    },
    {
        "no": 19,
        "uva": "10101",
        "title": "Bangla Numbers",
        "zh": "把整數轉成 Bangla 計數單位格式：kuti, lakh, hajar, shata。",
        "need": "多行非負整數；每行輸出編號加轉換結果。",
        "idea": "每 7 位會重複 kuti；遞迴處理高位，再處理 lakh/hajar/shata/個位。",
        "file": "019_10101_bangla_numbers.py",
        "code": r'''
import sys

def bangla(n):
    parts = []
    if n >= 10000000:
        parts += bangla(n // 10000000)
        parts.append("kuti")
        n %= 10000000
    if n >= 100000:
        parts += [str(n // 100000), "lakh"]
        n %= 100000
    if n >= 1000:
        parts += [str(n // 1000), "hajar"]
        n %= 1000
    if n >= 100:
        parts += [str(n // 100), "shata"]
        n %= 100
    if n:
        parts.append(str(n))
    return parts

for case, line in enumerate(sys.stdin, 1):
    n = int(line)
    parts = bangla(n) if n else ["0"]
    print(f"{case:4d}. {' '.join(parts)}")
''',
        "tests": [("23764\n45897458973958\n", "   1. 23 hajar 7 shata 64\n   2. 45 lakh 89 hajar 7 shata 45 kuti 89 lakh 73 hajar 9 shata 58\n")],
    },
    {
        "no": 20,
        "uva": "10170",
        "title": "The Hotel with Infinite Rooms",
        "zh": "第 1 天住 S 人，之後每天人數加 1，找累積人數第一次達到或超過 D 的那天人數。",
        "need": "多組 S D，讀到 EOF。",
        "idea": "從 S 開始累加直到 sum >= D。數字不大時最直觀，也可用公式；這裡用 while 容易記。",
        "file": "020_10170_infinite_rooms.py",
        "code": r'''
import sys

for line in sys.stdin:
    s, d = map(int, line.split())
    total = 0
    day_people = s
    while total < d:
        total += day_people
        if total >= d:
            print(day_people)
            break
        day_people += 1
''',
        "tests": [("1 6\n3 10\n", "3\n5\n")],
    },
    {
        "no": 21,
        "uva": "10189",
        "title": "Minesweeper",
        "zh": "給踩地雷盤面，將非地雷格改成周圍八格地雷數。",
        "need": "多組 n m 與 n 行盤面，以 0 0 結束；輸出 Field #k。",
        "idea": "對每個非 * 格檢查八方向。",
        "file": "021_10189_minesweeper.py",
        "code": r'''
import sys

lines = sys.stdin.read().splitlines()
p = 0
case = 1
first = True
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while p < len(lines):
    n, m = map(int, lines[p].split()); p += 1
    if n == 0 and m == 0:
        break
    grid = lines[p:p+n]; p += n
    if not first:
        print()
    first = False
    print(f"Field #{case}:")
    case += 1
    for r in range(n):
        row = []
        for c in range(m):
            if grid[r][c] == "*":
                row.append("*")
            else:
                count = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                        count += 1
                row.append(str(count))
        print("".join(row))
''',
        "tests": [("4 4\n*...\n....\n.*..\n....\n0 0\n", "Field #1:\n*100\n2210\n1*10\n1110\n")],
    },
    {
        "no": 22,
        "uva": "10190",
        "title": "Divide, But Not Quite Conquer!",
        "zh": "判斷 n 是否能一直除以 m，最後剛好變成 1；可以則輸出整個序列，否則 Boring!。",
        "need": "多組 n m，讀到 EOF。",
        "idea": "m 必須大於 1，且每一步 n 都要能被 m 整除。",
        "file": "022_10190_divide.py",
        "code": r'''
import sys

for line in sys.stdin:
    n, m = map(int, line.split())
    seq = [n]
    ok = m > 1 and n > 1
    while ok and n != 1:
        if n % m != 0:
            ok = False
            break
        n //= m
        seq.append(n)
    print(" ".join(map(str, seq)) if ok and seq[-1] == 1 else "Boring!")
''',
        "tests": [("125 5\n30 3\n", "125 25 5 1\nBoring!\n")],
    },
    {
        "no": 23,
        "uva": "10193",
        "title": "All You Need Is Love",
        "zh": "兩個二進位數若轉十進位後最大公因數大於 1，就代表有共同因子。",
        "need": "第一行測資數；每組兩行二進位字串。",
        "idea": "int(s, 2) 轉換後用 gcd。",
        "file": "023_10193_love.py",
        "code": r'''
import sys
from math import gcd

lines = sys.stdin.read().splitlines()
t = int(lines[0])
p = 1
for case in range(1, t + 1):
    a = int(lines[p], 2)
    b = int(lines[p + 1], 2)
    p += 2
    if gcd(a, b) > 1:
        print(f"Pair #{case}: All you need is love!")
    else:
        print(f"Pair #{case}: Love is not all you need!")
''',
        "tests": [("2\n11011\n11000\n11011\n10011\n", "Pair #1: All you need is love!\nPair #2: Love is not all you need!\n")],
    },
    {
        "no": 24,
        "uva": "10221",
        "title": "Satellites",
        "zh": "已知地球表面上方高度 s 與中心角 a，計算弧長與弦長；角度可能是 degree 或 minute。",
        "need": "多組 s a unit；地球半徑固定 6440。",
        "idea": "minute 要除以 60 變 degree；大於 180 度取較小角 360-a；再轉弧度計算。",
        "file": "024_10221_satellites.py",
        "code": r'''
import sys
import math

R = 6440
for line in sys.stdin:
    s, a, unit = line.split()
    radius = R + float(s)
    angle = float(a)
    if unit == "min":
        angle /= 60
    if angle > 180:
        angle = 360 - angle
    rad = math.radians(angle)
    arc = radius * rad
    chord = 2 * radius * math.sin(rad / 2)
    print(f"{arc:.6f} {chord:.6f}")
''',
        "tests": [("500 30 deg\n", "3633.775503 3592.408346\n")],
    },
    {
        "no": 25,
        "uva": "10222",
        "title": "Decode the Mad man",
        "zh": "把輸入字元換成鍵盤上左邊第二個鍵，還原打錯位置的文字。",
        "need": "任意文字到 EOF；保留換行。",
        "idea": "建立鍵盤字串，每個可見字元找 index 後輸出 index-2 的字。",
        "file": "025_10222_decode_mad_man.py",
        "code": r'''
import sys

keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
pos = {ch: i for i, ch in enumerate(keys)}
out = []
for ch in sys.stdin.read():
    low = ch.lower()
    if low in pos and pos[low] >= 2:
        out.append(keys[pos[low] - 2])
    else:
        out.append(ch)
print("".join(out), end="")
''',
        "tests": [("k[r dyt I[o\n", "how are you\n")],
    },
    {
        "no": 26,
        "uva": "10226",
        "title": "Hardwood Species",
        "zh": "統計每種樹名在森林資料中的百分比。",
        "need": "第一行測資數，空白行分隔測資；每組多行樹名。",
        "idea": "每組用 Counter 計數，按樹名字典序輸出比例到小數四位。",
        "file": "026_10226_hardwood_species.py",
        "code": r'''
import sys
from collections import Counter

text = sys.stdin.read().splitlines()
t = int(text[0])
idx = 1
while idx < len(text) and text[idx] == "":
    idx += 1
for case in range(t):
    cnt = Counter()
    total = 0
    while idx < len(text) and text[idx] != "":
        cnt[text[idx]] += 1
        total += 1
        idx += 1
    if case:
        print()
    for name in sorted(cnt):
        print(f"{name} {cnt[name] * 100 / total:.4f}")
    while idx < len(text) and text[idx] == "":
        idx += 1
''',
        "tests": [("1\n\nRed Alder\nAsh\nAspen\nRed Alder\n", "Ash 25.0000\nAspen 25.0000\nRed Alder 50.0000\n")],
    },
    {
        "no": 27,
        "uva": "10235",
        "title": "Simply Emirp",
        "zh": "判斷 n 是否為質數；若 n 與反轉後的數都是不同的質數，則是 emirp。",
        "need": "多個整數，讀到 EOF。",
        "idea": "試除到 sqrt(n)。先判 n，再判 reverse(n)。",
        "file": "027_10235_simply_emirp.py",
        "code": r'''
import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(math.isqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

for s in sys.stdin.read().split():
    n = int(s)
    r = int(s[::-1])
    if not is_prime(n):
        print(f"{n} is not prime.")
    elif r != n and is_prime(r):
        print(f"{n} is emirp.")
    else:
        print(f"{n} is prime.")
''',
        "tests": [("17\n18\n2\n", "17 is emirp.\n18 is not prime.\n2 is prime.\n")],
    },
    {
        "no": 28,
        "uva": "10242",
        "title": "Fourth Point!!",
        "zh": "平行四邊形給四個點，其中有一個點重複出現，求缺少的第四點。",
        "need": "每組 8 個浮點數，代表四個點。",
        "idea": "若 A 是重複點，答案 = 另外兩點相加 - A。",
        "file": "028_10242_fourth_point.py",
        "code": r'''
import sys

data = list(map(float, sys.stdin.read().split()))
for i in range(0, len(data), 8):
    pts = [(data[i+j], data[i+j+1]) for j in range(0, 8, 2)]
    ans = None
    for a in range(4):
        for b in range(a + 1, 4):
            if pts[a] == pts[b]:
                others = [pts[k] for k in range(4) if k not in (a, b)]
                ans = (others[0][0] + others[1][0] - pts[a][0],
                       others[0][1] + others[1][1] - pts[a][1])
    print(f"{ans[0]:.3f} {ans[1]:.3f}")
''',
        "tests": [("0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0\n", "1.000 1.000\n")],
    },
    {
        "no": 29,
        "uva": "10252",
        "title": "Common Permutation",
        "zh": "找兩個字串共同擁有的字母，依字母順序輸出，每個字母次數取兩邊較小值。",
        "need": "每兩行一組字串，讀到 EOF。",
        "idea": "Counter 交集後按字母排序。",
        "file": "029_10252_common_permutation.py",
        "code": r'''
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    a = Counter(lines[i])
    b = Counter(lines[i + 1])
    common = a & b
    print("".join(ch * common[ch] for ch in sorted(common)))
''',
        "tests": [("pretty\nwomen\nwalking\ndown\n", "e\nnw\n")],
    },
    {
        "no": 30,
        "uva": "10268",
        "title": "498-bis",
        "zh": "給 x 與多項式係數，求多項式在 x 的導數值。",
        "need": "每組兩行：第一行 x，第二行從高次到常數項係數。",
        "idea": "若係數有 n 個，第一個係數次方是 n-1；導數係數為 coef*power，用 Horner 算導數值。",
        "file": "030_10268_498_bis.py",
        "code": r'''
import sys

lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    x = int(lines[i])
    coeffs = list(map(int, lines[i + 1].split()))
    degree = len(coeffs) - 1
    ans = 0
    for idx, coef in enumerate(coeffs[:-1]):
        power = degree - idx
        ans = ans * x + coef * power
    print(ans)
''',
        "tests": [("7\n1 -1\n", "1\n")],
    },
    {
        "no": 31,
        "uva": "10409",
        "title": "Die Game",
        "zh": "骰子初始 top=1, north=2, west=3，依指令滾動後輸出最上面的數字。",
        "need": "多組，先給指令數 n，再給 n 行 north/south/east/west，以 0 結束。",
        "idea": "維護 top,bottom,north,south,east,west 六面，照方向交換。",
        "file": "031_10409_die_game.py",
        "code": r'''
import sys

lines = sys.stdin.read().splitlines()
p = 0
while p < len(lines):
    n = int(lines[p]); p += 1
    if n == 0:
        break
    top, bottom, north, south, east, west = 1, 6, 2, 5, 4, 3
    for _ in range(n):
        cmd = lines[p]; p += 1
        if cmd == "north":
            top, south, bottom, north = south, bottom, north, top
        elif cmd == "south":
            top, north, bottom, south = north, bottom, south, top
        elif cmd == "east":
            top, west, bottom, east = west, bottom, east, top
        elif cmd == "west":
            top, east, bottom, west = east, bottom, west, top
    print(top)
''',
        "tests": [("1\nnorth\n3\nnorth\neast\nsouth\n0\n", "5\n1\n")],
    },
    {
        "no": 32,
        "uva": "10415",
        "title": "Eb Alto Saxophone Player",
        "zh": "薩克斯風每個音會按一些手指，計算整首歌每根手指從沒按到按下的次數。",
        "need": "第一行測資數；每行一串音符。",
        "idea": "用表格記每個音按哪些指頭，逐字比較前一狀態與現在狀態。",
        "file": "032_10415_saxophone.py",
        "code": r'''
import sys

notes = {
    "c": "0111001111", "d": "0111001110", "e": "0111001100", "f": "0111001000",
    "g": "0111000000", "a": "0110000000", "b": "0100000000",
    "C": "0010000000", "D": "1111001110", "E": "1111001100", "F": "1111001000",
    "G": "1111000000", "A": "1110000000", "B": "1100000000",
}
lines = sys.stdin.read().splitlines()
t = int(lines[0])
for song in lines[1:1+t]:
    prev = "0000000000"
    ans = [0] * 10
    for ch in song:
        cur = notes[ch]
        for i in range(10):
            if prev[i] == "0" and cur[i] == "1":
                ans[i] += 1
        prev = cur
    print(" ".join(map(str, ans)))
''',
        "tests": [("1\ncdefgab\n", "0 1 1 1 0 0 1 1 1 1\n")],
    },
    {
        "no": 33,
        "uva": "10420",
        "title": "List of Conquests",
        "zh": "統計每個國家出現幾次，姓名部分不用管。",
        "need": "第一行 n；接著 n 行，每行第一個單字是國家。",
        "idea": "split(maxsplit=1) 取國名，Counter 後依國名字典序輸出。",
        "file": "033_10420_list_of_conquests.py",
        "code": r'''
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
n = int(lines[0])
cnt = Counter(line.split(maxsplit=1)[0] for line in lines[1:1+n])
for country in sorted(cnt):
    print(country, cnt[country])
''',
        "tests": [("3\nSpain Donna Elvira\nEngland Jane Doe\nSpain Maria\n", "England 1\nSpain 2\n")],
    },
    {
        "no": 34,
        "uva": "10642",
        "title": "Can You Solve It?",
        "zh": "在斜向編號座標系中，求從點 1 到點 2 的編號差。",
        "need": "第一行測資數；每組 x1 y1 x2 y2。",
        "idea": "座標 (x,y) 的序號可用三角數：s=x+y，id=s*(s+1)//2 + x。",
        "file": "034_10642_can_you_solve_it.py",
        "code": r'''
import sys

def pos(x, y):
    s = x + y
    return s * (s + 1) // 2 + x

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for case in range(1, t + 1):
    x1, y1, x2, y2 = data[p:p+4]; p += 4
    print(f"Case {case}: {pos(x2, y2) - pos(x1, y1)}")
''',
        "tests": [("1\n0 0 1 0\n", "Case 1: 2\n")],
    },
    {
        "no": 35,
        "uva": "10783",
        "title": "Odd Sum",
        "zh": "計算區間 [a,b] 中所有奇數的總和。",
        "need": "第一行測資數；每組 a b。",
        "idea": "範圍小可直接迴圈；考試好寫不易錯。",
        "file": "035_10783_odd_sum.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for case in range(1, t + 1):
    a, b = data[p], data[p + 1]; p += 2
    ans = sum(x for x in range(a, b + 1) if x % 2)
    print(f"Case {case}: {ans}")
''',
        "tests": [("2\n1\n5\n3\n5\n", "Case 1: 9\nCase 2: 8\n")],
    },
    {
        "no": 36,
        "uva": "10812",
        "title": "Beat the Spread!",
        "zh": "已知兩隊分數總和 s 與差 d，求兩隊分數；若不可能則輸出 impossible。",
        "need": "第一行測資數；每組 s d。",
        "idea": "大分=(s+d)/2，小分=(s-d)/2，必須非負且整數。",
        "file": "036_10812_beat_spread.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for _ in range(t):
    s, d = data[p], data[p + 1]; p += 2
    if s < d or (s + d) % 2:
        print("impossible")
    else:
        print((s + d) // 2, (s - d) // 2)
''',
        "tests": [("2\n40 20\n20 40\n", "30 10\nimpossible\n")],
    },
    {
        "no": 37,
        "uva": "10908",
        "title": "Largest Squares",
        "zh": "對每個查詢中心點，找最大奇數邊長正方形，使整個正方形字元都和中心字元相同。",
        "need": "第一行測資數；每組 M N Q，M 行字元矩陣，Q 個中心 r c。",
        "idea": "從半徑 0 往外擴，邊界超出或新方框有不同字元就停止。",
        "file": "037_10908_largest_squares.py",
        "code": r'''
import sys

lines = sys.stdin.read().splitlines()
t = int(lines[0])
p = 1
for _ in range(t):
    m, n, q = map(int, lines[p].split()); p += 1
    grid = lines[p:p+m]; p += m
    print(m, n, q)
    for _ in range(q):
        r, c = map(int, lines[p].split()); p += 1
        ch = grid[r][c]
        radius = 0
        while True:
            nr = radius + 1
            if r - nr < 0 or r + nr >= m or c - nr < 0 or c + nr >= n:
                break
            ok = True
            for i in range(r - nr, r + nr + 1):
                for j in range(c - nr, c + nr + 1):
                    if grid[i][j] != ch:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
            radius = nr
        print(2 * radius + 1)
''',
        "tests": [("1\n3 3 1\naaa\naaa\naaa\n1 1\n", "3 3 1\n3\n")],
    },
    {
        "no": 38,
        "uva": "10922",
        "title": "2 the 9s",
        "zh": "判斷大整數是否為 9 的倍數；若是，計算反覆各位數相加到 9 需要幾層，稱為 9-degree。",
        "need": "多行數字字串，以 0 結束。",
        "idea": "數位和不是 9 倍數就不是；是的話反覆 digit sum 計 degree。",
        "file": "038_10922_2_the_9s.py",
        "code": r'''
import sys

for s in sys.stdin.read().split():
    if s == "0":
        break
    total = sum(map(int, s))
    if total % 9 != 0:
        print(f"{s} is not a multiple of 9.")
    else:
        degree = 1
        while total != 9:
            total = sum(map(int, str(total)))
            degree += 1
        print(f"{s} is a multiple of 9 and has 9-degree {degree}.")
''',
        "tests": [("999999999999999999999\n9\n0\n", "999999999999999999999 is a multiple of 9 and has 9-degree 3.\n9 is a multiple of 9 and has 9-degree 1.\n")],
    },
    {
        "no": 39,
        "uva": "10929",
        "title": "You can say 11",
        "zh": "判斷大整數是否為 11 的倍數。",
        "need": "多行數字字串，以 0 結束。",
        "idea": "交錯位數和差若可被 11 整除，原數可被 11 整除。",
        "file": "039_10929_you_can_say_11.py",
        "code": r'''
import sys

for s in sys.stdin.read().split():
    if s == "0":
        break
    odd = sum(int(s[i]) for i in range(0, len(s), 2))
    even = sum(int(s[i]) for i in range(1, len(s), 2))
    if (odd - even) % 11 == 0:
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")
''',
        "tests": [("112233\n30800\n0\n", "112233 is a multiple of 11.\n30800 is a multiple of 11.\n")],
    },
    {
        "no": 40,
        "uva": "10931",
        "title": "Parity",
        "zh": "把 n 轉成二進位，輸出二進位字串與其中 1 的個數。",
        "need": "多個正整數，以 0 結束。",
        "idea": "bin(n)[2:] 取得二進位字串。",
        "file": "040_10931_parity.py",
        "code": r'''
import sys

for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break
    b = bin(n)[2:]
    print(f"The parity of {b} is {b.count('1')} (mod 2).")
''',
        "tests": [("21\n0\n", "The parity of 10101 is 3 (mod 2).\n")],
    },
    {
        "no": 41,
        "uva": "11005",
        "title": "Cheapest Base",
        "zh": "給每個數字 0-35 的印刷成本，對多個十進位數找出用哪個 base 2-36 表示時總成本最低。",
        "need": "第一行測資數；每組 36 個成本、查詢數 q、q 個數字。",
        "idea": "對每個 base 反覆取餘數計算成本，找最小值的所有 base。",
        "file": "041_11005_cheapest_base.py",
        "code": r'''
import sys

def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]
    total = 0
    while n:
        total += costs[n % base]
        n //= base
    return total

data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for case in range(1, t + 1):
    costs = data[p:p+36]; p += 36
    q = data[p]; p += 1
    print(f"Case {case}:")
    for _ in range(q):
        n = data[p]; p += 1
        vals = [(cost_in_base(n, b, costs), b) for b in range(2, 37)]
        best = min(v for v, _ in vals)
        bases = [str(b) for v, b in vals if v == best]
        print(f"Cheapest base(s) for number {n}: {' '.join(bases)}")
    if case != t:
        print()
''',
        "tests": [("1\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n1\n10\n", "Case 1:\nCheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n")],
    },
    {
        "no": 42,
        "uva": "11063",
        "title": "B2-Sequence",
        "zh": "判斷序列是否為 B2：正整數、嚴格遞增，且任兩項 i<=j 的和都不重複。",
        "need": "多組資料，每組 n 後接 n 個數。",
        "idea": "先檢查遞增與正數，再用 set 檢查所有 pair sum。",
        "file": "042_11063_b2_sequence.py",
        "code": r'''
import sys

data = list(map(int, sys.stdin.read().split()))
p = 0
case = 1
while p < len(data):
    n = data[p]; p += 1
    arr = data[p:p+n]; p += n
    ok = all(arr[i] > 0 and (i == 0 or arr[i] > arr[i-1]) for i in range(n))
    seen = set()
    if ok:
        for i in range(n):
            for j in range(i, n):
                s = arr[i] + arr[j]
                if s in seen:
                    ok = False
                    break
                seen.add(s)
            if not ok:
                break
    print(f"Case #{case}: It is {'a' if ok else 'not a'} B2-Sequence.")
    print()
    case += 1
''',
        "tests": [("4\n1 2 4 8\n4\n1 2 3 4\n", "Case #1: It is a B2-Sequence.\n\nCase #2: It is not a B2-Sequence.\n\n")],
    },
    {
        "no": 43,
        "uva": "11150",
        "title": "Cola",
        "zh": "喝完可樂的空瓶每 3 瓶可換 1 瓶，問最多能喝幾瓶；可以先借一瓶空瓶最後還。",
        "need": "多個 n，讀到 EOF。",
        "idea": "經典結果是 n + n//2；也可模擬含借瓶，公式最快。",
        "file": "043_11150_cola.py",
        "code": r'''
import sys

for n in map(int, sys.stdin.read().split()):
    print(n + n // 2)
''',
        "tests": [("3\n10\n81\n", "4\n15\n121\n")],
    },
    {
        "no": 44,
        "uva": "11321",
        "title": "Sort! Sort!! and Sort!!!",
        "zh": "依特殊規則排序：先按 n mod m 小到大；同餘時奇數排偶數前；奇數由大到小，偶數由小到大。",
        "need": "多組 n m，接著 n 個整數；以 0 0 結束。每組要先原樣輸出 n m。",
        "idea": "自訂排序 key：(x % m, odd/even rank, value rank)。Python 負數 % 結果和 C 不同，要自製 C 風格餘數。",
        "file": "044_11321_sort_sort.py",
        "code": r'''
import sys

def c_mod(x, m):
    return x % m if x >= 0 else -((-x) % m)

def key(x, m):
    if x % 2:
        return (c_mod(x, m), 0, -x)
    return (c_mod(x, m), 1, x)

data = list(map(int, sys.stdin.read().split()))
p = 0
out = []
while p < len(data):
    n, m = data[p], data[p + 1]; p += 2
    out.append(f"{n} {m}")
    if n == 0 and m == 0:
        break
    arr = data[p:p+n]; p += n
    out.extend(str(x) for x in sorted(arr, key=lambda x: key(x, m)))
print("\n".join(out))
''',
        "tests": [("5 3\n1\n2\n3\n4\n5\n0 0\n", "5 3\n3\n1\n4\n5\n2\n0 0\n")],
    },
    {
        "no": 45,
        "uva": "11332",
        "title": "Summing Digits",
        "zh": "反覆把數字各位數相加，直到變成一位數。",
        "need": "多個正整數，以 0 結束。",
        "idea": "直接用 digital root：n%9，若餘 0 則答案 9。",
        "file": "045_11332_summing_digits.py",
        "code": r'''
import sys

for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break
    print(9 if n % 9 == 0 else n % 9)
''',
        "tests": [("2\n11\n47\n1234567892\n0\n", "2\n2\n2\n2\n")],
    },
    {
        "no": 46,
        "uva": "11349",
        "title": "Symmetric Matrix",
        "zh": "判斷 n*n 矩陣是否對中心對稱，且所有元素不可為負。",
        "need": "第一行測資數；每組格式 `N = n` 後接 n*n 個整數。",
        "idea": "把矩陣攤平成 list，檢查每個值 >=0 且 arr[i] == arr[-1-i]。",
        "file": "046_11349_symmetric_matrix.py",
        "code": r'''
import sys

tokens = sys.stdin.read().replace("=", " ").split()
t = int(tokens[0])
p = 1
for case in range(1, t + 1):
    p += 1  # 跳過 N
    n = int(tokens[p]); p += 1
    arr = list(map(int, tokens[p:p+n*n])); p += n*n
    ok = all(x >= 0 for x in arr) and arr == arr[::-1]
    print(f"Test #{case}: {'Symmetric.' if ok else 'Non-symmetric.'}")
''',
        "tests": [("1\nN = 2\n1 2\n2 1\n", "Test #1: Symmetric.\n")],
    },
    {
        "no": 47,
        "uva": "11417",
        "title": "GCD",
        "zh": "對 1 <= i < j <= N 的所有配對，計算 gcd(i,j) 總和。",
        "need": "多個 N，以 0 結束。",
        "idea": "N 最大不大，雙迴圈加 math.gcd 最簡單。",
        "file": "047_11417_gcd.py",
        "code": r'''
import sys
from math import gcd

for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    print(total)
''',
        "tests": [("10\n100\n0\n", "67\n13015\n")],
    },
    {
        "no": 48,
        "uva": "11461",
        "title": "Square Numbers",
        "zh": "計算閉區間 [a,b] 中有幾個完全平方數。",
        "need": "多組 a b，以 0 0 結束。",
        "idea": "答案是 floor(sqrt(b)) - ceil(sqrt(a)) + 1。",
        "file": "048_11461_square_numbers.py",
        "code": r'''
import sys
import math

data = list(map(int, sys.stdin.read().split()))
for i in range(0, len(data), 2):
    a, b = data[i], data[i + 1]
    if a == 0 and b == 0:
        break
    lo = math.isqrt(a - 1) + 1
    hi = math.isqrt(b)
    print(max(0, hi - lo + 1))
''',
        "tests": [("1 4\n1 10\n0 0\n", "2\n3\n")],
    },
    {
        "no": 49,
        "uva": "12019",
        "title": "Doom's Day Algorithm",
        "zh": "給 2011 年的月日，輸出那天是星期幾。",
        "need": "第一行測資數；每組 month day。",
        "idea": "直接用 2011 年每月天數累積，已知 2011/1/1 是 Saturday。",
        "file": "049_12019_dooms_day.py",
        "code": r'''
import sys

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
for _ in range(t):
    m, d = data[p], data[p + 1]; p += 2
    day_of_year = sum(month_days[:m-1]) + d
    print(days[day_of_year % 7])
''',
        "tests": [("3\n1 6\n2 28\n12 25\n", "Thursday\nMonday\nSunday\n")],
    },
]


def clean(code):
    return textwrap.dedent(code).strip() + "\n"


def with_learning_notes(problem):
    code = clean(problem["code"])
    if code.startswith('"""'):
        return code

    code = add_common_code_comments(code)
    header = f'''"""
UVA {problem["uva"]} - {problem["title"]}

題目中文意思：
{problem["zh"]}

這題需要什麼資料：
{problem["need"]}

解法重點：
{problem["idea"]}

寫程式時可以照這個順序想：
1. 先把輸入讀進來，確認是一行一組、第一行有測資數，還是讀到 EOF。
2. 把題目要的規則轉成變數、迴圈、判斷式或函式。
3. 按照題目指定格式輸出，CPE/UVA 很常因為空格、空行、大小寫錯而 WA。
"""

# ===== 程式開始 =====
# 下面保留可以直接提交的 Python 解答。
# 註解會寫「這行在做什麼」以及「為什麼要這樣做」，
# 你用 Cursor 看時，可以先讀上面的題目說明，再對照下面程式。

'''
    return textwrap.dedent(header) + code


def add_common_code_comments(code):
    comments = {
        "import sys": "# 匯入 sys：CPE/UVA 常用 sys.stdin 讀輸入，速度快，也能自然讀到 EOF。",
        "import math": "# 匯入 math：需要 sqrt、sin、radians、isqrt 這類數學函式時使用。",
        "from collections import Counter": "# Counter 是計數工具，適合統計字母、樹名、國家等出現次數。",
        "from math import gcd": "# gcd 用來求最大公因數，直接用內建函式比自己寫更快更不容易錯。",
        "data = list(map(int, sys.stdin.read().split()))": "# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。",
        "tokens = sys.stdin.read().split()": "# 一次讀完所有 token：保留字串型態，之後需要時再轉 int/float。",
        "lines = sys.stdin.read().splitlines()": "# splitlines() 逐行保留資料，適合每一行都有意義的題目。",
        "lines = sys.stdin.read().splitlines()": "# splitlines() 逐行保留資料，適合每一行都有意義的題目。",
        "for line in sys.stdin:": "# 逐行讀到 EOF：不知道有幾筆測資時最常用這種寫法。",
        "if not line.strip():": "# 如果遇到空白行就跳過，避免 split 後沒有資料造成錯誤。",
        "continue": "# continue 代表跳過這一輪，直接讀下一行或下一筆資料。",
        "break": "# break 代表題目的結束條件成立，離開目前迴圈。",
        "print()": "# 題目要求測資之間空一行時，直接 print() 輸出空白行。",
    }

    starts = [
        ("print(", "# print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。"),
        ("for ", "# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。"),
        ("while ", "# while 迴圈適合「做到某個條件成立為止」的模擬題。"),
        ("if ", "# if 判斷題目的特殊情況或規則分支。"),
        ("elif ", "# elif 是第二種判斷情況，讓不同規則分開處理。"),
        ("else:", "# else 處理前面條件都不成立時的情況。"),
        ("return ", "# return 把函式算出的結果交回呼叫它的地方。"),
        ("def ", "# def 定義函式，把會重複使用的邏輯整理起來。"),
    ]

    result = []
    last_comment = None
    for line in code.splitlines():
        stripped = line.strip()
        indent = line[:len(line) - len(line.lstrip())]
        comment = comments.get(stripped)
        if comment is None:
            for prefix, candidate in starts:
                if stripped.startswith(prefix):
                    comment = candidate
                    break
        if comment and comment != last_comment:
            result.append(indent + comment)
            last_comment = comment
        else:
            last_comment = None if stripped else last_comment
        result.append(line)
    return "\n".join(result).strip() + "\n"


def write_solutions():
    OUT.mkdir(exist_ok=True)
    for p in PROBLEMS:
        path = OUT / p["file"]
        path.write_text(with_learning_notes(p), encoding="utf-8")


def write_readme():
    lines = [
        "# CPE 一星 49 題中文整理與 Python 解答",
        "",
        "來源清單：<https://yuihuang.com/cpe-level-1-49/>",
        "",
        "使用方式：每題對應 `solutions/` 裡的一個 `.py` 檔。打開後可以直接貼到 ZeroJudge / UVA 類型平台；註解都保留在程式裡，方便你用 Cursor 快速看懂。",
        "",
        "準備策略：一星題大多是輸入輸出、模擬、排序、字串、簡單數學。考前先把每題的「需要資料」和「解題核心」背熟，再練習自己重打一次程式。",
        "",
    ]
    for p in PROBLEMS:
        lines += [
            f"## {p['no']:02d}. UVA {p['uva']} - {p['title']}",
            "",
            f"中文意思：{p['zh']}",
            "",
            f"這題需要什麼資料：{p['need']}",
            "",
            f"解題核心：{p['idea']}",
            "",
            f"Python 解答檔：[`solutions/{p['file']}`](solutions/{p['file']})",
            "",
        ]
    (ROOT / "CPE一星49題總整理.md").write_text("\n".join(lines), encoding="utf-8")


def write_tests():
    body = r'''
import subprocess
import sys
from pathlib import Path
from generate_cpe_pack import PROBLEMS

ROOT = Path(__file__).resolve().parent

def main():
    passed = 0
    total = 0
    for problem in PROBLEMS:
        script = ROOT / "solutions" / problem["file"]
        for sample_in, expected in problem.get("tests", []):
            total += 1
            result = subprocess.run(
                [sys.executable, str(script)],
                input=sample_in,
                text=True,
                capture_output=True,
                timeout=5,
            )
            if result.returncode != 0:
                print(f"FAIL {problem['no']:02d} {problem['uva']} runtime error")
                print(result.stderr)
                return 1
            if result.stdout != expected:
                print(f"FAIL {problem['no']:02d} {problem['uva']}")
                print("Expected:")
                print(repr(expected))
                print("Got:")
                print(repr(result.stdout))
                return 1
            passed += 1
    print(f"All {passed}/{total} sample checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''
    (ROOT / "run_sample_tests.py").write_text(clean(body), encoding="utf-8")


def main():
    write_solutions()
    write_readme()
    write_tests()
    print(f"Generated {len(PROBLEMS)} solutions in {OUT}")


if __name__ == "__main__":
    main()
