# You have the four functions:
# printFizz that prints the word "fizz" to the console,
# printBuzz that prints the word "buzz" to the console,
# printFizzBuzz that prints the word "fizzbuzz" to the console, and
# printNumber that prints a given integer to the console.
# You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:
# Thread A: calls fizz() that should output the word "fizz".
# Thread B: calls buzz() that should output the word "buzz".
# Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
# Thread D: calls number() that should only output the integers.
# Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:
# "fizzbuzz" if i is divisible by 3 and 5,
# "fizz" if i is divisible by 3 and not 5,
# "buzz" if i is divisible by 5 and not 3, or
# i if i is not divisible by 3 or 5.
# Implement the FizzBuzz class:
# FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.
# void fizz(printFizz) Calls printFizz to output "fizz".
# void buzz(printBuzz) Calls printBuzz to output "buzz".
# void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
# void number(printNumber) Calls printnumber to output the numbers.
from typing import Callable
import threading


class FizzBuzz:
    def __init__(self, n: int):      
        self.n = n
        self.f = threading.Lock()
        self.b = threading.Lock()
        self.fb = threading.Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()
        self.main = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.f.acquire()
            if self.n == 0 :
                break
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.b.acquire()
            if self.n == 0:
                break
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                break
            printFizzBuzz()
            self.main.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.main.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release()

        self.main.acquire() 
        self.n = 0
        self.f.release()
        self.b.release()
        self.fb.release()
