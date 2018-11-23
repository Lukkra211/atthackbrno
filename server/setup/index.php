
    <?php include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/header.php'; ?>
      <script type="text/javascript">
    function change(){
      // když je nějaký povinný vstup prázdný, nechat tlačítko  znovu zmáčknutelné
      // resp. nic nedělat, ale při odesílání formuláře napsat 'Odesílání...' a azakázat znovu zmáčknutí
      // nejlépe místo tlačítka dát 'GIF odesílání, čekejte prosím'
      //    alert(document.getElementsByTagName("input")[0].value);
      var i;
      var coutMissInputs=0;
      for (i = 0; i <= document.getElementsByTagName("input").length-1; i++) { 
        if (document.getElementsByTagName("input")[i].required && document.getElementsByTagName("input")[i].value == "") {
          coutMissInputs++;
        }
      }
      if (coutMissInputs<=0) {
        document.getElementById("thisWillChangeToLoader").innerHTML = "<div align='center'><table style='background-color: transparent; ' align='center' valign='top' ><tr style='background-color: transparent; '><td style='background-color: transparent; ' align='left'> <div class='loader' id='loader'></div><br></td><td valign='bottom' align='center' style='background-color: transparent; '><p style='text-align: right; '><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Odesílání, čekejte prosím ...</p></td></tr></table></div>";
        //document.getElementById("thisWillChangeToLoader").innerHTML = "<div class='loader' id='loader'></div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Odesílám ...</p>";
        hideButton();
      }
  }
  function hideButton() {
    var x = document.getElementById("submitButton");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
  </script>
  <title>Setup page - Quiz</title>
    <meta property="og:title" content="Setup page - Quiz" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="https://quiz.buchticka.eu/images/background.jpg" />
    <meta property="og:description" content="Here you can make Quiz working!" />
  
</head>
<body style="background-color: transparent;">
    <div class="dashboardContent" >
        <center>
            <div style="background-color: rgba(255, 255, 255, 0.75);" class="mui-panel">
                <h1>Welcome</h1>
                <h2>Setup of Quiz</h2>
                <?php
                    if (isset($_GET["servername"]) and isset($_GET["username"]) and isset($_GET["password"]) and isset($_GET["dbname"])) {
                        $newFileName = realpath($_SERVER['DOCUMENT_ROOT'])."/controlDatabase/dbConnect.php";
                        $newFileContent = "
                        <?php
                            // Here we must enter variables for connection to database
                            \$servername = \"".$_GET["servername"]."\";
                            \$username = \"".$_GET["username"]."\";
                            \$password = \"".$_GET["password"]."\";
                            \$dbname = \"".$_GET["dbname"]."\";

                            \$conn = new mysqli(\$servername, \$username, \$password, \$dbname); 
                            if(\$conn->connect_error){
                                die(\$conn->connect_error); }
                            \$conn -> set_charset(\"UTF8\") or die(\"<h1 style='background-color: pink; color: red;'>BAD CODING!</h1>\");
                        ?>";

                        if (file_put_contents($newFileName, $newFileContent) !== false) {
                            echo "File created (" . basename($newFileName) . ")";
                        } else {
                            echo "Cannot create file (" . basename($newFileName) . ")";
                        }
                    
                        // Try to create database
                        try{
                            // Create connection to database server without setting database
                            $conn = new mysqli($_GET["servername"], $_GET["username"], $_GET["password"]); 
                            // Check connection
                            if($conn->connect_error){
                                die($conn->connect_error);
                            }
                            // Check encoding
                            $conn -> set_charset("UTF8") or die("Bad coding!");
                            // Create database
                            $sql = "CREATE DATABASE IF NOT EXISTS ".$_GET["dbname"].";";
                            if ($conn->query($sql) === TRUE) {
                                echo "<h3>Database created successfully</h3>";
                                //$conn->close(); // disconnect
                            } else {
                                echo "<h2 style='color: red; '>Error creating database: " . $conn->error . "</h2>";
                            }

                            // Create connection to database server and database
                            $conn = new mysqli($_GET["servername"], $_GET["username"], $_GET["password"], $_GET["dbname"]); 
                            if($conn->connect_error){
                                die($conn->connect_error); }
                            $conn -> set_charset("UTF8") or die("Spatne kodovani!");

                            echo "  <div style='background-color: rgba(240, 255, 220, 0.75); '>
                                        <h3 style='color: limegreen; '>Successfully connected to database!</h3>
                                        <p  style='color: limegreen; '>Database named `".$_GET["dbname"]."` is already existing.</p>
                                    </div>";
                        }catch (Exception $e){
                            echo "<h2 style='color: red; '>Eroor : ".$e."</h2>";
                        }
                        // Try to create table with attributors
                        try{
                            // Name of the file
                            $filename = 'quiz.sql';
                            // Temporary variable, used to store current query
                            $templine = '';
                            // Read in entire file
                            $lines = file($filename);
                            // Loop through each line
                            foreach ($lines as $line){
                                // Skip it if it's a comment
                                if (substr($line, 0, 2) == '--' || $line == '')
                                    continue;

                                // Add this line to the current segment
                                $templine .= $line;
                                // If it has a semicolon at the end, it's the end of the query
                                if (substr(trim($line), -1, 1) == ';'){
                                    // Perform the query
                                    //mysql_query($templine) or print('Error performing query \'<strong>' . $templine . '\': ' . mysql_error() . '<br /><br /></strong>');
                                    $conn->query($templine) or print("<div style='background-color: rgba(255, 220, 220, 0.75); '> Error performing query '<strong style='color: red; '>" . $templine . "': " . $conn->error . "<br /><br /></strong></div>");
                                    // Reset temp variable to empty
                                    $templine = '';
                                }
                            }
                             echo " <div style='background-color: rgba(240, 255, 220, 0.75); '>
                                        <h3 style='color: limegreen; '>Tables imported successfully to database named `".$_GET["dbname"]."`.</h3>
                                    </div>";
                        }catch (Exception $e){
                            echo "<h2 style='color: red; background-color: rgba(255, 220, 220, 0.75); '>Pozor: ".$e."</h2>";
                        }
                        $conn->close();
                    }else{
                        ?>
                        <form action="index.php" method="GET">
                            <div class="mui-textfield  mui-textfield--float-label">
                              <input type="text" name="servername" id="servername" required value="localhost">
                              <label style="text-align: left; ">Servername <b style="color: red; ">*</b></label>
                            </div>
                            <div class="mui-textfield  mui-textfield--float-label">
                              <input type="text" name="username" id="username" required value="root">
                              <label style="text-align: left; ">User name <b style="color: red; ">*</b></label>
                            </div>
                            <div class="mui-textfield mui-textfield--float-label">
                              <input type="password" name="password" id="password" >
                              <label style="text-align: left; ">Password </label>
                            </div>
                            <div class="mui-textfield mui-textfield--float-label">
                              <input type="text" name="dbname" id="dbname" required value="quiz">
                              <label style="text-align: left; ">DB name <b style="color: red; ">*</b></label>
                            </div>
                            <div style="text-align: center; " align="center">
                              <div id="thisWillChangeToLoader"></div>
                              <input type="submit" id="submitButton" onclick="change()" class="mui-btn mui-btn--primary mui-btn--raised" value="Odeslat">
                            </div>

                        </form>
                    <?php }
                    ?>
            </div>
        </center>
    </div>
<?php include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/footer.php';?>