#!/usr/bin/env python3
import cgi, cgitb
import http.cookies
import os
from CookStorage import CookStorage
import uuid

head = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>first Question</title>
   <link href="styles.css" rel="stylesheet">
</head>
<body style="background-color: white" >
"""

questions = [["В каком случае водитель совершит вынужденную остановку?",
              ["Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу",
               "Остановившись на проезжей части из-за технической неисправности транспортного средства",
               "В обоих перечисленных случаях"], "1"],
             ["Что означает мигание зелёного сигнала светофора?",
              [
                  "Предупреждает о неисправности светофора",
                  "Разрешает движение и информирует о том, что вскоре будет включен запрещающий сигнал",
                  "Запрещает дальнейшее движение"
              ], "1"],
             ["Водитель обязан подавать сигналы световыми указателями поворота (рукой):",
              [
                  "Перед началом движения или перестроением",
                  "Перед поворотом или разворотом",
                  "Перед остановкой",
                  "Во всех перечисленных случаях"
              ], "3"],
             [
                 "Для перевозки людей на мотоцикле водитель должен иметь водительское удостоверение на право управления транспортными средствами",
                 [
                     "Категории «A» или подкатегории «A1»",
                     "Любой категории или подкатегории в течение 2 и более лет",
                     "Только категории «A» или подкатегории «A1» в течение 2 и более лет"
                 ], "2"],
             ["При какой неисправности разрешается эксплуатация транспортного средства?",
              [
                  "Не работают пробки топливных баков",
                  "Не работает механизм регулировки положения сиденья водителя",
                  "Не работают устройства обогрева и обдува стекол",
                  "Не работает стеклоподъемник"
              ], "3"],
             ["В случае, когда правые колёса автомобиля наезжают на неукреплённую влажную обочину, рекомендуется:",
              [
                  "Затормозить и полностью остановиться",
                  "Затормозить и плавно направить автомобиль на проезжую часть",
                  "Не прибегая к торможению, плавно направить автомобиль на проезжую часть"
              ], "2"],
             ["Что понимается под временем реакции водителя?",
              [
                  "Время с момента обнаружения водителем опасности до полной остановки транспортного средства",
                  "Время с момента обнаружения водителем опасности до начала принятия мер по её избежанию",
                  "Время, необходимое для переноса ноги с педали управления подачи топлива на педаль тормоза"
              ], "1"]
             ]

form_start = """
<p>%s</p>
    <form id="choose" action="/cgi-bin/startForm.py" method="%s" target="_self"
      style="align-self: center; text-align: left">
"""
form_end = """
    <input type="submit" value="Ок"/>
</form>
"""

common_question = """
    <input class="container" type="radio" name="question" value="%d"/> %s
    <br>
"""

current_count = """
<p>Текущий счет %s</p>
"""

end_body = """
    Поздравляем вы верно ответили на %d из %d вопросов
    <br>
     <form id="repeat" action="http://localhost:8000" method="GET">
    Повторить?
    <br>
    <input type="submit" value="Да"/>
    </form>
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
    i = 0
    for value in questions[current][1]:
        print(common_question % (i, value))
        i = i + 1
    print(form_end)
    if current == 0:
        print(current_count % 0)
    else:
        print(current_count % cook["result"].value)


def right_answer():
    current = storage.find_cookie_session(cook["session"].value, "current")
    value = form.getvalue("question")
    res = storage.find_cookie_session(cook["session"].value, "result")
    if int(questions[current - 1][2]) == int(value):
        res = storage.find_cookie_session(cook["session"].value, "result")
        res = res + 1
        storage.set_cookie_result(cook["session"].value, "result", int(res))
    cook["result"] = res
    print("Set-cookie: result=%d" % res)


def if_last():
    current = storage.find_cookie_session(cook["session"].value, "current")
    if current is None:
        method = form.getvalue("method")
        storage.set_cookie_result(cook["session"].value, "result", 0)
        storage.set_cookie_result(cook["session"].value, "current", 0)
        print("Set-cookie: result=0")
        print("Set-cookie: method=%s" % method)
    else:
        right_answer()

    print("Content-type: text/html\n")
    print(head)
    if current == len(questions):
        res = storage.find_cookie_session(cook["session"].value, "result")
        print(end_body % (res, len(questions)))
        storage.set_cookie_result(cook["session"].value, "current", None)
    else:
        print_form(get_method(), storage.find_cookie_session(cook["session"].value, "current"))
        increment_current()


def get_method():
    if cook.get("method") is None:
        method = "GET"
        return method
    else:
        method = cook.get("method")
        return method.value


def check_session():
    if cook.get("session") is None:
        id = uuid.uuid1()
        cook["session"] = id
        print("Set-cookie: session=%s" % id)


storage = CookStorage()
cook = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
check_session()

form = cgi.FieldStorage()
if_last()
