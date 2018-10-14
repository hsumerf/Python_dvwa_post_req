str1 = b"script&gt;alert(\'Hi umer\')"
str2 = b"Hello &lt;script&gt;alert(\'Hi umer\')&lt;/script&gt;"
print(type(str2.decode('utf-8')))
print(str2.decode('utf-8'))
str3 = """b'\r\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
\r\n\r\n
<html xmlns="http://www.w3.org/1999/xhtml">
 \r\n\r\n\t
 <head>
  \r\n\t\t
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  \r\n\r\n\t\t
  <title>
   Damn Vulnerable Web App (DVWA) v1.0.7 :: Vulnerability: Reflected Cross Site Scripting (XSS)
  </title>
  \r\n\r\n\t\t
  <link href="../../dvwa/css/main.css" rel="stylesheet" type="text/css"/>
  \r\n\r\n\t\t
  <link href="../../favicon.ico" rel="icon" type="\\image/ico"/>
  \r\n\r\n\t\t
  <script src="../../dvwa/js/dvwaPage.js" type="text/javascript">
  </script>
  \r\n\r\n\t
 </head>
 \r\n\r\n\t
 <body class="home">
  \r\n\t\t
  <div id="container">
   \r\n\r\n\t\t\t
   <div id="header">
    \r\n\r\n\t\t\t\t
    <img alt="Damn Vulnerable Web App" src="../../dvwa/images/logo.png"/>
    \r\n\r\n\t\t\t
   </div>
   \r\n\r\n\t\t\t
   <div id="main_menu">
    \r\n\r\n\t\t\t\t
    <div id="main_menu_padded">
     \r\n\t\t\t\t
     <ul>
      <li class="" onclick="window.location=\'../../.\'">
       <a href="../../.">
        Home
       </a>
      </li>
      <li class="" onclick="window.location=\'../../instructions.php\'">
       <a href="../../instructions.php">
        Instructions
       </a>
      </li>
      <li class="" onclick="window.location=\'../../setup.php\'">
       <a href="../../setup.php">
        Setup
       </a>
      </li>
     </ul>
     <ul>
      <li class="" onclick="window.location=\'../../vulnerabilities/brute/.\'">
       <a href="../../vulnerabilities/brute/.">
        Brute Force
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/exec/.\'">
       <a href="../../vulnerabilities/exec/.">
        Command Execution
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/csrf/.\'">
       <a href="../../vulnerabilities/csrf/.">
        CSRF
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/fi/.?page=include.php\'">
       <a href="../../vulnerabilities/fi/.?page=include.php">
        File Inclusion
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/sqli/.\'">
       <a href="../../vulnerabilities/sqli/.">
        SQL Injection
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/sqli_blind/.\'">
       <a href="../../vulnerabilities/sqli_blind/.">
        SQL Injection (Blind)
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/upload/.\'">
       <a href="../../vulnerabilities/upload/.">
        Upload
       </a>
      </li>
      <li class="selected" onclick="window.location=\'../../vulnerabilities/xss_r/.\'">
       <a href="../../vulnerabilities/xss_r/.">
        XSS reflected
       </a>
      </li>
      <li class="" onclick="window.location=\'../../vulnerabilities/xss_s/.\'">
       <a href="../../vulnerabilities/xss_s/.">
        XSS stored
       </a>
      </li>
     </ul>
     <ul>
      <li class="" onclick="window.location=\'../../security.php\'">
       <a href="../../security.php">
        DVWA Security
       </a>
      </li>
      <li class="" onclick="window.location=\'../../phpinfo.php\'">
       <a href="../../phpinfo.php">
        PHP Info
       </a>
      </li>
      <li class="" onclick="window.location=\'../../about.php\'">
       <a href="../../about.php">
        About
       </a>
      </li>
     </ul>
     <ul>
      <li class="" onclick="window.location=\'../../logout.php\'">
       <a href="../../logout.php">
        Logout
       </a>
      </li>
     </ul>
     \r\n\t\t\t\t
    </div>
    \r\n\r\n\t\t\t
   </div>
   \r\n\r\n\t\t\t
   <div id="main_body">
    \r\n\r\n\t\t\t\t\r\n
    <div class="body_padded">
     \r\n\t
     <h1>
      Vulnerability: Reflected Cross Site Scripting (XSS)
     </h1>
     \r\n\r\n\t
     <div class="vulnerable_code_area">
      \r\n\r\n\t\t
      <form action="#" method="GET" name="XSS">
       \r\n\t\t\t
       <p>
        What\'s your name?
       </p>
       \r\n\t\t\t
       <input name="name" type="text"/>
       \r\n\t\t\t
       <input type="submit" value="Submit"/>
       \r\n\t\t
      </form>
      \r\n\r\n\t\t
      <pre>Hello &lt;script&gt;alert(\'Hi umer\')&lt;/script&gt;</pre>
      \r\n\r\n\t
     </div>
     \r\n\r\n\t
     <h2>
      More info
     </h2>
     \r\n\r\n\t
     <ul>
      \r\n\t\t
      <li>
       <a href="http://hiderefer.com/?http://ha.ckers.org/xss.html" target="_blank">
        http://ha.ckers.org/xss.html
       </a>
      </li>
      \r\n\t\t
      <li>
       <a href="http://hiderefer.com/?http://en.wikipedia.org/wiki/Cross-site_scripting" target="_blank">
        http://en.wikipedia.org/wiki/Cross-site_scripting
       </a>
      </li>
      \r\n\t\t
      <li>
       <a href="http://hiderefer.com/?http://www.cgisecurity.com/xss-faq.html" target="_blank">
        http://www.cgisecurity.com/xss-faq.html
       </a>
      </li>
      \r\n\t
     </ul>
     \r\n
    </div>
    \r\n\r\n\t\t\t\t
    <br/>
    \r\n\t\t\t\t
    <br/>
    \r\n\t\t\t\t\r\n\r\n\t\t\t
   </div>
   \r\n\r\n\t\t\t
   <div class="clear">
    \r\n\t\t\t
   </div>
   \r\n\r\n\t\t\t
   <div id="system_info">
    \r\n\t\t\t\t
    <input class="popup_button" onclick="javascript:popUp( \'../../vulnerabilities/view_help.php?id=xss_r&amp;security=high\' )" type="button" value="View Help"/>
    <input class="popup_button" onclick="javascript:popUp( \'../../vulnerabilities/view_source.php?id=xss_r&amp;security=high\' )" type="button" value="View Source"/>
    <div align="left">
     <b>
      Username:
     </b>
     admin
     <br/>
     <b>
      Security Level:
     </b>
     high
     <br/>
     <b>
      PHPIDS:
     </b>
     disabled
    </div>
    \r\n\t\t\t
   </div>
   \r\n\r\n\t\t\t
   <div id="footer">
    \r\n\r\n\t\t\t\t
    <p>
     Damn Vulnerable Web Application (DVWA) v1.0.7
    </p>
    \r\n\r\n\t\t\t
   </div>
   \r\n\r\n\t\t
  </div>
  \r\n\r\n\t
 </body>
 \r\n\r\n
</html>
'
"""
# print(str2)
if str1 in str2:
    print("yes true")
else:
    print("false")
