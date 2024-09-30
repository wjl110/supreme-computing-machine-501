text = "hello world"

substring = "world"

text_1 = "Lingnan_University_in_HongKong"

count = text.count(substring)
print(count)
#Calculate the number of times substring appears in text and return it to count
#Output result: 1

position = text.find(substring)
print(position)
#Find the position of substring in text and return its value to position
#Output result: 6

join = text.join(substring)
print(join)
#Use the join method on text and pass the parameter substring into the join method. The final result is returned to join, that is w+text+o+text+r+text+l+text+d
#Output result: whello worldohello worldrhello worldlhello worldd

replace = text.replace(substring, "Lingnan University")
print(replace)
#The replace method replaces the substring in the text with the value passed as a parameter and returns the replaced result to replace
#Output result: hello Lingnan University


split = text.split(substring)

print(split)
#Example 1: Split the text into substrings and return the split result to split
#Output result: ['hello ',' ']

#Why there are spaces in the output result here will be explained in detail in the practice of Example 3

split_default = text.split()
print(split_default)
#The split method does not pass any parameters and will be split by space by default, for example, in this Example 2
#Output result:['hello', 'world']

#Secondly, why are there parentheses [] in the output result here? Because the split method returns a "list" that stores the split string, there will be parentheses [] in the output result
#It can be understood as dividing a string into an array of strings, and then placing the array in a list to form a list


split_custom = text_1.split("_")
print(split_custom)
#You can test using some custom symbols to segment text, such as this Example 3
#Output result:['Lingnan', 'University', 'in', 'HongKong']

#At this point, it is easy to understand why whitespace appears in Example 1, because the split method treats the passed parameters as whitespace and divides the text into spaces, resulting in whitespace

startswith = text.startswith(substring)
print(startswith)
#Determine whether the text starts with substring and return the result to startswift; If yes, return True; otherwise, return False
#Output result: False

endswith = text.endswith(substring)
print(endswith)
#Determine whether the text ends with a substring and return the result to endswift
#Output result: True

#⚠️Boolean values returned by both startswift and endswift, namely True and False

lower = text.lower()
print(lower)
#Convert all text to lowercase and return the converted result to lower
#Output result: hello world
