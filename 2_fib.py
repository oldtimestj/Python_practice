#!/usr/bin/env python
# -*- coding:utf-8 -*-
def fib(max):
    """

    :param max: 输出菲波那切数列的个数
    :return:'done'
    """
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return 'done'