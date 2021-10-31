nums = {
    1: "one",
    2: "two",
    3: "three"
}
# print(4 not in nums)
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    12: "True"
}

# print(pairs.get("orange"))
# print(pairs.get(7, 12))
# print(pairs.get(12345, "not found"))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, *c, d = range(20)
# print(a)
# print(c)
# print(d)

a = {"a", "b"}
b = {"c", "d", "a"}
# print(a | b) #combines
# print(a & b) #item only in both
# print(a - b) #items only in set 1
# print(a ^ b) #items in either set, but not both

cubes = [i**2 for i in range(10) if i**2 % 2 == 0]
# print(cubes)

userInput = "awesome"
userLen = [i for i in range(len(userInput))]
# newInput
print(userLen)
# output = [i for i in userInput if i != ('a' or 'e' or 'i' or 'o' or 'u')]
# print(output)