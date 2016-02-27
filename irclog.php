<!doctype html>
<html>
<head>
 <meta charset="utf-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title> IRC LOG </title>
 <link href="css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
 <script src="js/bootstrap.min.js"></script>

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
$sql = new mysqli($sql_server, $sql_user, $sql_pass);

//sql error
if($sql->connect_error) {
    print("<p>DB Failed." . $sql->connect_error);
    exit();
}

$sql->select_db($sql_db);
$starttime = $sql->real_escape_string($_POST["starttime"]);
$endtime   = $sql->real_escape_string($_POST["endtime"]);
#print($starttime . "~" . $endtime . "<br>");
$query = "SELECT * FROM irclog WHERE created BETWEEN '" . $starttime . "' AND '" . $endtime . "'";
$result = $sql->query($query);
#print($result);
while($row = $result->fetch_array()) {
    echo('' . $row[5] . ' ' . '[' . $row[1] . '] ' . $row[4] . "<br>");
}

print(' <form action="/maobot/irclog.php#bottom" method="POST">');
print(' <select id="channel" name="channel" onchange="submit();">');
$query = "SELECT * FROM channel";
$result = $sql->query($query);
while($row = $result->fetch_array()) {
     print('  <option value="' . $row[1] . '">' . $row[1] . '</option>');
}

$sql->close();
?>
 <fieldset>
 <input type="datetime-local" id="starttime" name="starttime" value="<?php echo(date('Y-m-d H:i:s', time()-60*60*24)) ?>">
 <input type="datetime-local" id="endtime" name="endtime" value="<?php echo(date('Y-m-d H:i:s')) ?>">
 <input type="submit" id="submit" name="submit" value="submit">
 </form>
</body>
</html>
