anonymous_filter = lambda x: x.lower().count('я') >= 23
print(anonymous_filter("яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!"))
