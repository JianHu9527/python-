# -*- coding: utf-8 -*-
# @Time    : 2023/04/21 下午 3:47
# @Author  : XXX
# @Site    : 
# @File    :
# @Software: PyCharm 
# @Comment :字符串操作
print("---查看内存"*5)
# 查看函数的内存地址 id（变量）
cpu_name = "124567989"
print(id(cpu_name))
print("---字符串操作"*5)
my_str = "hellow,python,python"
print(my_str.capitalize())
# 分割符:.split（） 对数据进行分割,可以指定分割次数,未指定的话默认全部分割,如果不存在会报错，且分割的会消失
print(my_str.split("py", 1))  # ['hellow,', 'thon,python']
#  查找字符串中出现的次数：.count
print(my_str.count("p"))
# 查找字符串的长度：len
print(len(my_str))
#  判断字符串是否为什么开头：startswith  是的话为True
print(my_str.startswith("py"))
#  判断字符串是否为什么结尾或者文件是否为.py或者其他格式结尾：endswith  是的话为True
print(my_str.endswith("py"))
info_str = "jd_2019_09_02.py"
print(info_str.endswith(".py"))
#  查找 find 返回索引从0开始 多个相同返回默认出现的第一个索引 没有为-1 下面代码继续执行
#  rfind 似find 不过是从后往前找 print(my_str.rfind("on"))
#  查找 index 与find用法一致 但是找不到会失败不执行下面的代码
#  rindex从右侧到左侧查询 找不到还是会异常报错
print(my_str.find("e"))
print(my_str.find("python", 8))  # 从索引8开始找
print(my_str.find("python", 8, len(my_str)))
#  替换 replace(旧的，新的，替换几次）不指定的话默认全部 也可以倒序替换
print(my_str.replace("python", "go", 1))

# partition 将数据类型从左往右将数据进行分割 print(my_str.partition("on"))# ('hellow,pyth', 'on', ',python')
# rpartition 将数据类型从右像左边进行数据分割

# isalpha 判断所有字符都是字母，返回ture / false
# isalpha 判断只包含数字 返回ture / false
# isalnum 判断字符都是字母或者数字 返回ture / false
# isspace 判断是否包含空格 返回ture

# join每个元素后面插入字符串 构造出一个新的字符串
# print(my_str.join("@@!"))  # @hellow,python,python@hellow,python,python!
#  .ljust返回一个原字符串左对齐，并默认使用空格填充至长度
print(my_str.ljust(30, "2"))  # hellow,python,python2222222222
#  .rjust 返回一个原字符串左对齐，并使用空格填充至长度
print(my_str.rjust(30, "2"))  # 2222222222hellow,python,python
#  .center 返回一个字符串居中 并使用空格键填充至长度
print(my_str.center(30, "2"))  # 22222hellow,python,python22222

# strip 删除字符串两端的空白字符  print(my_str.strip(" @")) 也可以指定去除字符 但是指定字符前面有空格只去除空格
# lstrip 删除字符串左边空白的字符
# rstrip 删除末端的空白字符

# upper修改为大写 lower或者casefold首字母修改为小写 title或者capitalize修改首字母大写
print(my_str.title())

# splitlines 按照行分割，返回一个各行作为元素的列表
# print(my_str.splitlines()) # ['hellow,python,python']

print("---切片---" * 5)
#  切片 split[开始位置索引，结束下标，步长]
#  作用：从大字符串快速切出小字符串
#  说明：切片的范围，包含开始索引，不包含结束位置索引，左避右开 只能获取结束位置前的一个字符
#  注意：获取数据的步调步长，步长为1可以省略
#  结论:切片中开始索引或结束索引涉及到字符串的边界，则开始索引或结束索引可以省略
#  正序切片，从左往右,如果结束索引就是字符串的末尾，则结束索引可以省略,
#  步长为正1步长可以省略。步长前面的冒号可以省略
my_str1 = "hellow,python,python"
print(my_str1[0:5:1])  # 切出hello
print(my_str1[-1:-7:-1])  # 倒序切片 nohtyp

print("---列表---" * 5)
#  列表:用来存放多个数据的高级容器(有序的容器)
#  格式:列表名=[数据1,数据2，...数据3]
#  列表名=[]或列表名= list() 空列表
#  访问列表中数据:通过索引访问:列表名[索引值] (注意:索引不要越界)
list_name = [1, 3.22, True, "hellow"]
print(list_name[3])  # 索引 hellow
#  列表.insert(索引，数据)在指定位置插入数据
list_name.insert(2, "Hj")  # 也可以插入小列表或者小元组或者组合
print(list_name)
#  列表.append (数据)在末尾追加数据
list_name.append("haha")
print(list_name)
#  列表1.extend(列表2) 将列表2的数据追加到列表1(把列表2合并到列表1里边去）
#  删除
#  del 列表[索引] 删除指定的索引数据 #  把列表从内存里边清空 del 列表名
#  列表.remove（数据） 删除第一个出现的指定数据
#  列表.pop（） 删除末尾数据，返回删除的数据
#  列表.pop（索引） 删除指定的索引数据，返回删除的数据
#  列表.clear（） 清空列表
#  修改
#  #列表[索引] = 数据修改指定索引的数据 #  列表中的数据可以修改
#  查#通过索引获取数据 #1.列表名[索引] #2.通过数据获取索引
#  列表名.index (数据)获取数据在列表中第一次出现的索引值
#  统计
#  len(列表) 列表长度(列表中元素的个数)
#  列表.count(数据)数据在列表中出现的次数
#  排序
#  列表.sort()升序排序(从小到大排序) 列表.sort(REVERSE = True)降序排序
#  列表逆序 列表.reverse（） 前面的数据放后面 后面的数据放前面
#  拷贝 列表.copy（）

print("---元组---" * 5)
#  元组:也是用来存储多个数据的高级容器, (可以存储存储任意数据类型)
#  注意:元组中的数据修改是受到限制的
#  格式:元组名= (数据1,数据2,数据3,
#  只有一个元素的元组，元组 = （数据, )需要在数据后面加逗号
my_tuple = (100, 12.3, False, "python", 20, "中文", [100, 123])
#  1.访问元组的中数据 通过索引访问数据:元组名[索引值/下标]
#  元组中的数据不支持修改  但是元组中右列表或者字典可以修改
my_tuple[6][1] = 101
print(my_tuple)
#  2.通过数据获取索引元组名.index(数据) 数据不存在报错
#  3.统计元组中某个数据出现的次数 元组.count (数据)
#  4.统计元组的长度 len（元组名）

print("---字典---" * 5)
#  字典用来存储的数据的高级容器(字典中的数据是无序)
#  作用:字典主要用来存储一个人物或事物的详细信息的，不能通过索引的方式访问
#  以键值对的方式存储的，键key 值(value)，字典中以键值对的方式来存储数据的
#  格式:字典名= {key1:value1, key2:value2, key3:value3 ...}
#  1.字典中的键key是唯一的，字典中有 相同的键key对应不同的值,后面的值会替换前面的值
#  my_ _dict = {'name': '常威'，'age': 30， 'high': 180.5， 'age': 40, 'age': 50}
#  2.字典中key键的数据类型,可以是除了列表和字典以外的所有数据类型，字曲中的键key不能是列表或字曲本身
#  列表不能作为字典的键值，字典本身也不能作为字典的键
#  3.字典是无序的
my_dict = {'name': '上官翠花', 'age': 22, 'gender': "女", 'high': 172.5}
print(my_dict['name'])  # 键存在时返回，不存在下面代码不执行
print(my_dict.get("ood"))  # 字典名.get（"key"）找的键值对不存在也不会影响下面的代码执行返回None
#  增/改
#  字典名[key] = value key存在就修改，不存在就增加键值对
#  字典名.setdefault(key, value) key存在 ,不修改对应value值，使用默认值，不存在的话改变
#  字典1.update(字典2) 把字典2合并到字典1, key存在,更新对应的value值，key不存在,添加进去
#  删
#  1.del 字典名[key] key存在 ,正常删除键值对，key不存在,报错
#  2.字典名.pop(key) key存在,正常删除键值对，key不存在 ,报错
#  3.字典名.clear(）# 清空字典
#  字典的高级应用:
#  1. Len(字典名)获取的字 典中键值对的个数
#  2.高级用法.了解
#  ①字典名.keys()  获取所有 的键(key)组成的特殊的列表
#  ②字典名.values()  获取所有的值(value)组成的特殊的列表
#  ③字典名.items()  获取所有的键( key )和值(value)组成元组,元组组成的特殊的列表


# for循环小结:
# 作用:主要用来遍历列表,元组,字典,字符串这样的序列容器,遍历就是一个一个的从容器中获取数据
# 语法:for 临时变量 in 容器:
#         对临时变量的处理
# 说明: for可以遍历列表,元组,字典,字符串这样的序列容器


