# initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

# printing original dictionary
print("the original dictionary : " + str(test_dict))


#initialize value
k = 2


# using loop
# selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

# printing result
print("Frequency of K is : " + str(res))        