"""Problem3"""

def main():
    """Problem3"""
    word = str(input())
    if len(word) == 5:
        print(word[::-1].lower())
    else:
        print("Error")
main()
