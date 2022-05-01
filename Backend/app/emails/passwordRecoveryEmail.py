from app.utils import sendEmailHelper

header ="""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="x-apple-disable-message-reformatting">
  <title></title>

  <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet">
  <!-- CSS Reset Start -->
  <style>
    html,
    body {
      margin: 0 auto !important;
      padding: 0 !important;
      height: 100% !important;
      width: 100% !important;
      background: #f1f1f1;
    }

    * {
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
    }

    div[style*="margin:16px 0"] {
      margin: 0 !important;
    }

    table,
    td {
      mso-table-lspace: 0pt !important;
      mso-table-rspace: 0pt !important;
    }

    table {
      border-spacing: 0 !important;
      border-collapse: collapse !important;
      table-layout: fixed !important;
      margin: 0 auto !important;
    }


  </style>
  <!-- CSS Reset End -->
  <style>
    .primary {
      background: #0d0cb5;
    }

    .bg_white {
      background: #ffffff;
    }

    .bg_light {
      background: #fafafa;
    }


    .bg_dark {
      background: rgba(0, 0, 0, .8);
    }

    .email-section {
      padding: 2.5em;
    }

    .btn {
      padding: 5px 15px;
      display: inline-block;
    }

    .btn.btn-primary {
      border-radius: 5px;
      background: #0d0cb5;
      color: #ffffff;
    }

    .btn.btn-white {
      border-radius: 5px;
      background: #ffffff;
      color: #000000;
    }

    .btn.btn-white-outline {
      border-radius: 5px;
      background: transparent;
      border: 1px solid #000000;;
      color: #000000;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-family: 'Poppins', sans-serif;
      color: #000000;
      margin-top: 0;
    }

    body {
      font-family: 'Poppins', sans-serif;
      font-weight: 400;
      font-size: 15px;
      line-height: 1.8;
      color: rgba(0, 0, 0, .4);
    }

    a {
      color: #0d0cb5;
    }

    /* Logo */
    .logo h1 {
      margin: 0;
    }

    .logo h1 a {
      color: #000000;
      font-size: 20px;
      font-weight: 700;
      text-transform: uppercase;
      font-family: "Poppins", sans-serif;
    }

    .navigation {
      padding: 0;
    }

    .navigation li {
      list-style: none;
      display: inline-block;
      margin-left: 5px;
      font-size: 13px;
      font-weight: 500;
    }

    .navigation li a {
      color: rgba(0, 0, 0, 0.4);
    }

    /*HERO*/
    .hero {
      position: relative;
      z-index: 0;
    }

    .hero .overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      content: "";
      width: 100%;
      background: #000000;
      z-index: -1;
      opacity: 0.3;
    }

    .hero .icon a {
      display: block;
      width: 60px;
      margin: 0 auto;
    }

    .hero .text {
      color: rgba(255, 255, 255, 0.8);
    }

    .hero .text h2 {
      color: #ffffff;
      font-size: 30px;
      margin-bottom: 0;
    }

    /*HEADING SECTION*/

    .heading-section h2 {
      color: #000000;
      font-size: 20px;
      margin-top: 0;
      line-height: 1.4;
      font-weight: 700;
      text-transform: uppercase;
    }

    .heading-section .subheading {
      display: inline-block;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: rgba(0, 0, 0, 0.4);
      position: relative;
    }

    .heading-section .subheading::after {
      position: absolute;
      left: 0;
      right: 0;
      bottom: -10px;
      content: "";
      width: 100%;
      height: 0px;
      background: #0d0cb5;
      margin: 0 auto;
    }

    .heading-section-white {
      color: rgba(255, 255, 255, 0.8);
    }

    .heading-section-white h2 {
      line-height: 1;
      padding-bottom: 0;
    }

    .heading-section-white h2 {
      color: #ffffff;
    }

    .heading-section-white .subheading {
      margin-bottom: 0;
      display: inline-block;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: rgba(255, 255, 255, 0.4);
    }

    .icon {
      text-align: center;
    }
  </style>
</head>

<body width="100%" style="margin: 0;padding: 0 !important;mso-line-height-rule:exactly; background-color: #222222;">
  <center style="width: 100%;background-color: #f1f1f1;">
    <div>
      &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
      &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
      &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
      &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
    </div>

    <div style="max-width: 800px;margin: 0 auto;" class="email-container">
      <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
        style="margin: auto;">

        <tr>
          <td valign="top" class="bg_white" style="padding: 1em 2.5em;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
              <tr>
                <td width="40%" class="logo" style="text-align: left;">
                  <h1><a href="#">LAUNCHAPP</a></h1>
                </td>
              </tr>
            </table>
          </td>
        </tr>"""
        
        
body = """\  <tr>
          <td valign="middle" class="hero bg_dark"
            style="background-image: url(img/bg_1.jpg); background-size: cover;height: 300px;">
            <div class="overlay"></div>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
              <tr>
                <td>
                  <div class="text" style="padding: 0 3em; text-align: center;">
                    <h3>LaunchApp Password Recovery</h3>
                     <p  style="padding: 0 3em;text-align: left;"> Hi {},</p>
                     <p style="padding: 0 3em;text-align: left;">
                     Thank you for using LaunchApp. Click on the link below to reset your password. 
                      <p><a href="{}" class="btn btn-white-outline">Reset Password</a></p>
                    </p>
                  </div>
                  <div class="icon">
                    <a href="#">
                      <img src="img/002-play-button.png" alt=""
                        style="width: 60px;max-width: 600px;height: auto;margin: auto;display: block;">
                    </a>
                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr> """
        
        
footer = """ <tr>
                <td valign="top" class="bg_white" style="padding: 1em 2.5em;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td width="40%" class="logo" style="text-align: center;">
                        <h2>Always Ready to Serve Your Launch</h2>
                        <p><a href="#" class="btn btn-white-outline">Get Started</a></p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
        </tr>
        
      
      </table>
    </div>
  </center>

</body>

</html>"""

def getEmailMessage(userName: str,  link: str):
    return ''.join([ header, body.format(userName, link), footer])

def passwordRevovery(userEmail:str, userName: str, link: str):
    subject:str ="LaunchApp Password Recovery"
    message = getEmailMessage(userName, link)
    sendEmailHelper.sendMail(userEmail, message, subject)