
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
  <title>Traffic AI</title>
  
</head>
<body style="background-color: transparent;">
    <div class="dashboardContent" >
        <center>
            <div style="background-color: rgba(255, 255, 255, 0.75);" class="mui-panel">
                <h1>Traffic AI</h1>
                <h2>Welcome</h2>
                <form enctype="multipart/form-data" action="uploadFile.php" method="POST">
                    <input type="hidden" name="MAX_FILE_SIZE" value="300000" />
                    <b>Choose File:</b> <input style='cursor: pointer; ' name="userfile" type="file" required />
                    <br>
                    <input type="submit" value="Send File" id="submitButton" onclick="change()" class="mui-btn mui-btn--primary mui-btn--raised"/>
                </form>
            </div>
        </center>
    </div>
<?php include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/footer.php';?>