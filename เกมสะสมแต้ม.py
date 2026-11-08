"""เกมสะสมแต้ม"""
def main():
    """เกมสะสมแต้ม"""
    num = int(input())
    total = 0
    for _ in range(num):
        mark = input()
        if mark == "+":
            total += 10
        elif mark == "-":
            total -= 5
    print(total)
main()
