#!/usr/bin/env python3

head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>first Question</title>
</head>
<body>
"""

first_question = """
 <p>В каком случае водитель совершит вынужденную остановку?</p>
    <form id="choose" action="/cgi-bin/question.py" method="%s" target="_blank"
      style="align-self: center; text-align: center">
    <input type="radio" name="question" value="on"/> Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу
    <input type="radio" name="question" value="off"/> Остановившись на проезжей части из-за технической неисправности транспортного средства
    <input type="radio" name="question" value="off"/> В обоих перечисленных случаях
    <input type="submit" value="Ок"/>
</form>
"""

import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

method = form.getvalue("form")

if form.getvalue("form"):
    print(head)
    print(first_question % "GET")
else:
    print(first_question % "POST")
