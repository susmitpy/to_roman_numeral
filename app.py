# For testing
import roman

"""
Symbol  Value
I        1
V        5
X        10
L        50
C        100
D        500
M        1000

XL = L (50) - X (10) = 40
CD = D (500) - C (100) = 400
CM = M (1000) - C (100) = 900
"""

def check_rules(s):
    ans = s
    # (V) 5 + (IV) 4 = (IX) 9 
    ans = ans.replace("VIV", "IX")

    # (L) 50 + (XL) 40 = (XC) 90
    ans = ans.replace("LXL", "XC")

    # (D) 500 + (CD) 400 = (CM) 900
    ans = ans.replace("DCD", "CM")
    
    return ans

def parse(s):
    last_char = None
    last_count = 0
    temp = []
    final = []
    for c in s:
        temp.append(c)
        if last_char is None:
            last_char = c
            last_count = 1
            continue
        
        if last_char == c:
            last_count += 1
            if last_count == 4:
                if last_char == "I":
                    final.append("IV")
                    temp.clear()
                elif last_char == "X":
                    final.append("XL")
                    temp.clear()
                elif last_char == "C":
                    final.append("CD")
                    temp.clear()
        else:
            last_char = c
            last_count = 1

            final.extend(temp[:-1])
            temp = temp[-1:]
    final.extend(temp)
    return "".join(final)

def to_roman(n: int) -> str:
    ans = ""
    symbols = ["M", "D", "C", "L", "X", "V", "I"]
    vals = [1000, 500, 100, 50, 10, 5, 1]
    for ind, val in enumerate(vals):
        for _ in range(n // val):
            ans += symbols[ind]
        n = n % val
    return check_rules(parse(ans))


def tests():
    # Test Cases used during development
    test_cases = {
        32 : "XXXII",
        1676 : "MDCLXXVI",
        521 : "DXXI",
        34: "XXXIV",
        49: "XLIX",
        94 : "XCIV",
        99: "XCIX",
        999: "CMXCIX",
        3999 : "MMMCMXCIX"
    }

    for ip, op in test_cases.items():
        opr = to_roman(ip)
        result = "Correct" if op == opr else "Incorrect"
        print(f"I/P : {ip} O/P: {op} O/P Returned: {opr} {result}")

    print("Testing for numbers from 1 to 3999 usnig roman library")
    num_correct = num_incorrect = 0
    incorrects = []
    for num in range(1,4000):
        if roman.toRoman(num) == to_roman(num):
            num_correct += 1
        else:
            num_incorrect+=1
            incorrects.append(num)

    print("Done")
    print(f"Correct: {num_correct}\nIncorrect : {num_incorrect}\nIncorrects: {incorrects}")

tests()
