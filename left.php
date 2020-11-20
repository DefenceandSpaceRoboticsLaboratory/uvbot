<?php

if (file_exists("temp/for.rob")) {
    unlink("temp/for.rob");
} else {
}

if (file_exists("temp/back.rob")) {
    unlink("temp/back.rob");
} else {
}

if (file_exists("temp/left.rob")) {

} else {
    $myfile = fopen("temp/left.rob", "w");
    fwrite($myfile," ");
    fclose($myfile);
}

if (file_exists("temp/right.rob")) {
    unlink("temp/right.rob");
} else {
}
?>
