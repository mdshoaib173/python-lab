Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> print("shoaib")
shoaib
>>> a=20
>>> b=100
>>> print(a+b)
120
>>> a="python programming"
>>> a[0]
'p'
>>> len(a)
18
>>> a[o:5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[o:5]
NameError: name 'o' is not defined
>>> a[0:5]
'pytho'
>>> print(a.upper())
PYTHON PROGRAMMING
>>> print(a.lower())
python programming
>>> print(a.replace("python", "c"))
c programming
>>> a=[1,2,4,8,-3,4.8,'b']
>>> a.append(5)
>>> print(a)
[1, 2, 4, 8, -3, 4.8, 'b', 5]
>>> a
[1, 2, 4, 8, -3, 4.8, 'b', 5]
>>> b=[1,4,5]
>>> a.extend(['a','b','c'])
>>> a
[1, 2, 4, 8, -3, 4.8, 'b', 5, 'a', 'b', 'c']
>>> a.extend(b)
>>> a
[1, 2, 4, 8, -3, 4.8, 'b', 5, 'a', 'b', 'c', 1, 4, 5]
>>> a=['2',4,5]
>>> b=[5,6,7]
>>> a+b
['2', 4, 5, 5, 6, 7]
>>> a.index(5)
2
>>> a.len(5)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.len(5)
AttributeError: 'list' object has no attribute 'len'
>>> a=["cmr","good","college"]
>>> a.insert(1,"is")
>>> a
['cmr', 'is', 'good', 'college']
>>> a.replace(3,"university")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.replace(3,"university")
AttributeError: 'list' object has no attribute 'replace'
>>> a.replace("college","university")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.replace("college","university")
AttributeError: 'list' object has no attribute 'replace'
>>> a.replace("college","university",3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.replace("college","university",3)
AttributeError: 'list' object has no attribute 'replace'
>>> a.pop("college")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.pop("college")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(3)
'college'
>>> a
['cmr', 'is', 'good']
>>> a.insert(3,"university")
>>> a
['cmr', 'is', 'good', 'university']
>>> a.count(2)
0
>>> 
a.sort
<built-in method sort of list object at 0x7fbec959a908>
>>> 
>>> a
['cmr', 'is', 'good', 'university']
>>> a=["sachin",15000,"dravid",12000"sehwag",10000]
SyntaxError: invalid syntax
>>> a=["sachin",15000,"dravid",12000,"sehwag",10000]
>>> #to display sachin's runs
>>> a=[0:1]
SyntaxError: invalid syntax
>>> a[0:1]
['sachin']
>>> a[0;2]
SyntaxError: invalid syntax
>>> a[0:2]
['sachin', 15000]
>>> #to display dravid's runs
>>> a[3:5]
[12000, 'sehwag']
>>> a[2:4]
['dravid', 12000]
>>> a=(1,2,3,"a")
>>> a*2
(1, 2, 3, 'a', 1, 2, 3, 'a')
>>> 
