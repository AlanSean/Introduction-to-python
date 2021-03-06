#中文编码
#!usr/bin/python
# -*- coding: utf-8 -*-
#ps 代码一定不要有缩进
# 列表类型以及列表的函数和方法


list = ['hello', 'wrold']
# len 获取查询长度
length = len(list)
# append 添加一个新元素,到列表的末尾
list.append('admin')
# pop删除指定位置的元素
list.pop(len(list)-1)
# insert指定位置添插入元素
#两个参数 1.要插入的位置 2.插入的内容
list.insert(len(list),'admin')
#打印列表
print(list)
#['hello', 'wrold', 'admin']
#如果你输入的下标大于列表长度则会自动插入到列表长度的位置
#即list.insert(len(list),'admin')
list.insert(1000,'admin')
print(list[3]) #admin
# extend 列表追加合并 

list = [123,456]
list1 = [789,101112]
a = list.extend(list1) #[123,456,789,101112]

#index 列表 找出第一个匹配项的的下标(索引位置) 返回下标
list = [123,456,456,'b']
a = list.index(456)
#remove  删除第一个匹配项
list = [123,'a',[1,3,4]]
list.remove([1,3,4]) # list = [123,'a']
#resverse 反向列表
list.resverse()
#sort 排序列表
#list.sort(cmp=None, key=None, reverse=False)
list = [1,2,3,4,6,5]
list.sort()
list.sort(reverse = True)
list = [[1, 6], [2, 3], [3, 7]]
#声明函数
def second(item): 
        return item[1]
list.sort(key = second)
list.sort(key = second,reverse = True)

# operator模块 比较两个列表的元素

import operator
a = [123,'abc']
b = [456,'edf']
operator.lt(a,b) # a < b  从第一个数字或者字母(ASCII)比较
operator.le(a,b) # a <= b
operator.eq(a,b) # a == b
operator.ne(a,b) # a != b
operator.gt(a,b) # a > b
operator.ge(a,b) # a >= b
#返回值是boolean类型


# ord和chr
#ord 字符串转ASCII
#chr 数字转字符串
a = 'a'
a = ord(a) #97
a = chr(a) # 'a'


# max 和 min

#max返回列表的最大值,list元素必须为同一类型,返回最大的值
#max返回列表的最小值,list元素必须为同一类型,返回最小的值
#数字直接比较大小 字符串比较ASCII
list = [123, 456]
print (max(list), min(list))
#456 123
list = ['ab', 'cd']
print (max(list), min(list))
#ascii值 97 98,99 100
#cd ab

# list函数和tuple函数  
将无序集合转为列表,只转换最外1层
list((1, 2, 3, (4, 5))) #[1, 2, 3, (4, 5)] 
将列表转为无序集合,只转换最外1层
tuple([1, 2, 3, [4, 5]]) # (1, 2, 3, [4, 5])
