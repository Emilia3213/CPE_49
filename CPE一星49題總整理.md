# CPE 一星 49 題中文整理與 Python 解答

來源清單：<https://yuihuang.com/cpe-level-1-49/>

使用方式：每題對應 `solutions/` 裡的一個 `.py` 檔。打開後可以直接貼到 ZeroJudge / UVA 類型平台；註解都保留在程式裡，方便你用 Cursor 快速看懂。

準備策略：一星題大多是輸入輸出、模擬、排序、字串、簡單數學。考前先把每題的「需要資料」和「解題核心」背熟，再練習自己重打一次程式。

## 01. UVA 100 - The 3n + 1 problem

中文意思：給兩個整數 i, j，找出區間內每個數做 Collatz 規則後的循環長度，輸出最大循環長度。

這題需要什麼資料：每行兩個整數；輸出原本順序的 i j 與閉區間 [min(i,j), max(i,j)] 的最大 cycle length。

解題核心：逐數計算 Collatz 長度並用快取避免重算。注意輸入順序要原樣輸出。

Python 解答檔：[`solutions/001_100_3n_plus_1.py`](solutions/001_100_3n_plus_1.py)

## 02. UVA 118 - Mutant Flatworld Explorers

中文意思：機器人在矩形世界中依指令移動；若走出邊界會掉落並留下氣味，之後其他機器人在同位置同方向會忽略該掉落指令。

這題需要什麼資料：第一行右上角座標；之後每組為 x y 方向與一行指令。方向 N/E/S/W，指令 L/R/F。

解題核心：模擬方向轉換與前進。掉落位置用 set 記錄 (x,y,dir)。

Python 解答檔：[`solutions/002_118_mutant_flatworld_explorers.py`](solutions/002_118_mutant_flatworld_explorers.py)

## 03. UVA 272 - TeX Quotes

中文意思：把文章中的雙引號依序替換成 TeX 的左引號 `` 與右引號 ''。

這題需要什麼資料：任意多行文字，保留其他字元與換行。

解題核心：遇到 `"` 時用布林值交替輸出開引號與關引號。

Python 解答檔：[`solutions/003_272_tex_quotes.py`](solutions/003_272_tex_quotes.py)

## 04. UVA 299 - Train Swapping

中文意思：計算火車車廂用相鄰交換排成遞增順序時，最少需要交換幾次。

這題需要什麼資料：第一行測資數；每組給車廂數 n，再給 n 個車廂編號。

解題核心：相鄰交換次數等於逆序數；n 小，雙迴圈數逆序即可。

Python 解答檔：[`solutions/004_299_train_swapping.py`](solutions/004_299_train_swapping.py)

## 05. UVA 490 - Rotating Sentences

中文意思：把多行文字順時針旋轉 90 度，短行缺的地方用空白補齊。

這題需要什麼資料：讀到 EOF 的所有行；輸出旋轉後文字。

解題核心：找到最大寬度，將每行右側補空白，再從左欄到右欄、由下往上輸出。

Python 解答檔：[`solutions/005_490_rotating_sentences.py`](solutions/005_490_rotating_sentences.py)

## 06. UVA 948 - Fibonaccimal Base

中文意思：把十進位正整數轉成 Fibonacci 進位表示法，也就是用不相鄰的 Fibonacci 數相加。

這題需要什麼資料：第一行測資數；每行一個 n，輸出 `n = bits (fib)`。

解題核心：預先產生 1,2,3,5...，由大到小貪心取用。

Python 解答檔：[`solutions/006_948_fibonaccimal_base.py`](solutions/006_948_fibonaccimal_base.py)

## 07. UVA 10008 - What's Cryptanalysis

中文意思：統計文章中英文字母出現次數，不分大小寫，依次數多到少、同次數按字母 A-Z 輸出。

這題需要什麼資料：第一行 n，接著 n 行文字。

解題核心：只統計 A-Z；排序 key 使用 (-count, letter)。

Python 解答檔：[`solutions/007_10008_whats_cryptanalysis.py`](solutions/007_10008_whats_cryptanalysis.py)

## 08. UVA 10019 - Funny Encryption Method

中文意思：對每個十進位數 n，分別計算 n 的二進位 1 的數量，以及把 n 的十進位每位當作十六進位字串後的 1 的數量。

這題需要什麼資料：第一行測資數；每行一個整數。

解題核心：b1 = bin(n).count('1')；b2 = bin(int(str(n),16)).count('1')。

Python 解答檔：[`solutions/008_10019_funny_encryption_method.py`](solutions/008_10019_funny_encryption_method.py)

## 09. UVA 10035 - Primary Arithmetic

中文意思：計算兩個非負整數直式加法時產生幾次進位。

這題需要什麼資料：多組 a b，以 `0 0` 結束。

解題核心：從個位數往前加，記錄 carry，每次和 >=10 就多一次進位。

Python 解答檔：[`solutions/009_10035_primary_arithmetic.py`](solutions/009_10035_primary_arithmetic.py)

## 10. UVA 10038 - Jolly Jumpers

中文意思：長度 n 的序列若相鄰差的絕對值剛好包含 1 到 n-1 各一次，就是 Jolly。

這題需要什麼資料：每行一組：n 後面接 n 個整數。

解題核心：建立相鄰差集合，檢查是否等於 {1..n-1}。

Python 解答檔：[`solutions/010_10038_jolly_jumpers.py`](solutions/010_10038_jolly_jumpers.py)

## 11. UVA 10041 - Vito's family

中文意思：找一個街號讓所有親戚到該處的距離總和最小。

這題需要什麼資料：第一行測資數；每組第一個數是親戚數 r，後面 r 個街號。

解題核心：一維絕對距離總和最小點是中位數。

Python 解答檔：[`solutions/011_10041_vitos_family.py`](solutions/011_10041_vitos_family.py)

## 12. UVA 10050 - Hartals

中文意思：多個政黨每隔 h 天罷工，計算 n 天內有多少工作日受罷工影響；週五、週六不算。

這題需要什麼資料：第一行測資數；每組 n、政黨數 p、接著 p 個 hartal 參數。

解題核心：逐天檢查是否非週末且能被任一 h 整除。UVA 的第 6、7 天是週五、週六。

Python 解答檔：[`solutions/012_10050_hartals.py`](solutions/012_10050_hartals.py)

## 13. UVA 10055 - Hashmat the Brave Warrior

中文意思：給兩個軍隊人數，輸出差的絕對值。

這題需要什麼資料：每行兩個非負整數，讀到 EOF。

解題核心：直接 abs(a-b)。

Python 解答檔：[`solutions/013_10055_hashmat.py`](solutions/013_10055_hashmat.py)

## 14. UVA 10056 - What is the Probability?

中文意思：n 個人輪流嘗試成功機率 p 的事件，求第 i 個人最先成功的機率。

這題需要什麼資料：第一行測資數；每組 n p i。

解題核心：第 i 人第一次輪到就成功或前面整輪都失敗後成功：p*(1-p)^(i-1) / (1-(1-p)^n)。若 p=0 則 0。

Python 解答檔：[`solutions/014_10056_probability.py`](solutions/014_10056_probability.py)

## 15. UVA 10057 - A mid-summer night's dream

中文意思：給一堆數字，找所有能讓絕對距離總和最小的 A，輸出一個 A、原資料中等於可行 A 的數量、可行 A 的個數。

這題需要什麼資料：多組資料，每組先給 n，再給 n 個整數。

解題核心：排序後，中位區間 [arr[(n-1)//2], arr[n//2]] 都可行。

Python 解答檔：[`solutions/015_10057_midsummer.py`](solutions/015_10057_midsummer.py)

## 16. UVA 10062 - Tell me the frequencies!

中文意思：統計每行文字中各 ASCII 字元出現次數，依次數小到大，次數相同 ASCII 大到小輸出。

這題需要什麼資料：多行文字；不同輸入行的答案間要空一行。

解題核心：Counter 每行，排序 key=(count, -ord)。

Python 解答檔：[`solutions/016_10062_frequencies.py`](solutions/016_10062_frequencies.py)

## 17. UVA 10071 - Back to High School Physics

中文意思：已知速度 v 和時間 t，求等加速度對稱運動在 2t 時的位移。

這題需要什麼資料：每行兩個整數 v t。

解題核心：題目公式就是 2*v*t。

Python 解答檔：[`solutions/017_10071_physics.py`](solutions/017_10071_physics.py)

## 18. UVA 10093 - An Easy Problem!

中文意思：給一串由 0-9、A-Z、a-z 組成的數，找最小進位 base，使這個數能被 base-1 整除。

這題需要什麼資料：多行字串，讀到 EOF；忽略非英數字元。

解題核心：字元值最大值 + 1 是最低 base；base 範圍至少 2 到 62。利用 N mod (base-1) 等於各位值總和 mod (base-1)。

Python 解答檔：[`solutions/018_10093_easy_problem.py`](solutions/018_10093_easy_problem.py)

## 19. UVA 10101 - Bangla Numbers

中文意思：把整數轉成 Bangla 計數單位格式：kuti, lakh, hajar, shata。

這題需要什麼資料：多行非負整數；每行輸出編號加轉換結果。

解題核心：每 7 位會重複 kuti；遞迴處理高位，再處理 lakh/hajar/shata/個位。

Python 解答檔：[`solutions/019_10101_bangla_numbers.py`](solutions/019_10101_bangla_numbers.py)

## 20. UVA 10170 - The Hotel with Infinite Rooms

中文意思：第 1 天住 S 人，之後每天人數加 1，找累積人數第一次達到或超過 D 的那天人數。

這題需要什麼資料：多組 S D，讀到 EOF。

解題核心：從 S 開始累加直到 sum >= D。數字不大時最直觀，也可用公式；這裡用 while 容易記。

Python 解答檔：[`solutions/020_10170_infinite_rooms.py`](solutions/020_10170_infinite_rooms.py)

## 21. UVA 10189 - Minesweeper

中文意思：給踩地雷盤面，將非地雷格改成周圍八格地雷數。

這題需要什麼資料：多組 n m 與 n 行盤面，以 0 0 結束；輸出 Field #k。

解題核心：對每個非 * 格檢查八方向。

Python 解答檔：[`solutions/021_10189_minesweeper.py`](solutions/021_10189_minesweeper.py)

## 22. UVA 10190 - Divide, But Not Quite Conquer!

中文意思：判斷 n 是否能一直除以 m，最後剛好變成 1；可以則輸出整個序列，否則 Boring!。

這題需要什麼資料：多組 n m，讀到 EOF。

解題核心：m 必須大於 1，且每一步 n 都要能被 m 整除。

Python 解答檔：[`solutions/022_10190_divide.py`](solutions/022_10190_divide.py)

## 23. UVA 10193 - All You Need Is Love

中文意思：兩個二進位數若轉十進位後最大公因數大於 1，就代表有共同因子。

這題需要什麼資料：第一行測資數；每組兩行二進位字串。

解題核心：int(s, 2) 轉換後用 gcd。

Python 解答檔：[`solutions/023_10193_love.py`](solutions/023_10193_love.py)

## 24. UVA 10221 - Satellites

中文意思：已知地球表面上方高度 s 與中心角 a，計算弧長與弦長；角度可能是 degree 或 minute。

這題需要什麼資料：多組 s a unit；地球半徑固定 6440。

解題核心：minute 要除以 60 變 degree；大於 180 度取較小角 360-a；再轉弧度計算。

Python 解答檔：[`solutions/024_10221_satellites.py`](solutions/024_10221_satellites.py)

## 25. UVA 10222 - Decode the Mad man

中文意思：把輸入字元換成鍵盤上左邊第二個鍵，還原打錯位置的文字。

這題需要什麼資料：任意文字到 EOF；保留換行。

解題核心：建立鍵盤字串，每個可見字元找 index 後輸出 index-2 的字。

Python 解答檔：[`solutions/025_10222_decode_mad_man.py`](solutions/025_10222_decode_mad_man.py)

## 26. UVA 10226 - Hardwood Species

中文意思：統計每種樹名在森林資料中的百分比。

這題需要什麼資料：第一行測資數，空白行分隔測資；每組多行樹名。

解題核心：每組用 Counter 計數，按樹名字典序輸出比例到小數四位。

Python 解答檔：[`solutions/026_10226_hardwood_species.py`](solutions/026_10226_hardwood_species.py)

## 27. UVA 10235 - Simply Emirp

中文意思：判斷 n 是否為質數；若 n 與反轉後的數都是不同的質數，則是 emirp。

這題需要什麼資料：多個整數，讀到 EOF。

解題核心：試除到 sqrt(n)。先判 n，再判 reverse(n)。

Python 解答檔：[`solutions/027_10235_simply_emirp.py`](solutions/027_10235_simply_emirp.py)

## 28. UVA 10242 - Fourth Point!!

中文意思：平行四邊形給四個點，其中有一個點重複出現，求缺少的第四點。

這題需要什麼資料：每組 8 個浮點數，代表四個點。

解題核心：若 A 是重複點，答案 = 另外兩點相加 - A。

Python 解答檔：[`solutions/028_10242_fourth_point.py`](solutions/028_10242_fourth_point.py)

## 29. UVA 10252 - Common Permutation

中文意思：找兩個字串共同擁有的字母，依字母順序輸出，每個字母次數取兩邊較小值。

這題需要什麼資料：每兩行一組字串，讀到 EOF。

解題核心：Counter 交集後按字母排序。

Python 解答檔：[`solutions/029_10252_common_permutation.py`](solutions/029_10252_common_permutation.py)

## 30. UVA 10268 - 498-bis

中文意思：給 x 與多項式係數，求多項式在 x 的導數值。

這題需要什麼資料：每組兩行：第一行 x，第二行從高次到常數項係數。

解題核心：若係數有 n 個，第一個係數次方是 n-1；導數係數為 coef*power，用 Horner 算導數值。

Python 解答檔：[`solutions/030_10268_498_bis.py`](solutions/030_10268_498_bis.py)

## 31. UVA 10409 - Die Game

中文意思：骰子初始 top=1, north=2, west=3，依指令滾動後輸出最上面的數字。

這題需要什麼資料：多組，先給指令數 n，再給 n 行 north/south/east/west，以 0 結束。

解題核心：維護 top,bottom,north,south,east,west 六面，照方向交換。

Python 解答檔：[`solutions/031_10409_die_game.py`](solutions/031_10409_die_game.py)

## 32. UVA 10415 - Eb Alto Saxophone Player

中文意思：薩克斯風每個音會按一些手指，計算整首歌每根手指從沒按到按下的次數。

這題需要什麼資料：第一行測資數；每行一串音符。

解題核心：用表格記每個音按哪些指頭，逐字比較前一狀態與現在狀態。

Python 解答檔：[`solutions/032_10415_saxophone.py`](solutions/032_10415_saxophone.py)

## 33. UVA 10420 - List of Conquests

中文意思：統計每個國家出現幾次，姓名部分不用管。

這題需要什麼資料：第一行 n；接著 n 行，每行第一個單字是國家。

解題核心：split(maxsplit=1) 取國名，Counter 後依國名字典序輸出。

Python 解答檔：[`solutions/033_10420_list_of_conquests.py`](solutions/033_10420_list_of_conquests.py)

## 34. UVA 10642 - Can You Solve It?

中文意思：在斜向編號座標系中，求從點 1 到點 2 的編號差。

這題需要什麼資料：第一行測資數；每組 x1 y1 x2 y2。

解題核心：座標 (x,y) 的序號可用三角數：s=x+y，id=s*(s+1)//2 + x。

Python 解答檔：[`solutions/034_10642_can_you_solve_it.py`](solutions/034_10642_can_you_solve_it.py)

## 35. UVA 10783 - Odd Sum

中文意思：計算區間 [a,b] 中所有奇數的總和。

這題需要什麼資料：第一行測資數；每組 a b。

解題核心：範圍小可直接迴圈；考試好寫不易錯。

Python 解答檔：[`solutions/035_10783_odd_sum.py`](solutions/035_10783_odd_sum.py)

## 36. UVA 10812 - Beat the Spread!

中文意思：已知兩隊分數總和 s 與差 d，求兩隊分數；若不可能則輸出 impossible。

這題需要什麼資料：第一行測資數；每組 s d。

解題核心：大分=(s+d)/2，小分=(s-d)/2，必須非負且整數。

Python 解答檔：[`solutions/036_10812_beat_spread.py`](solutions/036_10812_beat_spread.py)

## 37. UVA 10908 - Largest Squares

中文意思：對每個查詢中心點，找最大奇數邊長正方形，使整個正方形字元都和中心字元相同。

這題需要什麼資料：第一行測資數；每組 M N Q，M 行字元矩陣，Q 個中心 r c。

解題核心：從半徑 0 往外擴，邊界超出或新方框有不同字元就停止。

Python 解答檔：[`solutions/037_10908_largest_squares.py`](solutions/037_10908_largest_squares.py)

## 38. UVA 10922 - 2 the 9s

中文意思：判斷大整數是否為 9 的倍數；若是，計算反覆各位數相加到 9 需要幾層，稱為 9-degree。

這題需要什麼資料：多行數字字串，以 0 結束。

解題核心：數位和不是 9 倍數就不是；是的話反覆 digit sum 計 degree。

Python 解答檔：[`solutions/038_10922_2_the_9s.py`](solutions/038_10922_2_the_9s.py)

## 39. UVA 10929 - You can say 11

中文意思：判斷大整數是否為 11 的倍數。

這題需要什麼資料：多行數字字串，以 0 結束。

解題核心：交錯位數和差若可被 11 整除，原數可被 11 整除。

Python 解答檔：[`solutions/039_10929_you_can_say_11.py`](solutions/039_10929_you_can_say_11.py)

## 40. UVA 10931 - Parity

中文意思：把 n 轉成二進位，輸出二進位字串與其中 1 的個數。

這題需要什麼資料：多個正整數，以 0 結束。

解題核心：bin(n)[2:] 取得二進位字串。

Python 解答檔：[`solutions/040_10931_parity.py`](solutions/040_10931_parity.py)

## 41. UVA 11005 - Cheapest Base

中文意思：給每個數字 0-35 的印刷成本，對多個十進位數找出用哪個 base 2-36 表示時總成本最低。

這題需要什麼資料：第一行測資數；每組 36 個成本、查詢數 q、q 個數字。

解題核心：對每個 base 反覆取餘數計算成本，找最小值的所有 base。

Python 解答檔：[`solutions/041_11005_cheapest_base.py`](solutions/041_11005_cheapest_base.py)

## 42. UVA 11063 - B2-Sequence

中文意思：判斷序列是否為 B2：正整數、嚴格遞增，且任兩項 i<=j 的和都不重複。

這題需要什麼資料：多組資料，每組 n 後接 n 個數。

解題核心：先檢查遞增與正數，再用 set 檢查所有 pair sum。

Python 解答檔：[`solutions/042_11063_b2_sequence.py`](solutions/042_11063_b2_sequence.py)

## 43. UVA 11150 - Cola

中文意思：喝完可樂的空瓶每 3 瓶可換 1 瓶，問最多能喝幾瓶；可以先借一瓶空瓶最後還。

這題需要什麼資料：多個 n，讀到 EOF。

解題核心：經典結果是 n + n//2；也可模擬含借瓶，公式最快。

Python 解答檔：[`solutions/043_11150_cola.py`](solutions/043_11150_cola.py)

## 44. UVA 11321 - Sort! Sort!! and Sort!!!

中文意思：依特殊規則排序：先按 n mod m 小到大；同餘時奇數排偶數前；奇數由大到小，偶數由小到大。

這題需要什麼資料：多組 n m，接著 n 個整數；以 0 0 結束。每組要先原樣輸出 n m。

解題核心：自訂排序 key：(x % m, odd/even rank, value rank)。Python 負數 % 結果和 C 不同，要自製 C 風格餘數。

Python 解答檔：[`solutions/044_11321_sort_sort.py`](solutions/044_11321_sort_sort.py)

## 45. UVA 11332 - Summing Digits

中文意思：反覆把數字各位數相加，直到變成一位數。

這題需要什麼資料：多個正整數，以 0 結束。

解題核心：直接用 digital root：n%9，若餘 0 則答案 9。

Python 解答檔：[`solutions/045_11332_summing_digits.py`](solutions/045_11332_summing_digits.py)

## 46. UVA 11349 - Symmetric Matrix

中文意思：判斷 n*n 矩陣是否對中心對稱，且所有元素不可為負。

這題需要什麼資料：第一行測資數；每組格式 `N = n` 後接 n*n 個整數。

解題核心：把矩陣攤平成 list，檢查每個值 >=0 且 arr[i] == arr[-1-i]。

Python 解答檔：[`solutions/046_11349_symmetric_matrix.py`](solutions/046_11349_symmetric_matrix.py)

## 47. UVA 11417 - GCD

中文意思：對 1 <= i < j <= N 的所有配對，計算 gcd(i,j) 總和。

這題需要什麼資料：多個 N，以 0 結束。

解題核心：N 最大不大，雙迴圈加 math.gcd 最簡單。

Python 解答檔：[`solutions/047_11417_gcd.py`](solutions/047_11417_gcd.py)

## 48. UVA 11461 - Square Numbers

中文意思：計算閉區間 [a,b] 中有幾個完全平方數。

這題需要什麼資料：多組 a b，以 0 0 結束。

解題核心：答案是 floor(sqrt(b)) - ceil(sqrt(a)) + 1。

Python 解答檔：[`solutions/048_11461_square_numbers.py`](solutions/048_11461_square_numbers.py)

## 49. UVA 12019 - Doom's Day Algorithm

中文意思：給 2011 年的月日，輸出那天是星期幾。

這題需要什麼資料：第一行測資數；每組 month day。

解題核心：直接用 2011 年每月天數累積，已知 2011/1/1 是 Saturday。

Python 解答檔：[`solutions/049_12019_dooms_day.py`](solutions/049_12019_dooms_day.py)
