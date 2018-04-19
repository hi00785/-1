from fractions import * 
import numpy 
import time
def size():
    start=time.perf_counter()
    print("您算分数，还是整数？")
    a=input()
    if a=="分数":
        temp = input("是加减乘除哪一个？请输入运算符号：")
        x = numpy.random.randint(1,50)
        y = numpy.random.randint(1,50)
        b = numpy.random.randint(1,50)
        c = numpy.random.randint(1,50)
        if temp == "+":
            print("答案为:%s+%s=%s"%(Fraction(x,y),Fraction(b,c),Fraction(x, y) + Fraction(b, c)))
        elif temp == "-":
            print("答案为:%s-%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) - Fraction(b, c)))
        elif temp == "*":
            print("答案为:%s*%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) * Fraction(b, c)))
        elif temp == "/":
            print("答案为:%s/%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) / Fraction(b, c)))
    elif a=="整数":
        x=numpy.random.randint(1,50)
        y=numpy.random.randint(1,50)
        temp = input("加减乘除？")
        if temp == "+":
            print("答案为:{:d}+{:d}={:d}" .format(x, y, x+y))
        elif temp == "-":
            print("答案为:{:d}-{:d}={:d}" .format(x, y, x-y))
        elif temp == "*":
            print("答案为:{:d}*{:d}={:d}".format(x, y, x*y))
        elif temp == "/":
            print("答案为:{:d}/{:d}={:.2f}" .format(x, y, x/y))
    else:
        print("您输入的数据有误")
    end=time.perf_counter()
    print("程序运行时间：{:.3f}".format(end-start))
size()