''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    """
    This function reads a sentence from input, and prints a substring based on the start and end index provided.
    """
    sentence = input()
    start_index = int(input())
    end_index = int(input()) + 1

    print(sentence[start_index:end_index])

main()

