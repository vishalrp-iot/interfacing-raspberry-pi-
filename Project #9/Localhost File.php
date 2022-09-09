<HTML>
<HEAD><TITLE>SENSOR DATA</TITLE>
<META http-equiv="refresh" content="10" charset='utf-8'>
<style type='text/css'>
body{
	background-color: green;
	color: white;
}
</style>
</HEAD>
<BODY>
<h1 align='center'>LIVE TEMPRETURE/HUMIDITY STATION</h1>
<?php

echo $username;

$conn = mysqli_connect("localhost", "root", "qwerty", "temp_data");
if (!$conn) {
    die('Could not connect: ' . mysqli_connect_error());
}

$q="SELECT tempreture, humidity FROM tempData";
$result=mysqli_query($conn, $q);
$num_rows = mysqli_num_rows($result);

while($num_rows > 1){
	$num_rows = $num_rows-1;
	$row = mysqli_fetch_assoc($result);
}

echo "<h2 align='center'>Tempreture: ".$row["tempreture"]."&#176;C<br>";
echo " Humidity: ".$row["humidity"]."%</h2>";

mysqli_close($conn);

?>
</BODY></HTML>
