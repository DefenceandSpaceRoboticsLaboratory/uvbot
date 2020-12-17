<?php

$contents='';
foreach ($_GET as $key => $value) {
    $contents.= "\n".$value;            
}
file_put_contents("temp/speed.rob", $contents, FILE_APPEND);


?>