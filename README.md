
# GRAPHICAL PASSWORD AUTHENTICATION 

The existing method of authentication in use today is alphanumerical usernames and passwords where there is a risk of stealing passwords or forgetting passwords due to long lengths. Most of the people forget the password and resets them. The proposed authentication system to overcome the limitations of textual passwords is Recognition Based Graphical password authentication system. Graphical passwords refer to using pictures (also drawings) as passwords. In this the user has to set passwords in the form of graphical objects in a certain pattern and later use that pattern to login to the system.

## Problem Statement

In today’s IT world, for computer and information security the user authentication plays a significant role. For this authentication a password is a very important aspect. The conventional method of alphanumeric(Textual) passwords has certain drawbacks I.e. problem of memorability, and vulnerable to various attacks like brute force, dictionary attack, spyware, guessing.

## Recognition Based System: 

In this type of graphical authentication technique multiple images are shown to user at registration phase. User has to select some images in a particular order to keep it as their password. So, at the time of login the selected images are shuffled and displayed to the user. The user has to select the images in the same order as selected at the time of registration. Every time the user will have to use the same sequence while the images are placed in different ways.

## Two Step Verification:

In graphical authentication technique multiple images are shown to user at registration phase. During this process there is risk of shoulder surfing so we can make it more securely by having OTP verification to email by using the Pega tool. When the images are selected in successful way the Email verification starts. User has to enter the correct OTP to move forward.

## hacker try to craack this system(simple calculations)

- 5*4=20 imgs
- shuffling imgs 20! ie
20! = 2432902008176640000
- selecting min 5 img (ie combinations 20C5)
20C5=15504
- calculat shuffling imgs* -selecting min 5 img out of 20 imgs
ie: 20!*15504=37719712734770626560000 combinations
- every 5 attemps will be faild account will be blocked 1H
 ie 37719712734770626560000/5=7543942546954125312000H
- convert days 
7543942546954125312000/24=314330939456421888000 days 
- convert Years 
314330939456421888000/365=861180656044991473.972... years 
