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

$conn = mysqli_connect("localhost", "root", "secret", "sensor_data_station");
if (!$conn) {
    die('Could not connect: ' . mysqli_connect_error());
}

$q="select * from data_table where Sensor_NO = '#1' order by DATE desc, TIME desc limit 1;";

$result=mysqli_query($conn, $q);
$row=mysqli_fetch_array($result, MYSQLI_ASSOC);

echo "<h2 align='center'>DATE: ".$row["DATE"]."<br><br><br>";
echo "Sensor ID: ".$row["SENSOR_NO"]."<br>";
echo "Time: ".$row["TIME"]."<br>";
echo "Tempreture: ".$row["TEMPRETURE"]."&#176;C<br>";
echo " Humidity: ".$row["HUMIDITY"]."%<br><br>";

$q="select * from data_table where Sensor_NO = '#2' order by DATE desc, TIME desc limit 1;";

$result=mysqli_query($conn, $q);
$row=mysqli_fetch_array($result, MYSQLI_ASSOC);

echo "Sensor ID: ".$row["SENSOR_NO"]."<br>";
echo "Time: ".$row["TIME"]."<br>";
echo "Tempreture: ".$row["TEMPRETURE"]."&#176;C<br>";
echo " Humidity: ".$row["HUMIDITY"]."%</h2>";

mysqli_close($conn);

?>
</BODY></HTML>

