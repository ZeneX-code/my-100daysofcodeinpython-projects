'''So this is the First project of the !00 days coding challenge in python
this project only includes all the basic I have learned in the 7 days.'''

''' Created by Zenex(Aakash Shakya) on 6 august, 2019'''

'''this project is about the user authentication and allow users to make a write their thoughts.'''




import time
# import date

print('welcome to the Page... \nEnter your username and Password to LOGIN...')

UserName = str(input('UserName... '))
password = str(input('password... '))
localtime = time.asctime( time.localtime(time.time()))


print("checking the username and password...")

''' relax, here is a function '''

def relax(x,y):
    print('do you want to write...')
    answer=input('yes/no... ')

    if answer=='yes':
        print('the screen is yours\nwrite anything you want...')
        blog=input()
        print('you wrote...\n')
        return blog
    else:
        print('no worries...')

# def checker(a):
#     if len(password<8):
#         print('your password is less than 8 digits...')
#     else:
#         return 0

time.sleep(2)

if UserName==" ":
    if password==" ":
        print('please enter your username and password...')

    elif password!="password":
        print("enter your username and your password...")

    else :
        print("enter your username...")


elif UserName!="username":
    if password==" ":
        print('Enter your correct username and \nenter your password...')
    elif password!="username":
        print("enter correct username and password...")
    else:
        print("enter your correct username...")

else:
    if password=="password":
        print('Welcome in Zenex...')
        print(localtime)
        time.sleep(1)
        response=relax(UserName,password)
        print(response)


    elif password=="":
        print("enter your password...")
    elif password!="password":

        print("enter correct password...")
