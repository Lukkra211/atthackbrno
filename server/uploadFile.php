<?php
  include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/header.php';
?></head>
<body style="background-color: transparent;"><?php

$uploaddir = 'img/';
print_r($uploadfile = $uploaddir.basename($_FILES['userfile']['name']));

  echo '<pre>';/*
  if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
      echo "File is valid, and was successfully uploaded.\n";
  } else {
      echo "Possible file upload attack!\n";
  }*/

  echo 'info:';
  print_r($_FILES);
  echo "<br />";
  print_r($_FILES['userfile']['error']);
  print "</pre>";
  

  include realpath($_SERVER['DOCUMENT_ROOT']).'/htmlParts/footer.php';
  ?>