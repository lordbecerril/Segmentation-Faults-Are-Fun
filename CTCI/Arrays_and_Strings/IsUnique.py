'''
Implement an algorithm to determine if a string has all unique character.
What if you cannot use additional data structures?
'''

def isUnique(s):
    return len(set(s)) == len(s)


def main():
    string1 = 'asdfwe4$'
    string2 = 'asdfdd'
    string3 = ''
    string4 = 'a'

    # Brute Force is to go through each character
    print(isUnique(string1))
    print(isUnique(string2))
    print(isUnique(string3))
    print(isUnique(string4))

if __name__ == '__main__':
    main()
