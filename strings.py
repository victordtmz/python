# #!/usr/bin/venv python3
# #left and right align number of spaces, if number is smaller, it will fill with ceros - can alsu be used with f string. 
# # x = 'seven "{1:<020}" "{0:>09}"'.format(5646548, 9)
# # print('x is {}'.format(x), end='')



# x = '------ This is a string for testing purposes ----- '

# # will center the string within 100 characters
# print(x.center(100))
# #                         ------ This is a string for testing purposes -----

# #more agressive than lower, used mainly in other laguages - alphabets
# print(x.casefold())
# # ------ this is a string for testing purposes ----- 

# #all to lower case
# print(x.lower())
# # ------ this is a string for testing purposes -----

# # all tu upper case
# print(x.upper())
# # ------ THIS IS A STRING FOR TESTING PURPOSES -----


# x  = x.ljust(75)
# print(x, 'this is after justification')
# # ------ This is a string for testing purposes -----                          this is after justification

# x = '------ This is a string for testing purposes -----'

# print(x.count('p'))
# # 2 - prints the occurances of p

# # encodes the string
# print(x.encode('utf-8'))
# # b'------ This is a string for testing purposes ----- '

# #returns true if ends with given parameter 
# print(x.endswith('-'))
# # True
# x = '------ T\this is a string for testing purposes -----'
# print(x.expandtabs(8))
# # ------ T    his is a string for testing purposes -----
# # ------ T        his is a string for testing purposes ----- #this is an example with 8 spaces - above with 4

# # The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
# #it takes up to 3 parameters:
# # 1. sub - it is the substring to be searched in the sting
# # 2. start - index to start searching
# # 3. end - index to complete search
# x = '------ This is a string for testing purposes -----'
# print(x.find('is',5,11)) #returns 9
# print(x.find('for')) #returns 24

# print(x.index('a'))# returns the index of the first instance. 

# y = '1354684321abc-'
# # print(y.isalnum())#returns true if all characters are numbers or letters - alphanumeric

# z = ['1000', '1,000', '1000.50']
# for y in z:
#     print(y.isdecimal())
#     print(y.isdigit())
#     print(y.isnumeric())


class Solution(object):
   def romanToInt(self, romainImput):
      """
      :type s: str
      :rtype: int
      """
      romanConvertionDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(romainImput):
         if i+1<len(romainImput) and romainImput[i:i+2] in romanConvertionDict:
            num+=romanConvertionDict[romainImput[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=romanConvertionDict[romainImput[i]]
            i+=1
      return num
ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))