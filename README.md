# idpwlu README

#AIM
There are a lot of people using the same password for many websites. Even though you could diversify your password between different websites, I'm pretty sure you can only memorize only a few passwords. Using same passwords for many websites/services is not a good practice since if one password gets exposed, there's a great chance that the hacker will be able to get access to your accounts in other websites. One way to avoid such a scenario is to use unique passwords for each account in whatever website you use. But this practice will either require extraordinary memory or some method to save and query the password for your account. Project 'idpwlu', short for 'id/pw lookup', aims to implement the latter approach.

#USED TOOLS
- server: I used my raspberry pi connected to the internet. This has its pros/cons. The merit would be that raspberry pi is cheap and easy to install in your home. It consumes small amount of electricity. However, if for some reason the internet connection is disturbed or the raspberry pi is disfunctinoal, then the user will not be able to use 'idpwlu'. As an alternative, one could use this program in AWS which would be more reliable in terms of connectivity and maintanence but would cost more if the user plans to start an AWS just to use 'idpwlu'. If you already have an AWS instance, then this wouldn't be a problem for you.
