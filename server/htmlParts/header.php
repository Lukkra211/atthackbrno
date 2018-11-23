 <?php
$themeColor = "#01e1e1";
?>
<!doctype html>
<html>
 <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Chrome, Firefox OS and Opera -->
    <meta name="theme-color" content="<?php print($themeColor); ?> ">
    <!-- Windows Phone -->
    <meta name="msapplication-navbutton-color" content="<?php print($themeColor); ?> ">
    <!-- iOS Safari -->
    <meta name="apple-mobile-web-app-status-bar-style" content="<?php print($themeColor); ?> ">

    <!-- load STYLES -->
    <link href="/images/favicon.ico" rel="shortcut icon" type="image/x-icon">
    <link href="/styles/style.css"   rel="stylesheet"    type="text/css" />
    <link href="/styles/mui.css"     rel="stylesheet"    type="text/css" />
    <script src="/styles/mui.min.js"></script>
    <!-- SHARING -->
    <meta property="og:url" content=<?php echo '"'.$_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'].'"'; ?>/>
    
