#!/usr/bin/env python3
import cgi, cgitb
import http.cookies
import os
from CookStorage import CookStorage

head = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>first Question</title>
</head>
<body>
"""

questions = [["В каком случае водитель совершит вынужденную остановку?",
              ["Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу",
               "В обоих перечисленных случаях"], "1"]]

form_start = """
<p>%s</p>
    <form id="choose" action="/cgi-bin/startForm.py" method="%s" target="_blank"
      style="align-self: center; text-align: center">
"""
form_end = """
    <input type="submit" value="Ок"/>
</form>
"""

common_question = """
    <input type="radio" name="question" value="1"/> %s
    <br>
"""


def increment_current():
    cook = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    res = storage.find_cookie_session(cook["session"].value, "current")
    if res is not None:
        storage.set_cookie_result(cook["session"].value, "current",
                                  int(res) + 1)
    else:
        storage.set_cookie_result(cook["session"].value, "current", 0)

def print_form(method, current):
    print(form_start % (questions[current][0], method))
    for value in questions[current][1]:
        print(common_question % value)
    print(form_end)


storage = CookStorage()
cook = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
# Create instance of FieldStorage
form = cgi.FieldStorage()

value = form.getvalue("question")

increment_current()
print("Content-type: text/html\n")
print(head)
print(value)
print(storage.find_cookie_session(cook["session"].value, "current"))
print_form("GET", storage.find_cookie_session(cook["session"].value, "current"))
print()
