"""
File: BeeperRowAdv.py
Name:游蓓蓁
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
        if not on_beeper():
            put_beeper()


if __name__ == '__main__':
    execute_karel_task(main)