<?php
session_start();
session_regenerate_id(true);
//---------------------
//connection to server
//---------------------

$ini_array  = parse_ini_file("sql.ini", true);
$default    = $ini_array["DEFAULT"];
$sql_user   = $default["user"];
$sql_server = $default["server"];
$sql_pass   = $default["passwd"];
$sql_db     = $default["db"];

#print_r($sql_user);
#print_r($sql_server);
#print_r($sql_db);

$sql_Con = mysqli_connect($sql_server, 
    $sql_user, $sql_pass);
if (!$sql_Con) {
    die("Connection Failed.");
} else {
#   print_r("Success.");
}

//------------------------
//connection to DB
//------------------------
if (!mysql_select_db($sql_db)) {
    die("DB Failed.");
} else {
#   print_r("DB SUCCESS.");
}
#print_r($_SESSION);
//------------------------
//login
//------------------------

?>

