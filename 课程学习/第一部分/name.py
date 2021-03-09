name="ada lovelace"
# 将每个单词的首字母都改为大写
print(name.title())
print(name.lower())
first = "ada"
second = "lovelace"
fullname =first +second
print(fullname)
user_o = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key,value in user_o.items():
    print(key)
    print(value)
pizza ={
    'crust':'think',
    'toppings':['mushrooms','extra cheese'],
}
for topping in pizza['toppings']:
    print("\t"+topping)

message = input('fuck')
print(message)