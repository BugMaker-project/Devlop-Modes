import time
#这是关于Bug-Maker的开发规范
#请所有Coder阅读后再开始写代码
#包含隐藏前缀+"Dis"的类.变量.函数是被禁止的
'''Such as:
def __Dis_Sort():
    pass'''

#预留代码部分：
class ExceptionBug(Exception):
    pass
class NonePointerExpection(ExceptionBug):
    pass
class NonePointerError(ExceptionBug):
    pass
#Author:Barry Liu
#-----Chapter 1 基本语句要求-----
#第一部分:变量名及非核心函数

var:str="VAR"#变量可以使用英语,数字,下划线&通用的拼音
__Dis_Bianliang="Var"#尽可能使用变量注解
__Dis_str1:str="Success"#禁止使用表意不明的变量名

def isActionTime(LastTime:int,Interval:float) ->bool:#标准格式,推荐指数***
    if LastTime==0:
        return True
    return time.time()-LastTime>=Interval
def TwoStar_isActionTime(LastTime,Interval):#可接受格式,推荐指数**
    if LastTime==0:
        return True
    return time.time()-LastTime>=Interval
def __Dis_isActionTime(LastTime,Interval):#不可接受格式::"PLEASE:注明合适的退出条件,简化代码逻辑,加快速度"
    return time.time()-LastTime>=Interval

def IfConditional(Conditional1:bool,Conditional2:bool,Conditional3:bool,Conditional4:bool) ->bool:
    isTrue=Conditional1 and Conditional2 and Conditional3 and Conditional4#使用is前缀的布尔类型变量简化if语句
    if isTrue:
        return True
def __Dis_IfConditional(Conditional1,Conditional2,Conditional3,Conditional4):
    if Conditional1 and Conditional2 and Conditional3 and Conditional4:
        return True

def NestedLogic(Num1,Num2,Num3):#正确的嵌套使用情景::"同一条件下有多个条件逻辑"
    if Num1>Num2:
        if Num2>Num3:
            return True
        else:
            return False
    else:
        if Num2>Num3:
            return True
        else:
            return False
def __Dis_NestedLogic(Num1,Num2,Num3):#错误的嵌套使用情景::"else下堆放if表达式逻辑"
    if Num1>Num2:
        return True
    else:
        if Num2>Num3:
            return True

#第二部分:核心函数&核心数据

class Hero(object):#必须有继承的父类,但不得为"int,str,float,list,set,tuple,list"
    def __init__(self,name):
        self.name=name#可重制的属性必须传参
        self.gender="BOY"#不可重制的属性必须定值
    def check(self):#必须考虑到所有的情况,必要时Raise NonePointerExpection or NonePointerError(空指针异常)
        if self.name=="Barry" or self.name=="Jason":
            return True
        elif self.name=="Jiangxia":
            return False
        else:
            raise NonePointerError("None Here.")#记住必须要有相应的try...except截获异常并做出处理
class __Dis_Hero():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def check(self):
        if self.name=="Barry" or self.name=="Jason":
            return True
        elif self.name=="Jiangxia":
            return False

def ExceptionSystem(TestCode):#正确的处理异常
    try:
        TestCode()
    except Exception as E:
        print("This is %s" %E)
        #Return:This is "invalid literal for int() with base 10: 'Test'"
def __Dis_ExceptionSystem(TestCode):#纯粹就是扔掉异常.不负责任
    try:
        TestCode()
    except Exception as E:
        pass

def HelloTest():#正确的处理异常测试.在所有自己不确定的核心函数前必须使用装饰器(划重点)测试
    @ExceptionSystem#测试函数必须保留(Test:装饰器+Func)
    def hello():
        int("Hello")
def __Dis_helloTest():#会raise错误所以千万不要用于Debug
    def hello():
        int("Hello")
    ExceptionSystem(hello())

def Nested(Num):#嵌套函数时务必具有能在900次内跳出的退出条件
    Num*=2
    if Num<=200:
        Nested(Num)
    else:
        return Num
def __Dis_Nested(Num):
    Num*=2
    Nested(Num)

def ServersIF(Num):#在设计核心代码的时候禁止使用else作为逻辑组成(不便于debug),else只能用于raise Expection
    if Num>0:
        return "Num>0"
    elif Num<0:
        return "Num<0"
    else:
        raise NonePointerExpection("Is ZERO")
def __Dis_ServerIF(Num):
    if Num>0:
        return "Num>0"
    else:
        return "Num<=0"

def NotEmpty(Var):#正确的判空语句有助于减少不必要的错误
    reponse=Var
    if reponse!=None:
        return True
    return False
def __Dis_NotEmpty(Var):
    reponse=Var
    if reponse==None:
        raise NonePointerError("Empty!")

        
