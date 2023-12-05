import mysql.connector

dataBase = mysql.connector.connect(
    host = 'viaduct.proxy.rlwy.net',
    user = 'root',
    password = 'Gh-46F3aeEB245eE55e1bBb-Hg5-A5dh',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE railway')

print('ALL DONE!')