<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>LAB6 Volivach</title>
    <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>

<div id="question_block"></div>
<input id="ok" type="submit" value="Ok">

<script>
    let currentQuestion = 0;
    $(document).ready(function () {
        $('#question_block').load('/questions/question1.html', function (event) {
            alert("Questions was load")
        });
    });

    $('#ok').submit(function (event) {
        alert("Handler for .submit() called.");
        event.preventDefault();
    });

</script>

</body>
</html>
