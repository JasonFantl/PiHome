

<?php
echo "connecting...";

$mysqli = new mysqli('localhost', 'root', '1blownFuse', 'sensors');

echo "fetching... ";


// Oh no! A connect_errno exists so the connection attempt failed!
if ($mysqli->connect_errno) {
    // The connection failed. What do you want to do? 
    // You could contact yourself (email?), log the error, show a nice page, etc.
    // You do not want to reveal sensitive information

    // Let's try this:
    echo "Sorry, this website is experiencing problems.";

    // Something you should not do on a public site, but this example will show you
    // anyways, is print out MySQL error related information -- you might log this
    echo "Error: Failed to make a MySQL connection, here is why: \n";
    echo "Errno: " . $mysqli->connect_errno . "\n";
    echo "Error: " . $mysqli->connect_error . "\n";
    
    // You might want to show them something nice, but we will simply exit
    exit;
}


// Perform an SQL query
   $sql = 'SELECT name, value, sensor, read_only FROM inputs';
if (!$result = $mysqli->query($sql)) {
    // Oh no! The query failed. 
    echo "Sorry, the website is experiencing problems.";

    // Again, do not do this on a public site, but we'll show you how
    // to get the error information
    echo "Error: Our query failed to execute and here is why: \n";
    echo "Query: " . $sql . "\n";
    echo "Errno: " . $mysqli->errno . "\n";
    echo "Error: " . $mysqli->error . "\n";
    exit;
}

if ($result->num_rows > 0) {
   echo "<table id=\"inputState\">
 <tr>
  <th>name</th> 
  <th>value</th>
  <th>type</th>
  <th>read only</th>
 </tr>";
   // output data of each row
   while($row = $result->fetch_assoc()) {
      echo "<tr><td>" . $row["name"] . "</td><td>". $row["value"]. "</td><td>". $row["sensor"]. "</td><td>". $row["read_only"]. "</td></tr>";
   }
   echo "</table>";
} else { echo "0 results"; }


// The script will automatically free the result and close the MySQL
// connection when it exits, but let's just do it anyways
$result->free();
$mysqli->close();

?>
