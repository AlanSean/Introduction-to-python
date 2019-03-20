#!usr/bin/python
# -*- coding: utf-8 -*-





##String运算符
### +  字符串拼接  返回新字符串
string1 = 'strin' + 'g1' #string1

### * 重复输出字符串 相乘的意思 返回新字符串
string2 = string1 * 2 #string1string1

### [:] 截取字符串中的一部分 返回截取的部分
string3 = string2[0 : 1]#3

### in 成员运算符  该字符串是否含有该字符 返回boolean
string4 = 's' in string3 # True
string5 = 'true' in string3 # False

### not in 成员运算符 判断指定字符是否不在该字符串中，与in相反 返回boolean
string6 = 'true' not in string3 # True
string7 = 's' not in string3 # False

### r/R 原始字符串 防止转义
string8 = 'a\"' # a"
string9 = r'a\"' # a\\"
string10 = R'a\"' # a\\"pa

## 字符串格式化
### %s 格式化字符串
string11 = "ab%s" % 'c' #abc

### %c 格式化字符及其ASCII码
# ord('c') 99
string12 = "ab%c" % 99 #abc
string12 = "ab%c" % 'c' #abc

### %d 格式化整数
string13 = "12%d" % 3 #123

##String内建函数

###capitalize 字符串首字符变为大写
string14 = "string14"
string15 = string14.capitalize() #"String14"

###center(width[,char]) 
####width大于原字符串长度时，返回width长度的新字符串，否则原样返回
####char 可选参数 默认为空格。新长度大于原长度时使用该字符进行填充
#### 尽量返回一个原字符串居中的新字符串
string16 = 'strin'
string16 = string16.center(7,"*")#'*strin*'
string16 = 'string'
string16 = string16.center(7,"*")#'*string'

###endswith(suffix[,start,end]) 判断该字符串的末尾是否是指定的
####suffix 指定的字符串末尾，可以为字符串或者元素(字符串类型)
#### start,end 可选参数 指定起点 终点进行匹配
string17 = "string17"
string17.endswith('17') #True
string17.endswith('17',-2)#True
string17.endswith('ing',3,6)#True

###find(str,start,enb) 
####str 检索的字符串 start开始索引 默认为0 end 结束索引默认为字符串长度
####返回值 如果包含子字符串返回开始的索引值，否则返回-1
string18 = 'string18'
string18.find('18')#6
string18.find('1',6)#6
string18.find('g',4,10)#5