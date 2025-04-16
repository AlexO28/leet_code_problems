# You have a function printNumber that can be called with an integer parameter and prints it to the console.
# For example, calling printNumber(7) prints 7 to the console.
# You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:
# Thread A: calls zero() that should only output 0's.
# Thread B: calls even() that should only output even numbers.
# Thread C: calls odd() that should only output odd numbers.
# Modify the given class to output the series "010203040506..." where the length of the series must be 2n.
# Implement the ZeroEvenOdd class:
# ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
# void zero(printNumber) Calls printNumber to output one zero.
# void even(printNumber) Calls printNumber to output one even number.
# void odd(printNumber) Calls printNumber to output one odd number.
from threading import Semaphore
from typing import Callable


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.l1 = Semaphore(1)
        self.l2 = Semaphore(0)
        self.l3 = Semaphore(0)

        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.l1.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.l2.release()
            else:
                self.l3.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.l3.acquire()
            printNumber(i)
            self.l1.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.l2.acquire()
            printNumber(i)
            self.l1.release()
