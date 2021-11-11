<?php

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion($s) {
    $amConversion = [
        '01' => '01',
        '02' => '02',
        '03' => '03',
        '04' => '04',
        '05' => '05',
        '06' => '06',
        '07' => '07',
        '08' => '08',
        '09' => '09',
        '10' => '10',
        '11' => '11',
        '12' => '00',
    ];
    $pmConversion = [
        '01' => '13',
        '02' => '14',
        '03' => '15',
        '04' => '16',
        '05' => '17',
        '06' => '18',
        '07' => '19',
        '08' => '20',
        '09' => '21',
        '10' => '22',
        '11' => '23',
        '12' => '12',
    ];
    $type = substr($s, 8, 2);
    $hours = substr($s, 0, 2);
    $minutesAndSecconds = substr($s, 2, 6);
    
    if($type == 'AM'){
        return $amConversion[strval($hours)].$minutesAndSecconds;
    } else {
        return $pmConversion[strval($hours)].$minutesAndSecconds;
    }
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$s = rtrim(fgets(STDIN), "\r\n");

$result = timeConversion($s);

fwrite($fptr, $result . "\n");

fclose($fptr);
