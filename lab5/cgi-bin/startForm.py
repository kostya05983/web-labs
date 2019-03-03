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
    <input type="radio" name="question" value="%d"/> %s
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
    i = 1
    for value in questions[current][1]:
        print(common_question % (i, value))
        i = i + 1
    print(form_end)


def right_answer():
    current = storage.find_cookie_session(cook["session"].value, "current")
    value = form.getvalue("question")
    res = storage.find_cookie_session(cook["session"].value, "result")
    if (res == 0):
        res = 0
    if int(questions[current - 1][2]) == value:
        res = storage.find_cookie_session(cook["session"].value, "result")
        storage.set_cookie_result(cook["session"].value, "result", int(res) + 1)
    print("Set-cookie: result=" + res)


def if_last():
    current = storage.find_cookie_session(cook["session"].value, "current")
    print("Content-type: text/html\n")
    print(head)
    if current == len(questions):
        print("Uryaaa")
        storage.set_cookie_result(cook["session"].value, "current", 0)
    else:
        method = "GET"
        if current == 0:
            method = form.getvalue("method")
        print(storage.find_cookie_session(cook["session"].value, "current"))
        print_form(method, storage.find_cookie_session(cook["session"].value, "current"))
        if current != 0:
            right_answer()
        increment_current()


storage = CookStorage()
cook = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
form = cgi.FieldStorage()
if_last()
# Create instance of FieldStorage
