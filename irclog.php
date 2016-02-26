<?php
session_start();
session_regenerate_id(true);
//login check
#if(!isset($_SESSION["USERID"])) {
#    header("Location: logout.php");
#    exit;
#}
$default  = parse_ini_file("sql.ini", true)["DEFAULT"];
$sql_user   = $default["user"];
$sql_server = $default["server"];
$sql_pass   = $default["passwd"];
$sql_db     = $default["db"];
if(isset($_POST["submit"])) {
if(!empty($_POST["starttime"]) and !empty($_POST["endtime"])) {
    $sql = new mysqli($sql_server, $sql_user, $sql_pass);
    if($sql->connect_erro) {
        print("<p>DB Failed." . $sql->connect_error);
        exit();
    }

    $sql->select_db($sql_db);
    $starttime = $sql->real_escape_string($_POST["starttime"]);
    $endtime   = $sql->real_escape_string($_POST["endtime"]);
    print($starttime . "~" . $endtime);
    $query = "SELECT * FROM irclog WHERE created BETWEEN '" . $starttime . "' AND '" . $endtime . "'";
    $result = $sql->query($query);
    #print($result);
    while($row = $result->fetch_array()) {
        print($row[0] . $row[1]);
    }
    $sql->close();
}}
?>

<!doctype html>
<html>
<head>
 <meta charset="UTF-8">
 <title> IRC LOG </title>
</head>
<body>
 <form id="logtime" name="logtime" action="" method="POST">
 <fieldset>
 <input type="datetime-local" id="starttime" name="starttime" value="<?php echo(date('Y-m-d H:i:s', time()-60*60*24)) ?>">
 <input type="datetime-local" id="endtime" name="endtime" value="<?php echo(date('Y-m-d H:i:s')) ?>">
 <input type="submit" id="submit" name="submit" value="submit">
 </fieldset>
 </form>
</body>
</html>
