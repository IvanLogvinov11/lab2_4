#!/usr/bin/env python3
# -- coding: utf-8 --
import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    a1 = list(range(0, len(a)))
    in1 = int(input("range 1: "))
    in2 = int(input("range 2: "))
    min_a = a[0]
    pos = 0

    for i in range(0, len(a)):
        if a[i] < min_a:
            min_a = a[i]
            min_i = i

    for i in a:
        if i < 0:
            for j in a[i:len(a)]:
                pos += j
        else:
            break

    for i in range(0, len(a)):
        if (a[i] >= in1) and (a[i] <= in2):
            a.remove(a[i])
            a.append(0)
    for i in range(0, len(a)):
        print(a[i])
    print('\nminimum is: ', min_a , 'sum is', pos)