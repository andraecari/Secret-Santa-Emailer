'''
Andrae Cari
October 26 2021
'''

import random
import time
import data
import smtplib
from email.message import EmailMessage

"""
this is a test lol... im trying to figure out how to use github

"""

def randomize(numPeople):
    """
    Takes in the number of people, and generates a new list of random and unique indexes of the size of people.
    """
    # Create list
    names = []
    # Assign first receiver
    names.append(random.randint(1,numPeople-1)) 
    # Populate List
    for i in range(1,numPeople):
        while True:
            # Generate random number
            num = random.randint(0, numPeople - 1) 
            #if the generated number is not already in the list
            if num not in names:
                # If that number is not its own index(meaning the same person) and not the last index, add num to list.
                if num != i and i < numPeople - 1: 
                    names.append(num)
                    break
                # If that its the last in the list, add num to the list.
                elif i == numPeople - 1: 
                    names.append(num)
                    # If the last index rolls itself, swap value with a random index in names[].
                    if num == i: 
                        swap = random.randint(0, numPeople - 2)
                        temp = names[swap]
                        names[swap] = i
                        names[i] = temp
                    break
    return names

def showList(names, emails, addresses):
    """
    Takes in the list of names, emails, and addresses, and prints them.
    """
    # Prints header.
    print('~' * 80)
    print(f'{"Name:":20}{"Email:":30}{"Address:"}')
    print('~' * 80)
    # Prints each element in the names, emails, and addresses lists.
    for i in range(len(names)):
        print(f'{names[i]:20}{emails[i]:30}{addresses[i]}')
    print()

def send(names, emails, addresses, receivers):
    """
    Takes in the list of names, emails, addresses, and the new indexes to
    format the final sending output as for who gets who.
    """
    # Prints header.
    print('~' * 95)
    print(f'{"Secret Santa":20}{"Email of Santa":35}{"Receiver":20}{"Address of Receiver"}')
    print('~' * 95)
    i = 0
    # Properly formats and prints wanted output.
    for element in receivers:
        print(f'{names[i]:20}{emails[i]:25}{"--->":10}{names[element]:20}{addresses[element]}')
        i += 1 
    print('~' * 95)
    email(names, emails, addresses, receivers)

def email(names, emails, addresses, receivers):
    i = 0
    for element in receivers:
        msg = EmailMessage()
        msg['Subject'] = f'Secret Santa for: {names[i]}'
        msg['From'] = data.USER_EMAIL
        msg['To'] = f'{emails[i]}'
        msg.set_content(f'SECRET SANTA! {names[i]} you have gotten...')
        msg.add_alternative(f"""\

<!DOCTYPE HTML
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->
  <title></title>

  <style type="text/css">
    table,
    td {{
      color: #000000;
    }}

    a {{
      color: #0000ee;
      text-decoration: underline;
    }}

    @media (max-width: 480px) {{
      #u_content_heading_1 .v-container-padding-padding {{
        padding: 17px 10px 0px !important;
      }}

      #u_content_text_3 .v-container-padding-padding {{
        padding: 5px 10px 4px !important;
      }}

      #u_content_text_5 .v-container-padding-padding {{
        padding: 0px 10px 10px !important;
      }}

      #u_content_text_4 .v-container-padding-padding {{
        padding: 20px 10px 0px !important;
      }}
    }}

    @media only screen and (min-width: 520px) {{
      .u-row {{
        width: 500px !important;
      }}

      .u-row .u-col {{
        vertical-align: top;
      }}

      .u-row .u-col-100 {{
        width: 500px !important;
      }}

    }}

    @media (max-width: 520px) {{
      .u-row-container {{
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
      }}

      .u-row .u-col {{
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
      }}

      .u-row {{
        width: calc(100% - 40px) !important;
      }}

      .u-col {{
        width: 100% !important;
      }}

      .u-col>div {{
        margin: 0 auto;
      }}
    }}

    body {{
      margin: 0;
      padding: 0;
    }}

    table,
    tr,
    td {{
      vertical-align: top;
      border-collapse: collapse;
    }}

    p {{
      margin: 0;
    }}

    .ie-container table,
    .mso-container table {{
      table-layout: fixed;
    }}

    * {{
      line-height: inherit;
    }}

    a[x-apple-data-detectors='true'] {{
      color: inherit !important;
      text-decoration: none !important;
    }}
  </style>



  <!--[if !mso]><!-->
  <link href="https://fonts.googleapis.com/css?family=Pacifico&display=swap" rel="stylesheet" type="text/css">
  <!--<![endif]-->

</head>

<body class="clean-body u_body"
  style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #fafafa;color: #000000">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table
    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #fafafa;width:100%"
    cellpadding="0" cellspacing="0">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #fafafa;"><![endif]-->


          <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

                <!--[if (mso)|(IE)]><td align="center" width="500" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                  <div style="width: 100% !important;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div
                      style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
                      <!--<![endif]-->

                      <table id="u_content_heading_1" style="font-family:arial,helvetica,sans-serif;"
                        role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 0px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <h1
                                style="margin: 0px; color: #d33333; line-height: 130%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Brush Script MT',cursive; font-size: 33px;">
                                <strong>A&nbsp;CABO CHRISTMAS</strong>
                              </h1>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">Dear
                                    {names[i]},</span></p>
                                <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;"><span
                                      style="font-size: 14px; line-height: 19.6px;">Christmas</span> time has
                                    come.</span></p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">A
                                    time for joy and fun.</span></p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">Leave
                                    a gift and run,</span></p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">for
                                    our game of Secret Santa,</span></p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">has
                                    officially now begun.</span></p>
                                <p style="font-size: 14px; line-height: 140%; text-align: center;">&nbsp;</p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">You
                                    are the Secret Santa for:</span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_3" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:5px 10px 10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'courier new', courier; font-size: 18px; line-height: 25.2px;">{names[element].upper()}</span>
                                </p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_5" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:5px 10px 10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%; text-align: center;"><span
                                    style="font-family: 'courier new', courier; font-size: 14px; line-height: 19.6px;">{addresses[element]}</span>
                                </p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table id="u_content_text_4" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%; text-align: left;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">From,</span>
                                </p>
                                <p style="font-size: 14px; line-height: 140%; text-align: left;"><span
                                    style="font-family: 'Helvetica', sans-serif; font-size: 14px; line-height: 19.6px;">Andrae's
                                    Bot :)</span></p>
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <div align="center">
                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:arial,helvetica,sans-serif;"><tr><td style="font-family:arial,helvetica,sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.youtube.com/watch?v=owK5tHjL0aE" style="height:36px; v-text-anchor:middle; width:118px;" arcsize="11%" stroke="f" fillcolor="#169179"><w:anchorlock/><center style="color:#FFFFFF;font-family:arial,helvetica,sans-serif;"><![endif]-->
                                <a href="https://www.youtube.com/watch?v=-Khu2dXiPf8&ab_channel=JamesCharles" target="_blank"
                                  style="box-sizing: border-box;display: inline-block;font-family:arial,helvetica,sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #169179; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
                                  <span style="display:block;padding:10px 20px;line-height:120%;"><span
                                      style="font-size: 14px; line-height: 16.8px; font-family: 'Helvetica', sans-serif;">Watch
                                      this :)</span></span>
                                </a>
                                <!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                              align="left">

                              <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <tbody>
                                  <tr style="vertical-align: top">
                                    <td
                                      style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <span>&#160;</span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                  </div>
                </div>
                <!--[if (mso)|(IE)]></td><![endif]-->
                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
              </div>
            </div>
          </div>


          <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
      </tr>
    </tbody>
  </table>
  <!--[if mso]></div><![endif]-->
  <!--[if IE]></div><![endif]-->
</body>
</html>
        """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(data.USER_EMAIL, data.USER_PASS)
            smtp.send_message(msg)
        i += 1 

if __name__ == "__main__":
    # Lists to hold the 3 types of data (names, emails, and addresses).
    names = []
    emails = []
    addresses = []
    print("Welcome to Andrae's Secret Santa program:")

    while True:
        # Print empty line for spacing/readability.
        print()
        # Selects a certain mode for the program.
        if not names:
            mode = "start"
        else:
            mode = input('Please enter a mode (add, remove, show list, send, exit): ')
            
        # If start was selected, populate the lists accordingly to how many people specified.
        if mode == "start":
            # Receive input for how many people are to be added.
            num = int(input('Please enter the amount of people: '))
            # Add to each list num times.
            for i in range(num):
                names.append(input(f'Name {i + 1}: '))
                emails.append(input(f'Email {i + 1}: '))
                addresses.append(input(f'Address {i + 1}: '))
        # If add was selected, add to the lists accordingly to how many people specified.
        elif mode == "add":
            # Receive input for how many people are to be added.
            num = int(input('How many people would you like to add? '))
            # Add to each list num times.
            for i in range(num):
                names.append(input(f'Name {len(names) + 1}: '))
                emails.append(input(f'Email {len(emails) + 1}: '))
                addresses.append(input(f'Address {len(addresses) + 1}: '))
        # If remove was selected, remove index specified from all lists.
        elif mode == "remove":
            # Receive input for who would be removed.
            name = input('Who would you like to remove? ')
            # Find the index of that person.
            index = names.index(name)
            # Remove that index for all three lists.
            names.pop(index)
            emails.pop(index)
            addresses.pop(index)
            print(f'{name} has been removed.')
        # If show list was selected, call the showList() function.
        elif mode == "show list":
            showList(names, emails, addresses)
        # If send was selected, call the randomize() and send() function and print out who gets who.
        elif mode == "send":
            # New list of new indexes using randomize() function.
            receivers = randomize(len(names))
            # Prints the output using send() function.
            send(names, emails, addresses, receivers)
            break
        # If exit was selected, force exit out of the program.
        elif mode == "exit":
            break

    print("Merry Christmas! Have Fun!")
    print('~' * 26)