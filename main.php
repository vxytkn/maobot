<?php
session_start();

//login check
if(!isset($_SESSION["USERID"])) {
    header("Location: logout.php");
    exit;
}

?>
