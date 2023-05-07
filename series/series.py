def fibonacci(n):
    """
    This function returns the nth number in the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers in which each number 
    is the sum of the two preceding numbers (i.e., 0, 1, 1, 2, 3, 5, 8, 13, ...).
    
    Parameters:
        n (int): the index of the number to return in the Fibonacci sequence
    
    Returns:
        int: the nth number in the Fibonacci sequence
        
    If n is less than or equal to 1, the function returns n (i.e., 0 or 1). 
    This is because the first two numbers in the sequence are 0 and 1, 
    so any number less than or equal to 1 will simply be itself. For n greater 
    than 1, the function recursively calculates the sum of the (n-1)th and 
    (n-2)th numbers in the sequence.
    """
   
    if n <= 1:
        return n
   
    else:
        return fibonacci(n-1) + fibonacci(n-2)
                                         


def lucas(n):
    """
    This function returns the nth number in the Lucas sequence. 
    The Lucas sequence is a series of numbers in which each number is 
    the sum of the two preceding numbers (similar to the Fibonacci sequence). 
    The first two numbers in the sequence are 2 and 1.
    
    Parameters:
        n (int): the index of the number to return in the Lucas sequence
    
    Returns:
        int: the nth number in the Lucas sequence
        
    If n is 0, the function returns 2, since that is the first number in the 
    Lucas sequence. If n is 1, the function returns 1, since that is the 
    second number in the sequence. For n greater than 1, the function 
    recursively calculates the sum of the (n-1)th and (n-2)th numbers in 
    the sequence.
    """
  
    if n == 0:
        return 2
    elif n == 1:
        return 1  
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, x=0, y=1):
    """
    This function returns the nth number in a series similar to the Fibonacci 
    sequence. The series starts with two numbers (x and y), and each subsequent 
    number is the sum of the two preceding numbers. 
    
    Parameters:
        n (int): the index of the number to return in the series
        x (int, optional): the first number in the series (default is 0)
        y (int, optional): the second number in the series (default is 1)
    
    Returns:
        int: the nth number in the series
        
    If n is 0, the function returns x (i.e., the first number in the series). 
    If n is 1, the function returns y (i.e., the second number in the series).
    For n greater than 1, the function recursively calculates the sum of the 
    (n-1)th and (n-2)th numbers in the series using the same x and y values as 
    the initial call to the function.
    """
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)


 