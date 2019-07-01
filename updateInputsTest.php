
<?php
    echo "connecting...";
    $mysqli = mysqli_connect('localhost', 'root', '1blownFuse', 'sensors');
    echo "updating ";
    echo "...";
    

    if ($mysqli == false) {
        echo "Sorry, this website is experiencing problems.";
        echo "Error: Failed to make a MySQL connection";
        exit;
    }

 $name = $_POST["name"];

    // Perform an SQL query
    $sql = 'UPDATE inputs SET value=!value WHERE name=\'' . $name .'\'';
    
    $result = mysqli_query($mysqli, $sql);
    
    echo $result;
    
    mysqli_close($mysqli);
?>
