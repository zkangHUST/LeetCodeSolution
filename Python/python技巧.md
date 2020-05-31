## enumerate
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
```
s = "I am a stu form hust"
k = s.split()
print(k)
for i, w in  enumerate(s.split(), 1):  //下标从1开始
    print(i, w)
```