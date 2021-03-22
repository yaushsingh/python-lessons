import re 
#importing regular expression
email = 'ayushsingh2098@gmail.com'
expression = '[a-z\.0-9]+' 

matches = re.findall(expression,email)
#re.findall(,) gives list of pattern that matches the passed argument
print(matches) 
userid = matches[0]
domain = f'{matches[1]}'
print(userid)
print(domain)

#can also bedone as
"""email = 'ayushsingh3232@gmail.com'
parts = email.split('@')
names = parts[0]
domain = parts[1]
print(userid)
print(domain)"""

price = "Price : $1449.0"
expression ="Price : \$([0-9]*\.[0-9]*)" 
#above expression is generaliztion of our search expression
#* means anything of number inside all big bracket
#() helps to group the specific string
matches = re.search(expression, price) #gives only matched expression
print(matches.group(0)) #entire match
print(matches.group(1)) #first thing in brackets

#turning string into python number
price_number = float(matches.group(1))

#for removing comma from price
price_with_comma = "price : 12,689.09"
search_exp = "([0-9,]*\.[0-9])"
match = re.search(search_exp,price_with_comma)
price_without_comma = matches.group(1).replace(',','') #
price_num = float(price_without_comma)
print(type(price_num))