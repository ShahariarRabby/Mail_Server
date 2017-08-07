# Mail Server
# This can send and receive mail from Gmail server.

### All code is well described. Please see the `ipynb` file for more details. Also read the comment.
### If you want to understand the code see the ipynb file. `.py` files are for running purpose.

## You may only need to install *playsound* library `pip install playsound` 
#### library need to install:


if you face any problem please follow this process to install the library


<ol>
<li> 
smtplib

**For install smtp lib run** `pip install smtplib`
</li>

<li> 
email

**For install email run**`pip install email`
</li>

<li> 
getpass

**For install getpass run**`pip install getpass`
</li>

<li> 
imaplib

**For install imaplib run**`pip install imaplib`
</li>


<li> 

**playsound**

**For install playsound run** `pip install playsound`
</li>

<li> 
threading

**For install threading run**`pip install threading`
</li>
<li> 
ctypes

**For install ctypes run**`pip install ctypes`
</li>
</ol>

# Files
<ol>
<li> **Sendmail.py** is the main file for sending mail. All send function is under that file</li>
<li> **Sendy.py** can send mail. It is depandent on  **Sendmail.py**</li>
<li> **ReceiveMail.py** is the main file for reciving mail. All reciving function is under that file</li>
<li> **CheckMail.py** is check a number of file from server. It is depandent on  **ReceiveMail.py**</li>
<li> **Server.py** send connection request to server on every 15 sec and notify user if there is new email. It is depandent on  **ReceiveMail.py** </li>
</ol>
# Bugs
**In `py` file `getpass.getpass()` function is not working on my terminal. So I remove them from `py` file.
It will work well in `.ipynb` file. Try your terminal that it works your pc or not.**

# License
**MIT License**

**Copyright (c) 2017 Shahariar Rabby**

***Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:***

***The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.***

***THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.***



# Thank You
