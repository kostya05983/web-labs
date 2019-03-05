<html>
<body>

<div style="align-content: center; margin:auto; width: 50%; text-align: center">
    <?php
    $score = $_GET['score'];
    $amount = $_GET['amount'];
    $time = $_GET['time'];

    echo "Ваш счет $score из $amount; время=$time с";
    echo "<br>";
    $today = getdate();
    echo "$today"
    ?>
</div>

<div style="align-content: center; margin: auto; width: 50%; text-align: center">
    <?php
    $session = $_COOKIE['session'];
    $myfile = fopen("$session.txt", "w") or die("Unable to open file!");
    $score = $_GET['score'];
    $amount = $_GET['amount'];
    $time = $_GET['time'];
    fwrite($myfile, "Счет $score, Из $amount Время $time c \n");
    fclose($myfile);

    //    echo "<button onclick=\"window.location.assign('http://localhost:9092/end_page/$session.txt')\" >Скачать</button>"
    echo "<a href='http://localhost:9092/end_page/$session.txt' download='$session.txt'><button>Скачать статистику</button></a>"
    ?>
</div>


<div style="align-content: center; margin: auto; width: 50%; margin-top: 100px;">
    <?php

    class simplepie
    {
        function __construct($width, $height, $dataArr)
        {
            // Установка переменной окружения для GD
            putenv('GDFONTPATH=' . realpath('.'));
            // Имя шрифта для использования (обратите внимание, что расширение .ttf не указывается)
            $font = '/verdana.ttf';
            $this->image = imagecreate($width, $height);
            $piewidth = $width * 0.70;/* pie area */
            $x = round($piewidth / 2);
            $y = round($height / 2);
            $total = array_sum($dataArr);
            $angle_start = 0;
            $ylegend = 2;
            imagefilledrectangle($this->image, 0, 0, $width, $piewidth, imagecolorallocate($this->image, 128, 128, 128));
            foreach ($dataArr as $label => $value) {
                $angle_done = ($value / $total) * 360;
                /** angle calculated for 360 degrees */
                $perc = round(($value / $total) * 100, 1);
                /** percentage calculated */
                $color = imagecolorallocate($this->image, rand(0, 255), rand(0, 255), rand(0, 255));
                imagefilledarc($this->image, $x, $y, $piewidth, $height, $angle_start, $angle_done += $angle_start, $color, IMG_ARC_PIE);
                $xtext = $x + (cos(deg2rad(($angle_start + $angle_done) / 2)) * ($piewidth / 4));
                $ytext = $y + (sin(deg2rad(($angle_start + $angle_done) / 2)) * ($height / 4));
                imagettftext($this->image, 6, 0, $xtext, $ytext, imagecolorallocate($this->image, 0, 0, 0), $font, "$perc %");
                imagefilledrectangle($this->image, $piewidth + 2, $ylegend, $piewidth + 20, $ylegend += 20, $color);
                imagettftext($this->image, 8, 0, $piewidth + 22, $ylegend, imagecolorallocate($this->image, 0, 0, 0), $font, $label);
                $ylegend += 4;
                $angle_start = $angle_done;
            }
        }

        function render()
        {
            ob_start();
            imagejpeg($this->image, null, 100);

            $rawImageBytes = ob_get_clean();

            echo "<img src='data:image/jpeg;base64," . base64_encode($rawImageBytes) . "' />";
        }

    }


    /** usage */
    $score = $_GET['score'];
    $amount = $_GET['amount'];
    if (0 == $amount - $score) {
        $dataArr = array('неправильные ответы' => $score, 'правильные ответы' => $amount - $score);
        $width = 600;
        $height = 480;
        //    $pie = new simplepie($width, $height, $dataArr);
        $pie = new simplepie($width, $height, $dataArr);
        $pie->render();
    } else {
        $dataArr = array('правильные ответы' => $score, 'неправильные ответы' => $amount - $score);
        $width = 600;
        $height = 480;
        //    $pie = new simplepie($width, $height, $dataArr);
        $pie = new simplepie($width, $height, $dataArr);
        $pie->render();
    }
    ?>
</div>
</body>
</html>
