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
    let score = 0;
    const end = 1;

    $(document).ready(function () {
        $('#question_block').load('/questions/question1.html', function (event) {
            console.log("Start question was load")
        });
    });

    $('#ok').click(function () {
        console.log("Handle for ok button was called")
        let choose = $("input[name='question']:checked").val();
        if (choose === "right") {
            score = score + 1
        }

        if (currentQuestion === end) {
            window.location.pathname = "/end_page.php"
            return
        }

        currentQuestion = currentQuestion + 1;

        $("#question_block").empty().load(`questions/question${currentQuestion + 1}.html`, function (event) {
            console.log("current score")
        });

        event.preventDefault();
    });

</script>

</body>
</html>
