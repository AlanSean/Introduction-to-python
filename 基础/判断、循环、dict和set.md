# 条件判断

```
num = input('随便输入一个数字:')
try 
num = int(num)
except ValueError as e:
    print('你输入的不是数字')
if num > 0:
    print('你输入的数字大于0')
elif num < 0:
    print('你输入的数字小于0')
else:
    print('你输入的数字等于0')
```

#循环
```
#for x in list 将序列的每个元素代入变量x

list = [1,2,3]
for item in range(101):
    print(item)
#while 条件为true 就一直循环

num = 0
flag = True
while flag:
    if num == 2:
        flag = False
    else:
        num = num +1
#flag = False num =2

#break 强制结束循环

num = 0
flag = True
while flag:
    if num == 2:
        flag = False
    else:
        num = num +1
        break
#flag = Ture num =1

#continue 结束本轮循环执行下一次
num = 0
flag = True
while num < 5:
    num = num +1
    if num == 3:
        continue
    print(num)
# 1 2 4 5
```

#dict词典和set
```
#dict 有点像json对象
obj = {
    'name': '小明',
    'age': 18
}
#dict方法
## get get(key,key不存在时你想反回的值)

obj.get('name',None)

## pop pop(key) 删除key以及值

if 'age' in obj :
    obj.pop('age')

## clear 删除所有元素

obj.clear()

## copy 浅复制 以及直接赋值的区别

obj1 = {
    'name': '小明',
    'age': 18
}
obj2 = obj1.copy() #只会深拷贝父级对象 子对象还是浅拷贝
obj3 = obj1  #随obj1 元素变化
obj1['names'] = '大明'
print(obj2,obj3) # {'name': '小明', 'age': 18} {'name': '小明', 'age': 18, 'names': '大明'}、

##items 返回可遍历的键 值 元组数组(tuple)

item = obj.items() #dict_items([('name', 1)])

##keys 返回所有的键

obj = {
    'name': '小明',
    'dict': {
        'index': 1
    }
}
obj.keys() #dict_keys(['name']),不返回二维以上的

##values 返回所有的值 只返回一维
obj.values() #dict_values(['小明', {'index': 1}])

##update 更新词典(dict),两个dict的合并

obj1 = {
    'sex': '男'
}
obj.update(obj1) #{'name': '小明', 'dict': {'index': 1}, 'sex': '男'}

##popitem 随机删除一对键值
obj.popitem() #('sex', '男') 返回删除的键值对类型为元祖 tuple

#set
#和dict类似 但是没有值 只存储key，并且key不能为重复 输入重复也无效果
sets = set([1, 2, 3]) #{1, 2, 3}

## 方法
## add(key)
sets.add(4) #{1, 2, 3, 4}
## remove(key)
sets.remove(1) #{2, 3, 4}

```