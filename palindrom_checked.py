'''def is_palindrome (n):
    n=12321
    r=12321
    original=n
    reversed_num =r

    while n>r:
        reminder =n%10
        reversed_num=(reversed_num*10)+reminder
        n=n//10
    return original == reversed_num '''
n="priyank"
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print("palindrom")