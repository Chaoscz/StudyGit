Python

# 基础

## 输出

```python
s1=2 

s2=3

r= s1+s2 

print('s1+s2=%s' % r)

```

## 输入

```python
name = input("请输入你的姓名:")
print('hello,',name)
```

## 转义字符

```python
#多行输出
print('''line1
line2
line2''')
#使用r默认不转义
print(r'\\\t\\')
```

## list和tuple

```python
#list
list=['a','b','c']
#二维list
list =['a','b',['c','d']]
#获取倒数第2个
list[-2]
#添加元素 append 末尾
list.append('d')
#insert(index,element)
list.insert(1,e)
#删除 pop([index]) 默认删除最后一个
list.pop()
#tuple 元素无法改变
tuple =('a','b',['c','d'])
#tuple[2] 为list 元素可改变
tuple[2][0] ='x'
tuple[2][1]='y'
#单个元素定义
tuple=(1,)ss
```

## 条件判断

```python
#同一的缩进为一个代码块 注意 条件判断完 ':'不能缺少
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
#if elseif
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
    print('True')
```

## 循环

```python
#for循环
for x in list:
	print(x)
#while循环 
n=10
while n>0;
	print(n)
    n=n-2
    if n==2:
        break
print('n=',n)

#range[5] [0,5)
#range[0,5,2]  0,2,4 [0,5) step 2
```

## dict和set

```python
#dict 字典 key-value
dict = {'name':test,'age:'18}
#取值
dict['name']
#判断key 是否在字典中  
#(1) 'name' in dict 
#(2) dict.get('name') 不存在返回None  dict.get('name'[,string]) 不存在返回string
#删除pop
dict.pop('age')
#set  无重复，无序
set = ([1,2,3])
#添加元素  set.add(element)
#删除元素 set.remove(element)
#获得两个set的交集  set1 & set2 
#获得并集          set1 | set2
```

# 函数

## 调用函数

```python
#一般用法
abs(-1)
#max可接受多个参数
max(1,2,3,4,5)
#常用函数
int('123') #123
int(12.32) #12
float('12.34') #12.34
str(1.23) #'1.23'
bool(1) #true
bool('') #false
#可以把函数名赋给变量
a = abs
a(-1) #1
```

### 类型转换

```python
int(x [,base ])         #将x转换为一个整数  
long(x [,base ])        #将x转换为一个长整数  
float(x )               #将x转换到一个浮点数  
complex(real [,imag ])  #创建一个复数  
str(x )                 #将对象 x 转换为字符串  
repr(x )                #将对象 x 转换为表达式字符串  
eval(str )              #用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               #将序列 s 转换为一个元组  
list(s )                #将序列 s 转换为一个列表  
chr(x )                 #将一个整数转换为一个字符  
unichr(x )              #将一个整数转换为Unicode字符  
ord(x )                 #将一个字符转换为它的整数值  
hex(x )                 #将一个整数转换为一个十六进制字符串  
oct(x )                 #将一个整数转换为一个八进制字符串  
```

### 数学函数

```python
abs(x)	         #返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	         #返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	     #如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)	         #返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	         #返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	     #返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	         #如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	     #返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	 #返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)  #返回给定参数的最小值，参数可以为序列。
modf(x)	         #返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y #运算后的值。
round(x [,n])	 #返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	         #返回数字x的平方根
```

### 随机函数

```python
choice(seq)	   #从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑					选一个整数。
randrange ([start,] stop [,step])	#从指定范围内，按指定基数递增的集合中获取一个随机数，基数									  缺省值为1
random()	#随机生成下一个实数，它在[0,1)范围内。
seed([x])	#改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮			你选择seed。
shuffle(lst)	#将序列的所有元素随机排序
uniform(x, y)	#随机生成下一个实数，它在[x,y]范围内。
```

## 定义函数

```python
#求绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
#设置默认参数
def my_pow(x,n=2):
    s=1
    while n>0
    	s=s*s
    return s
#调用 
my_pow(5) #相当于 my_pow(5,2)
# 参数默认为 list  以下写法存在地址传递问题，每次调用都会添加'end' 
def add_end(L=[]):
    L.append('end')
   	return L
#解决方案
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
#传递可变参数 calc(1,2,3,4,5)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#将list作为可变参数 l = [1,2,3,4,5] 
calc(*l)
#关键字参数
def printme( str ):
   print str;
   return;
#调用printme函数
printme( str = "My string");
```

## 递归函数

```python
#求阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```

# 切片

```python
#截取list前3个元素
list = [1,2,3,4,5,6,7,8,9,10]
list[0:3] #[0,3) 从0开始到3  等同于 list[:3]
list[-2:] #倒数两个[8,9] 
list[-2:-1] #从-2开始到-1 [8]
list[:10:2] #[0,2,4,6,8] 前10个每两个去一个
```

# 迭代

```python
#dict 迭代
d ={'a':1,'b':2,'c':3}
for key in d:
    print(key)
#获取下标
l =['A','B','C']
for i,value in enumerate(l):
    print(i,value)
#同时引用两个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
```

# 列表生成式

```python
#生成[1x1, 2x2, 3x3, ..., 10x10]
[x * x for x in range(1, 11)] #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]
#双重循环
[m + n for m in 'ABC' for n in 'XYZ'] #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#dict   x=A y=B z=C
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
```
# 生成器

```python
#创建生成式
 g = (x * x for x in range(10))
#获取元素
#1.next(g)
#2. for l in g
```
# 迭代器

```python
#引用模块
from collections import Iterable
isinstance([], Iterable)#True
isinstance({}, Iterable)#True
isinstance('abc', Iterable)#True
isinstance((x for x in range(10)), Iterable)#True
isinstance(100, Iterable)#False
#把list、dict、str等Iterable变成Iterator 使用iter()函数：
isinstance(iter([]), Iterator)#True
isinstance(iter('abc'), Iterator)#True
```

# map/reduce

```python
#map 
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
list(map(f,[1,2,3,5])) #[1,4,9,25]
#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9])
#25

```

# filter

Python内建的`filter()`函数用于过滤序列。

和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

```python
# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```

# sorted

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

```python
sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

```python
#收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

```python
#忽略大小写，逆序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

# 返回函数

如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```

### 闭包

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#结果
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
 #结果
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```

# 匿名函数

```python

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25
```

# 装饰器

函数对象有一个`__name__`属性，可以拿到函数的名字：

```python
def now():
...     print('2015-3-25')

>>> now.__name__
'now'
>>> f.__name__
'now'
```

现在，假设我们要增强`now()`函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改`now()`函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

# 使用模块

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
 #当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
```

# 类

```python
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
class Student(object):
  
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
 	def print_score(self):
        print('%s: %s' % (self.name, self.score))
```





