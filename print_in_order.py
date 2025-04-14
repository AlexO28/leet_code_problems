# Suppose we have a class:
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
# Note:
# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
from threading import Semaphore
from typing import Callable


class Foo:
    def __init__(self):
        self.first_done = Semaphore(1)
        self.second_done = Semaphore(0)
        self.third_done = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        self.first_done.acquire()
        printFirst()
        self.second_done.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.second_done.acquire()
        printSecond()
        self.third_done.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.third_done.acquire()
        printThird()
