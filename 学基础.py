"""print("字面量")# 空一格进行注释 这是规范
这是多行

注释
用于注释类和方法还有整个python代码


# 变量的测试代码
money=50
icecream=10
cola=5
print("当前钱包余额：",money,"元")
money -=icecream
print("购买了冰淇淋花费：",icecream,"元")
money -=cola
print("购买了可乐花费：",cola,"元")
print("最终钱包剩余：",money,"元")

# type数据类型
print(type(money))
print(type("程序员"))
type1=type(cola)
print(type1)

# 数字类型的转换
num_str=str(11)
print(type(num_str),num_str)
num_float=float(11)
print(type(num_float),num_float)
num_int=int(11.565)
print(type(num_int),num_int)
num1=int("15")
print(type(num1),num1)

num=10
print("每个人有%s元"%num)# 把数字转换成字符串再拼接
print("每个人有%d元"%num)# 就是数字占位符%d


# sep：设置多个内容之间的分隔符

year = 2024
print(year, '年，我要减肥')
print(year, '年，我要读100本书', sep='')
print(year, '年，我要去10个城市旅游', sep='')


# end:设置结束符，默认结束符'\n' year = 2024
print(year, '年，我要减肥', sep='', end='\n\n')
print(year, '年，我要读100本书', sep='', end='\n\n')
print(year, '年，我要去10个城市旅游', sep='', end='\n\n')

name="mia"
print("我的名字叫：%s，请多多关照！"%name)

student_no=1
print("我的学号是：%06d"%student_no)

price=8999
num=5
money=num*price
print("手机单价：%d元，购买%d台，需要支付%d元"%(price,num,money))

scale=0.1
print("数据比例是：%.02f%%"%(scale*100))

name=input("输入你的名字：")
print("我的名字叫：%s，请多多关照！"%name)

scale=input("输入一个小数：")
scale=float(scale)
print("数据比例是：%0.2f%%"%(scale*100))

name=input("输入名字：")
company=input('输入公司：')
print("******************************")
print("姓名：%s\n公司：%s"%(name,company))
print("******************************")
#格式化f语法，特点：无精度控制
name = "chuanzhiboke"
year = 2006
stock_price = 19.99
print(f"我是{name}，我成立于{year}，今天的股价是：{stock_price}")

# 字符串格式化 练习题
# input函数接收的内容会自动转化为字符串格式，要在输入后强制转换成数字类型，才可以进行数学运算

name=input("请输入公司名：")
stock_price=float(input("请输入当前股价："))
stock_code= input("请输入股票代码：")
stock_price_daily_growth_factor=float(input("请输入增长系数："))
growth_days=int(input("请输入增长天数："))
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过了%d天的增长，股价达到了：%.2f"%(stock_price_daily_growth_factor,
                            growth_days,stock_price*stock_price_daily_growth_factor**growth_days))

# if 语句格式
if 判断条件 :
四个空格缩进 （属于if的代码块）
elif 判断条件:
四个空格缩进 （属于else if的代码块）
else:
四个空格缩进 （属于else的代码块）

# if练习题
print("欢迎来到黑马游乐园，成人全价，儿童半价。")
age = int(input('请输入你的年龄：'))
if age <18:
    print('你未成年，游玩半价5元')
else:
    print('你已经成年，游玩全价10元')
print('祝您游玩愉快！')

# control + / 选中快捷注释

# while循环从1加到100
sum = 0;i=1
while i<101:
    sum += i
    i+=1
print(sum);

# 猜数字游戏
import random
num_guess = random.randint(1,100)
while True:
    guess=int(input('请猜一个1到100中间的数字：'))
    if guess==num_guess:
        print('你猜对了！')
        break
    elif guess>num_guess:
        print("太大了。")
    else:
        print('太小了。')

# 打印99乘法表！
i = 1# 乘法表行数
while i < 10:
    j = 1# 乘法表列数
    while j <= i:
        if(i == j):# 当行列相同时，打印换行
            print(f"{j} * {i} = {i*j}")
        else:# 行类不相同时，打印制表符，且不换行
            print(f"{j} * {i} = {j*i}\t\t",end="")
        j += 1# 列每次自增1
    i += 1# 行自增1

# for 循环基本案例
name = "itheima is a brand of itcast"
count =0
for letter in name:
    if letter == "a":
        count += 1
print("name中含有%d个字母a"%count)

# for循环结合range的使用
count = 0
for i in range(1,101):
    if i % 2 == 0:
        count+=1
print(f"1到100之间（含100本身）有{count}个偶数")

# 打印乘法表 for循环的嵌套
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            print(f"{i} * {j} = {i*j}")
            break
        else:
            print(f"{j} * {i} = {i*j}\t\t",end="")

# 解法2
for i in range(1,10):
    for j in range(1,i+1): # range可以以代码做参数
        print(f"{j} * {i} = {i*j}\t",end="")
    print() # 打印完一行，即i结束，就换行

# 循环终极题目 总共账户工资余额1万元，当员工绩效大于5时，发1千工资，否则不发，当账户无余额结束发工资
import random
count_rest = 10000
for i in range(1,21):
    jixiao = random.randint(1,10)
    if jixiao < 5 :
        print(f"员工{i}，绩效分{jixiao}，低于5，不发工资，下一位。")
        continue
    elif count_rest >= 1000:
        count_rest-=1000
        print(f"向员工{i}发工资1000元，账户余额剩余{count_rest}")
        continue
    print("工资发完了，下个月领取吧")
    break
if count_rest > 0: # 彩蛋
    print("笨蛋东西，绩效各个都这么低，工资都没发完。")

# 函数的定义和使用
def survey():
    print("欢迎来到函数章节！")
survey()

# 函数参数的使用
def survey(x):

    函数的说明文档
    测量体温是否正常
    :param x: 输入体温
    :return: 是否体温正常

    print("进行体温测量中...")
    if x < 37.6:
        print("ok")
    else:
        print("不ok")
survey(37)

# 函数大作业 取款机 （缺点：没有传参）

money = 5000000
name = input("输入您的姓名：")

def search():
    print("---------------------查询余额-------------------------\n"
          f"{name}，您好，您的余额剩余：{money}\n")
def save():
    print("---------------------存款-------------------------\n")
    save = int(input("输入您存多少钱："))
    print(f"{name}，您好，您存款{save}元成功\n")
    global money
    money += save
    print(f"{name}，您好，您的余额剩余：{money}元\n")
def load():
    print("---------------------取款-------------------------\n")
    global money
    load = int(input("输入您取多少钱："))
    if load < money:
        print(f"{name}，您好，您取款{load}元成功\n")
    else:
        return None
    money -= load
    print(f"{name}，您好，您的余额剩余：{money}元\n")

def maindan():
    print("---------------------主菜单-------------------------\n"
          f"{name}，您好，欢迎来到银行，请选择操作：\n"
          "查询余额\t【输入1】\n"
          "存款  \t【输入2】\n"
          "取款  \t【输入3】\n"
          "退出  \t【输入4】\n"
          "请输入您的选择：")

def main():
    while True:
        maindan()
        num = input()
        if num == "1":
            search()
        elif num == "2":
            save()
        elif num == "3":
            load()
        else:
            print("程序退出！")
            return None
main()

# 列表
# list = [元素1,元素2] 各个元素可以是不同类型;元素可以也是列表，这样称为嵌套列表
# list = []
# list = list()
#列表的常用操作
mylist = ["itcast","itheima","python"]
#找到元素下标
index = mylist.index("itheima")
print(index)
#列表插入
mylist.insert(1,"best")
print(mylist)
#列表插入,从后插入，追加
mylist.append("黑马")
print(mylist)
mylist2=[1,12,2]
#列表插入,从后插入，追加一个列表
mylist.extend(mylist2)
print(mylist)
#列表删除
mylist = ["itcast","itheima","python"]
del mylist[2]
print(mylist)
mylist = ["itcast","itheima","python"]
element = mylist.pop(2)
print(mylist,element)
mylist = [1,2,3,4,2]
#去除掉元素2，而且是第一个2
mylist.remove(2)
print(mylist)
#列表清空
mylist.clear()
#统计元素数量
mylist= [1,1,2,3,4,4,5]
count= mylist.count(4)
print(count)
#列表总共多少个元素
num = len(mylist)
print(num)

##########################
# 廖雪峰学python
##########################
# 列表 list 元组 tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])

# 循环打印
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("hello!",i)

# 函数
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数

# 强制进制转换
n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))

n1=255
n2=1000
for num in [n1,n2]:
     a=hex(num)
     print(f'{num}的十六进制表示为{a}')

# 函数小测，计算二元一次方程
import math

def quadratic(a, b, c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 函数练习
def mul(*numbers):
    if(len(numbers)==0):
        raise TypeError()
    x=1
    for number in numbers:
        x=x*number
    return x

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

# 递归函数 汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # 将n-1个盘子从a借助c移动到b
        move(n - 1, a, c, b)
        # 将最大的盘子从a移动到c
        print(a, '-->', c)
        # 将n-1个盘子从b借助a移动到c
        move(n - 1, b, a, c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')

# 编程高级特性 减少代码 （生成列表）
nums = list(range(1, 100, 2))
print(nums)

# 去除字符串首尾的空格 切片的应用
def trim(s):
    if not s:        # 对于空字符串s[0]和s[-1]这样的索引操作会引发IndexError
        return s
    while s[0]==' ': # 当字符串开头和结尾都有多个空格时，使用循环来处理多个空格
        s=s[1:]
        if not s:
            return s
    while s[-1]==' ':
        s=s[:-1]
        if not s:
            return s
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')
# 解法 2
def trim(s):
    while s and s[0] == ' ': # while 循环的条件是一个逻辑与 and 连接的表达式。只有当 s 不为空
                            # （在 Python 中，空字符串被视为 False，非空字符串视为 True）
                            # 时，才会去检查 s[0] == ' ' 或者 s[-1] == ' '。
        s = s[1:]
    while s and s[-1] == ' ':
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')

# for 循环的迭代
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
     print(k,v)

# 判断是否可以迭代
from collections.abc import Iterable
print(isinstance('abc', Iterable))

# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:          # 字符串长度为0或1时的特殊处理
        return (None, None)
    #elif len(L) == 1:        长度为1时也可以直接用下面的代码
        return (L[0], L[0])
    max , min = L[0] , L[0]  # 赋值简便写法（与C语言不同）
    for l in L[1:]:          #比大小
        if l > max:
            max = l
        elif l < min:
            min = l
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')

# 列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a,b=b,a + b   # 这种赋值，是同时赋值，a赋值以后的值，不会用在a+b中
        n = n + 1
    return 'done'
fib(3)

# 杨辉三角
def triangles():
    A = [1]
    while True:
        yield A
        A = [1] + [A[i] + A[i + 1] for i in range(len(A) - 1)] + [1]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

# 高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# map() 的使用
def normalize(name):
    # 法1
    if not name:
        return name
    new_name = name[0].upper() + name[1:].lower()
    return new_name
    # 法2
    # return name.title()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# reduce()的使用
from functools import reduce

def prod(L):
    # 法1
    # return reduce(lambda x, y: x * y, L)
    # 法2
    def f(x,y):
        return x * y
    return reduce(f, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# map()、reduce()组合用法
from functools import reduce

def str2float(s):
    # 法1
    # 分割整数部分和小数部分
    integer, decimal = s.split('.')
    # 整数部分照常计算
    def fi(x, y):
        return x * 10 + y
    i = reduce(fi, map(int, integer))
    # 将小数部分字符转换为数字并累加成小数，考虑权重
    d = reduce(lambda x, y: x + int(y) * 10 ** (-1 * (decimal.index(y) + 1)), decimal, 0) # x初始化为0
    return i+d
    # 法2
    # integer, decimal = s.split('.')
    # int_part = reduce(lambda x, y: x * 10 + int(y), integer, 0)
    # # 使用map计算每个小数位对应的数值
    # dec_values = map(lambda y: int(y) * 10 ** (-1 * (decimal.index(y) + 1)), decimal)
    # # 使用reduce累加这些数值
    # dec_part = reduce(lambda x, y: x + y, dec_values)
    # return int_part + dec_part

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# filter()过滤器的使用  回文数字
# 判断真假，真则保留
def is_palindrome(x):
    y = x
    s = 0
    while x > 0:
        s = s * 10 + x % 10
        x //= 10  # // 运算符执行整除操作，它会舍去小数部分，只保留整数结果。
    if s == y:
        return True

    # 法2
    #s = str(n)
    #return s == s[::-1]   # 判断字符串 s 是否与其反转后的字符串相等，s[::-1] 是 Python 中反转字符串的一种简洁方式。
                           # 如果相等则返回 True，表示 n 是回文数；否则返回 False。


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# sorted()排序函数
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]  # 第一个元素姓名

L2 = sorted(L, key=by_name)
print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]  # 第二个元素成绩

L2 = sorted(L, key=by_score)
print(L2)

# 闭包问题 i 不会立刻返回，而是在for循环结束返回，所以值为3
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 闭包理解
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

# 闭包练习
def createCounter():
    x=0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 匿名函数
L = list(filter(lambda n : n % 2 == 1, range(1, 20)))

print(L)

# decorator() 装饰器函数
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # 1. 记录函数执行前的时间戳
        start_time = time.time()
        # 2. 执行原函数，透传所有参数并保存返回值
        # 函数调用前打印日志
        print(f'begin call: {fn.__name__}')
        # 执行原函数，透传所有参数并保存返回值
        result = fn(*args, **kwargs)
        # 函数调用后打印日志
        print(f'end call: {fn.__name__}')
        # 3. 计算执行耗时（转毫秒，保留4位小数）
        exec_time = (time.time() - start_time) * 1000
        # 4. 打印函数名和执行时间
        print(f'{fn.__name__} executed in {exec_time:.4f} ms')
        # 5. 返回原函数的执行结果
        return result

    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')

# 装饰器函数 decorator()
import functools

def log(text=None):

    # 支持无参数(@log)和带参数(@log('execute'))的日志装饰器
    # :param text: 可选的日志文本，默认值为'call'
    # :return: 装饰器/包装函数


    # 定义真正的装饰器函数（接收被装饰的函数作为参数）
    def decorator(fn):
        # 保留原函数的元信息（如__name__）
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # 确定日志文本：有参数用传入的text，无参数用默认'call'
            log_msg = text if text is not None else 'call'
            # 打印前置日志
            print(f'begin {log_msg}: {fn.__name__}')
            # 执行原函数并保存返回值
            result = fn(*args, **kwargs)
            # 打印后置日志
            print(f'end {log_msg}: {fn.__name__}')
            # 返回原函数的执行结果
            return result

        return wrapper

    # 关键：判断调用方式（无参数/带参数）
    if callable(text):
        # 情况1：无参数调用（@log），此时text是被装饰的函数
        fn = text  # 把函数赋值给fn
        text = None  # 重置text为默认值
        return decorator(fn)  # 直接返回装饰后的函数
    else:
        # 情况2：带参数调用（@log('execute')），返回装饰器函数
        return decorator


# ==================== 测试两种用法 ====================
# 用法1：无参数@log
@log
def f1():
    print('执行f1函数')


# 用法2：带参数@log('execute')
@log('execute')
def f2():
    print('执行f2函数')


# 执行测试
f1()
print('-' * 20)
f2()

# 面向对象 类的访问控制
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 获取对象信息
# 使用isinstance()函数 isinstance(h, Husky)
# 能用type()判断的基本类型也可以用isinstance()判断
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”

# 获得一个对象的所有属性和方法，可以使用dir()函数
# getattr() getattr(obj, 'y') # 获取属性'y'
# setattr() setattr(obj, 'y', 19) # 设置一个属性'y'
# hasattr() hasattr(obj, 'x') # 有属性'x'吗？

# 实例属性和类属性
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        Student.count =Student.count + 1

# 测试:
if Student.count != 0:
    print('1测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('2测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('3测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# python是动态语言，可以动态绑定方法（在实例中绑定方法，注意：给一个实例绑定的方法，对另一个实例是不起作用的）
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# @ property
# 用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    def __init__(self):
        # 1. 改用私有实例变量（加下划线），避免与@property属性名冲突
        # 否则@property 装饰的 width/height 属性名，与实例变量 self.width/self.height 重名了。
        # 当调用 s.width = 1024 时，会执行 width.setter 方法，其中 self.width = value 又会再次调用 width.setter，形成无限递归
        self._width=0
        self._height=0

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width *self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# 枚举类 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
from enum import Enum, unique

@unique # 检测枚举值有无重复，重复则报错
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# 检错 try出错，则执行except try不出错，则不执行except finally一定会执行
# 可以有多个except来捕获不同类型的错误
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 错误处理
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

# 单元测试
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
import unittest
from logging import raiseExceptions
from unittest import case


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        match self.score:
            case s if 80<=s<=100:
                return 'A'
            case s if 60<=s<80:
                return 'B'
            case s if 0<=s<60:
                return 'C'
            case _:
                raise ValueError("hhh")

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

# 文档测试
# 对函数fact(n)编写doctest并执行

def fact(n):
    '''
    Calculate 1*2*...*n

    # >>> fact(1)
    # 1
    # >>> fact(10)
    # 3628800
    # >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    #doctest.testmod(verbose=True)

# 文件读写
# 请将本地一个文本文件读为一个str并打印出来
fpath = 'C:/Users/86152/Desktop/论文与书单.txt'

with open(fpath, 'r',encoding='utf-8') as f:
    s = f.read()
    print(s)

# 运行代码观察结果

# 输出系统名称
import os
print(os.name)

# 利用os模块编写一个能实现dir -l输出的程序

# 导入操作系统相关功能模块，用于文件和目录操作
import os
# 导入stat模块，用于解析文件的权限、类型等状态信息
import stat
# 导入时间模块，用于格式化文件的修改时间
import time

# 尝试导入Unix/Linux系统专用的用户和用户组模块
# Windows系统没有这两个模块，所以用try-except做兼容处理
try:
    # pwd模块：通过用户ID(UID)获取用户名
    import pwd
    # grp模块：通过组ID(GID)获取用户组名
    import grp
    # 标记当前是Linux/Mac系统
    UNIX_SYSTEM = True
except ImportError:
    # 导入失败说明是Windows系统，标记为非Unix系统
    UNIX_SYSTEM = False


def get_file_permissions(mode):

    # 功能：将系统返回的数字文件模式，转换成 Linux 风格的 rwxr-xr-x 权限字符串
    # 参数：mode - os.stat()返回的st_mode，代表文件类型和权限的数字
    # 返回值：类似 drwxr-xr-x 的权限字符串

    # 初始化空的权限字符串
    perm_str = ''

    # 第一步：判断文件类型（目录、链接、普通文件）
    # 判断是否是目录，如果是权限第一位为d
    if stat.S_ISDIR(mode):
        perm_str += 'd'
    # 判断是否是软链接，如果是第一位为l
    elif stat.S_ISLNK(mode):
        perm_str += 'l'
    # 普通文件，第一位为-
    else:
        perm_str += '-'

    # 第二步：解析 文件所有者（user）的 读、写、执行权限
    # 所有者读权限：S_IRUSR 对应数字权限，有则显示r，无则-
    perm_str += 'r' if (mode & stat.S_IRUSR) else '-'
    # 所有者写权限
    perm_str += 'w' if (mode & stat.S_IWUSR) else '-'
    # 所有者执行权限
    perm_str += 'x' if (mode & stat.S_IXUSR) else '-'

    # 第三步：解析 用户组（group）的 读、写、执行权限
    perm_str += 'r' if (mode & stat.S_IRGRP) else '-'
    perm_str += 'w' if (mode & stat.S_IWGRP) else '-'
    perm_str += 'x' if (mode & stat.S_IXGRP) else '-'

    # 第四步：解析 其他用户（other）的 读、写、执行权限
    perm_str += 'r' if (mode & stat.S_IROTH) else '-'
    perm_str += 'w' if (mode & stat.S_IWOTH) else '-'
    perm_str += 'x' if (mode & stat.S_IXOTH) else '-'

    # 返回拼接好的完整权限字符串
    return perm_str


def get_user_name(uid):

    # 功能：通过用户ID(uid)获取对应的用户名
    # 参数：uid - 文件所有者的用户ID
    # 返回值：用户名字符串

    # 如果是Linux/Mac系统，通过pwd模块获取用户名
    if UNIX_SYSTEM:
        return pwd.getpwuid(uid).pw_name
    # Windows系统没有用户名，直接返回数字uid
    return str(uid)


def get_group_name(gid):

    # 功能：通过组ID(gid)获取对应的用户组名
    # 参数：gid - 文件所属的用户组ID
    # 返回值：用户组名字符串

    # Linux/Mac系统获取组名
    if UNIX_SYSTEM:
        return grp.getgrgid(gid).gr_name
    # Windows直接返回数字gid
    return str(gid)


def format_time(timestamp):

    # 功能：将时间戳格式化为 dir -l 风格的时间（月 日 时:分）
    # 参数：timestamp - 文件修改时间的时间戳
    # 返回值：格式化后的时间字符串

    # 将时间戳转为本地时间的结构化对象
    time_struct = time.localtime(timestamp)
    # 格式化为：月份 日期 小时:分钟
    return time.strftime("%b %d %H:%M", time_struct)


def dir_l(path='.'):

    # 功能：模拟Linux命令 dir -l / ls -l，长格式列出目录内容
    # 参数：path - 要查看的目录路径，默认是当前目录(.)

    # 打印输出表头，对齐格式，和系统命令保持一致
    print(f"{'权限':<9} {'硬链接':<5} {'所有者':<6} {'组':<8} {'大小':<8} {'修改时间':<11} {'文件名'}")
    # 打印分割线
    print('-' * 80)

    # 遍历指定目录下的所有文件和文件夹名称
    for filename in os.listdir(path):
        # 拼接完整文件路径：目录路径 + 文件名，防止路径错误
        file_path = os.path.join(path, filename)
        # 获取文件/文件夹的详细状态信息（权限、大小、时间、uid等）
        file_stat = os.stat(file_path)

        # 调用函数，获取格式化后的权限字符串
        perm = get_file_permissions(file_stat.st_mode)
        # 获取硬链接数量
        nlink = file_stat.st_nlink
        # 获取所有者用户名
        user = get_user_name(file_stat.st_uid)
        # 获取所属用户组名
        group = get_group_name(file_stat.st_gid)
        # 获取文件大小，单位字节
        size = file_stat.st_size
        # 获取格式化后的修改时间
        mtime = format_time(file_stat.st_mtime)

        # 按列对齐输出所有信息
        print(f"{perm:<11} {nlink:<6} {user:<8} {group:<8} {size:<8} {mtime:<15} {filename}")


# 程序入口：当直接运行这个.py文件时，执行下面代码
if __name__ == '__main__':
    # 调用dir_l函数，默认列出当前目录，也可以传入路径如 dir_l("C:\\Users")
    dir_l("C:/Users/86152/Desktop")

# 导入操作系统模块，用于文件/目录遍历、路径处理
import os


def search_files(keyword):

    # 递归查找当前目录及所有子目录中，文件名包含指定关键词的文件
    # :param keyword: 要查找的文件名关键词

    # 标记是否找到文件
    found = False

    # ========== 核心：os.walk() 遍历目录 ==========
    # os.walk('.') 表示从【当前目录】开始遍历
    # 返回三个值：
    # root：当前正在遍历的目录路径（相对路径）
    # dirs：当前目录下的子目录列表
    # files：当前目录下的文件列表
    for root, dirs, files in os.walk('.'):
        # 遍历当前目录下的所有文件
        for filename in files:
            # 判断：文件名 是否 包含指定的关键词（不区分大小写可加 .lower()）
            if keyword in filename:
                # 拼接：当前目录路径 + 文件名 = 文件的完整相对路径
                file_path = os.path.join(root, filename)
                # 打印找到的文件相对路径
                print(f"找到文件：{file_path}")
                found = True  # 标记已找到文件

    # 如果遍历完所有目录都没找到，输出提示
    if not found:
        print(f"未找到名称包含【{keyword}】的文件")


# ========== 程序入口 ==========
if __name__ == '__main__':
    # 获取用户输入的查找关键词
    search_key = input("请输入要查找的文件名字符串：").strip()

    # 判断用户是否输入了有效内容
    if not search_key:
        print("请输入有效的查找关键词！")
    else:
        # 调用查找函数
        search_files(search_key)

# ensure_ascii=True（默认）：中文会被转义成 /uXXXX 格式的 Unicode 编码，不显示原生中文
# ensure_ascii=False：中文正常显示，保留原生字符（最常用）
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj,ensure_ascii=False)
print(s)

# windows 上执行多进程的代码
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 用 Python 调用系统命令 nslookup 查询 www.python.org 的 IP 地址，并输出执行结果是否成功。
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)

# 线程
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# 正则表达式
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
import re

def is_valid_email(addr):
    # 正则表达式规则：
    # ^  : 匹配字符串开头
    # [a-zA-Z0-9.]+  : 用户名：字母/数字/点，至少1个字符
    # @  : 必须包含@符号
    # [a-zA-Z0-9.]+  : 域名主体：字母/数字/点
    # \.[a-zA-Z]{2,} : 域名后缀（.com/.org等），至少2个字母
    # $  : 匹配字符串结尾
    pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$'

    # 匹配成功返回True，失败返回False
    return re.match(pattern, addr) is not None

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 版本二可以提取出带名字的Email地址：
#
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
import re

def name_of_email(addr):
    # 正则表达式分组匹配：
    # ^          匹配字符串开头
    # <([^>]+)>  匹配 <内容>，捕获分组1存放姓名（非捕获分组包裹，可选匹配）
    # \s*        匹配任意空格（0个或多个）
    # (\w+)      捕获分组2存放@前面的用户名
    # @.*        匹配@及后面的所有内容
    pattern = r'^(?:<([^>]+)>)?\s*(\w+)@.*$'
    # 执行正则匹配
    match = re.match(pattern, addr)
    if match:
        # 如果分组1有值（存在<姓名>），返回分组1；否则返回分组2
        return match.group(1) or match.group(2)
    # 不匹配的情况返回None
    return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

# 时间（内建模块）
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    local_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    groups = re.match(r'UTC([+-]\d+):(\d+)',tz_str).groups()
    tz_hours = int(groups[0])
    tz = timezone(timedelta(hours=tz_hours))
    local_dt_with_tz =local_dt.replace(tzinfo=tz)
    return local_dt_with_tz.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

import functools
import time
def retry(max_time=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_time):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i+1}次调用失败 | 错误{e} | 请{delay}秒后重试")
                    time.sleep(delay)
            raise Exception(f"函数{func>__name__}，重试{max_time}次全部失败。")
        return wrapper
    return decorator
@retry(max_time=3, delay=2)
def call(query):
    pass

import functools
import time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数{func.__name__}耗时{end-start:.2f}s")
        return result

def my_gen():
    print("执行第一步")
    yield 1
    print("执行第二步")
    yield 2
    print("执行第三步")
    yield 3

g = my_gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

gen_data = (i*2 for i in range(1000000))
print( next(gen_data) )
print( next(gen_data) )
print( next(gen_data) )
"""
import time

def stream_llm_reply(full_text):
    """模拟大模型流式输出，逐字返回"""
    for char in full_text:
        # 模拟生成延迟
        time.sleep(0.1)
        yield char

# 逐字打印回复，就是聊天界面的打字机效果
for word in stream_llm_reply("你好，我是豆包，有什么可以帮你的？"):
    print(word, end="", flush=True)
