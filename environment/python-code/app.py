from flask import Flask
import MySQLdb
import os

# Connect to MySQL
app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Status:</b> {hostname}<br/>"
    try:
        #MYSQL_DB_HOST MYSQL_ROOT_PASSWORD MYSQL_DATABASE MYSQL_USER
        conn = MySQLdb.connect(host=os.getenv("MYSQL_DB_HOST", "none"),    # your host, usually localhost
                     user=os.getenv("MYSQL_USER", "none"),         # your username
                     passwd=os.getenv("MYSQL_ROOT_PASSWORD", "none"),  # your password
                     db=os.getenv("MYSQL_DATABASE", "none"))        # name of the data base
    except Exception as e: #if there is an error, print it
        coon.close()
        return html.format(name="FAILED!", hostname=e)
    menssage = "connection failed"
    conn.close()
    return html.format(name=os.getenv("MYSQL_USER", "failed"), hostname="connection to mysql successful")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
