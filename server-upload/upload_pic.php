<?php

date_default_timezone_set('America/New_York');

$str = file_get_contents('php://input');

$filestr = date("Y_m_d_H_i_s") . ".jpg";

$upload_path = "uploads/";
$latest_path = "latest/latest.jpg";

$fullpath = $upload_path . $filestr;

file_put_contents($fullpath, $str);

file_put_contents($latest_path, $str);

?>
