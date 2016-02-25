<?php
session_start();
session_regenerate_id(true);

$default  = parse_ini_file("sql.ini", true)["DEFAULT"];
$sql_user   = $default["user"];
$sql_server = $default["server"];
$sql_pass   = $default["passwd"];
$sql_db     = $default["db"];

#print_r($sql_user);
#print_r($sql_server);
#print_r($sql_db);

$errMes = "";
if(isset($_POST["login"])) {
    if(empty($_POST["userid"])) {
        $errMes = "ID not filled.";
    } else if(empty($_POST["password"])) {
        $errMes = "Password not fiiled.";
    } else {
        $sql = new mysqli($sql_server, 
            $sql_user, $sql_pass);
        if($sql->connect_error) {
            print("<p>DB failed." . $sql->connect_error);
            exit();
        }

        $sql->select_db($sql_db);
        $userid = $sql->real_escape_string($_POST["userid"]);
        $query = "SELECT * FROM user WHERE username = '" . $userid . "'";
        $result = $sql->query($query);
        if(!$result) {
            print('query failed.' . $sql->error);
            $sql->close();
            exit();
        }
        while ($row = $result->fetch_assoc()) {
            $hashed_pwd = $row['password'];
        }
        $sql->close();

        if(password_verify($_POST["password"], $hashed_pwd)) {
            session_regenerate_id(true);
            $_SESSION["USERID"] = $_POST["userid"];
            header("Location: main.html");
            exit;
        }
        else {
            $errMes = "Wrong ID or password.";
        }
    }
}
#print_r($_SESSION);
?>

<!doctype html>
<html>
 <head>
  <meta charset="UTF-8">
  <title>IRCLOG login</title>
 </head>
 <body>
 <form id="loginFrom" name="loginForm" action="" method="POST">
 <fieldset>
 <legend>login form</legend>
 <div><?php echo $errMes ?></div>
 <label for="userid">userid</label><input type="text" id="userid" name="userid" value="s">
 <br>
 <label for="password">password</label><input type="password" id="password" name="password" value="">
 <br>
 <input type="submit" id="login" name="login" value="login">
 </fieldset>
 </form>
 </body>
</html>
