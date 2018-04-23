# AutoTest_LoginByCookie
This module is designed for logging in web site with cookies to reduce other useless operations,   
such as inputting identifying code when perform automatic test for web app.  

It consists of two parts mainly including login_by_id.py and login_by_cookie.py.  
Firstly get cookies logging successfully by running login_by_id.py and store cookies in cookie_after.yaml.  
Then load cookies from cookie_after.yaml by running login_by_cookie.py to log in the web site.
