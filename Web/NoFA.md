The challenge gives us a website's source code and a `user.db` file to extract all users.\
By using `sqlite3` we can get information of `admin` user.
```
sqlite> .tables
users
sqlite> SELECT * FROM users;
--------------
5|admin|iamadmin@nfs.com|c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67|1
--------------
```
I am not good at Cryptography field (maybe I will learn more about it in the future) so I use `hash-identifier` tool to get the plaintext, which is `apple@123`.\
After log in successfully, the website requires us to input the OTP code to get the flag. So when I read the source code, I see that the OTP has already stored in cookie session before we log in.
```
---------------
if user and hashlib.sha256(password.encode()).hexdigest() == user['password']:
            if user['two_fa']:
                # Generate OTP
                otp = str(random.randint(1000, 9999))
                session['otp_secret'] = otp
                session['otp_timestamp'] = time.time()
                session['username'] = username
                session['logged'] = 'false'
                # send OTP to mail ---
                return redirect(url_for('two_fa'))
---------------
---------------
otp = request.form['otp']
stored_otp = session['otp_secret']
timestamp = session.get('otp_timestamp')
if stored_otp and otp == stored_otp and (time.time() - timestamp) < 120:
    session['logged'] = 'true'
    flash('Login successful!', 'green')
    return redirect(url_for('home'))
else:
    flash('Invalid OTP or OTP expired', 'red')
    return render_template('2fa.html')
---------------
```
So I use the [Flask session cookie decoder](https://www.kirsle.net/wizards/flask-session.cgi) and get the OTP.
```
{
    "logged": "false",
    "otp_secret": "5027",
    "otp_timestamp": 1792722888.2119823,
    "username": "admin"
}
```
Input this OTP and get the flag.

I tried another way to solve this challenge is that you just need to get the [Flask session cookie decoder/encoder](https://github.com/noraj/flask-session-cookie-manager), encode this JSON, change the session cookie uing `BurpSuite`. However, this way didn't work....
```
{
    "logged": "true",
    "username": "admin"
}
```