from Global_base import login
import requests
import unittest

p = login.LoginByPassWord()
print(p.login_by_password(18127813601)[1])