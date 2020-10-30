def my_hash(inputStr):
    #takes inputStr abd returns a number
    #'foo' --> [x, y, z]
    sb = inputStr.encode() #the ytf-8 bytes for he string
    total = 0
    for b in sb:
        total += b
    return total

# print(my_hash('foo'))

my_table = [None] * 8
#store key "foo" with value "bar"
hash_index = my_hash("foo") % len(my_table)
my_table[hash_index] = "bar"
print(my_table)

#get value w/ key
get_hash_index = my_hash('foo') % len(my_table)
# print(my_table[get_hash_index])
print(my_table)
#delete value w/ key "foo"
delete_hash_index = my_hash('foo') % len(my_table)
my_table[delete_hash_index] = None
# print(my_table[delete_hash_index])
print(my_table)
# def hash_get(key, value):
