from werkzeug.datastructures import MultiDict

md = MultiDict()
md.add("name", '홍길동')
print (md)

md.add("date", "2018-09-19")
print (md)

md.setlist("dates", ["2018-01-01", '2018-02-01', "2018-03-03"])
print(md)

print ("=================================================")

md.clear()

md.add("id", "hong")
print(md)

md.setdefault("ani", "dog")
print(md)

md.setdefault("id", "hong2")
print(md)

md.setdefault("ani", "cat")
print(md)

md.setdefault("ani1", "cat")
print(md)

print ("=================================================")

md.clear()

md.setlist('ani', ['dog', 'cat'])
print(md)

md.setlistdefault('ani', ['dog1', 'cat1'])
print(md)

md.setlistdefault('ani2', ['dog2', 'cat2'])
print(md)

print ("=================================================")

# append와 extend의 차이점
# append는 객체를 추가 extend는 element를 추가한다. extend는 또 다른 말로 iterable 객체라 한다.
x = [1, 2, 3]
x.append([4, 5])
print(x)

y = [1, 2, 3]
y.extend([4, 5])
print(y)

x.append(['홍'])
print(x)

y.extend(['홍'])
print(y)

print ("=================================================")

md.clear()

md.add('ani', ['dog', 'cat'])
print(md)

#md.setlist('ani', ['dog2', 'cat2'])
#print(md)

md_copy = md.copy()
print(md_copy)

md_deepcopy = md.deepcopy()
print(md_copy)

print("md : " + str(md))

md_copy['ani'].extend(['cat2'])
print(md_copy)

print("md : " + str(md))

md_deepcopy['ani'].extend(['cat3'])
print(md_deepcopy)

print("md : " + str(md))

print ("=================================================")

md.clear()

md.add("ani", "dog")
print(md)

ani_value = md.pop('ani')
print(ani_value)
print("md : " + str(md))

md.add("ani", "cat")
print(md)

ani_value = md.get('ani')
print(ani_value)
print("md : " + str(md))

print ("=================================================")

md.clear()

md.setlist('ani', ['dog', 'cat'])
print(md)

md_value = md.poplist('ani')
print(md_value)
print(md)

print ("=================================================")

md.clear()

md.add('ani', 'cat')
print(md)

md1 = MultiDict()
md1.add('name', '홍')
print(md1)

md.update(md1)
print(md)