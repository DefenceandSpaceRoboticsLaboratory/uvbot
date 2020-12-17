<?php


if (file_exists("temp/for.rob")) {
    unlink("temp/for.rob");
} else {
}

if (file_exists("temp/back.rob")) {
    
} else {
    $myfile = fopen("temp/back.rob", "w");
    fwrite($myfile," ");
    fclose($myfile);
}

if (file_exists("temp/left.rob")) {
    unlink("temp/left.rob");
} else {
}

if (file_exists("temp/right.rob")) {
    unlink("temp/right.rob");
} else {
}

?>
