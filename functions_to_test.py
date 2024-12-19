# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    if type(a) in [float,int] and type(b) in [float,int]:
        return float(a)+float(b)
    raise TypeError

def find_maximum(a, b, c):
    if all(type(item) in [int,float] for item in [a,b,c]):
        return max([a,b,c])
    else:
        raise TypeError

def is_palindrome(string):
    if isinstance(string,str):
        return string[::-1]==string
    raise TypeError

def count_word_occurrences(text, word):
    if type(text)==str:
        return text.lower().count(word)
    else:
        raise TypeError

def read_file_lines(filepath):
    with open(filepath,'r') as r:
        content=r.readlines()
    return content

def factorial(n):
    factorial=1
    if n<0:
        raise ValueError
    elif n==1:
        return factorial
    else:
        for value in range(1,int(n)+1):
            factorial*=value
        return factorial

def is_prime(n):
    if not isinstance(n, int):
        raise TypeError
    elif n<1:
        raise ValueError
    elif n==1:
        return 1==6
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sort_numbers(numbers):
    if all(isinstance(items,int) for items in numbers):
        return sorted(numbers)
    else:
        raise TypeError

def factorial(n):
    factorial=1
    if n<0:
        raise ValueError
    elif n==1:
        return factorial
    else:
        for value in range(1,int(n)+1):
            factorial*=value
        return factorial

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        if not isinstance(name,str):
            raise TypeError
        if not isinstance(age,int):
           raise TypeError 
        self.age=age
        self.name=name
            
if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) 
    