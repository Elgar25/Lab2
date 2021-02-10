#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны координаты на плоскости двух точек.
# Найти расстояние между этими точками.

if __name__ == '__main__':
    from math import*
    import math

    x = float(input("введите 1х координату"))
    y = float(input("введите 1у координату"))
    x2 = float(input("введите 2х координату"))
    y2 = float(input("введите 2у координату"))
    dist = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
    print("Расстояние", dist)