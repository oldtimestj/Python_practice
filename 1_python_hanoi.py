#!/usr/bin/env python
#-*- coding:utf-8 -*-
def move(n,source,auxiliary,target):
    """

    :param n: 需要移动盘子的个数
    :param source: 移动的源
    :param auxiliary: 移动中辅助
    :param target: 移动的目标
    :return:
    """
    if n == 1:
        print(source,'-->',target)
    else:
        move(n-1,source,target,auxiliary)
        print(source, '-->', target)
        move(n-1,auxiliary,source,target)
move(3,'A','B','C')


class Tower(object):
    def __init__(self):
        self.counter = 0
    def hanoi(self,n,org,aux,dst):
        if n == 1:
            self.counter += 1
            print('{0}-->{1}'.format(org,dst))
        else:
            self.hanoi(n-1,org,dst,aux)
            self.hanoi(1,org,aux,dst)
            self.hanoi(n-1,aux,org,dst)
def homework(*args):
    tower = Tower()
    print('移动步骤如下:')
    tower.hanoi(*args)
    print('总共移动次数为:{0}'.format(tower.counter))
homework(3,'A','B','C')