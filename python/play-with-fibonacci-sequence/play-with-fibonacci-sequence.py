''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    a = 0
    b = 1
    arr = [a, b]
    for i in range(n - 2):
        arr.append(a + b)
        a, b = b, a + b
    
    print(" ".join(map(str, arr)))

main()

