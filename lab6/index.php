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
    let startDate = new Date();
    const end = 6;

    function uuidv4() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    $(document).ready(function () {
        if (getCookie("session") === null) {
            setCookie("session", uuidv4(), 1)
        }
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
            let t2 = new Date();
            const dif = t2 - startDate;
            let seconds = dif / 1000;
            window.location = `end_page/end_page.php/?score=${score}&amount=${end + 1}&time=${seconds}`;
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
