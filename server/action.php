<?php
  include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/header.php';
?><title>Traffic AI</title>
<script type="text/javascript">
  function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
  function move() {
    var elem = document.getElementById("myBar"); 
    var width = <?php echo (int)(1080/$_POST["numberOfInteraction"]); ?>;
    var id = setInterval(frame, width);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++; 
            elem.style.width = width + '%'; 
            elem.innerHTML = width * 1 + '%';
            sleep(100);
        }
    }
  }
</script></head>
<body style="background-color: transparent;" onload='move()'>
    <div class="dashboardContent" >
        <center>
            <div style="background-color: rgba(255, 255, 255, 0.75);" class="mui-panel">
                <h1>Traffic AI</h1>
                <h2>Welcome</h2>

                <table style='width: 100%; '>
                  <tr>
                    <td><h3>Running Job:</h3></td>
                    <td><?php echo $_POST["nameOfTheJob"]; ?></td>
                  </tr>
                  <tr>
                    <td><h4>Completed:</h4></td>
                    <td> 1080 / <?php echo $_POST["numberOfInteraction"]." => ".(1080/(int)$_POST["numberOfInteraction"]);?>%</td>
                  </tr>
                  <tr style='width: 100%; '>
                    <td><h4>Progress: </h4></td>
                    <td>
                      <div id="myProgress" onload='move()'>
                        <div id="myBar"><?php echo (int)(1080/$_POST["numberOfInteraction"]); ?>%</div>
                      </div>
                    </td>
                  </tr>
                  <tr style='width: 100%; '>
                    <td><h4>Population: </h4></td>
                    <td>200</td>
                  </tr>
                </table>

<?php /*
  echo (isset($_POST["text1"]).", ".isset($_POST["text2"]).", ".isset($_POST["i"]).", ".isset($_POST["userfile"x]));
  if (isset($_POST["text1"]) and isset($_POST["text2"]) and isset($_POST["i"]) and isset($_POST["userfile"])) {
    $uploaddir = realpath($_SERVER['DOCUMENT_ROOT']).'/uploaded/';
    print_r($uploadfile = $uploaddir.basename($_FILES['userfile']['name']));

    echo '<pre>';
    if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
        echo "File is valid, and was successfully uploaded.\n";
    } else {
        echo "Possible file upload attack!\n";
    }

    echo 'info:';
    print_r($_FILES);
    echo "<br />";
    print_r($_FILES['userfile']['error']);
    print "</pre>";
    

    include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/footer.php';
  }else{
    echo "Something is wrong!";
  }*/
    ?>
            </div>
          </div>
        </center>
      </div>
  }
  <?php include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/footer.php';?>