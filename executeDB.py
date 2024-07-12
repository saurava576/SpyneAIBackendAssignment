from dataStructure import *
import sqlite3
import datetime
import json

conn = sqlite3.connect('testData.db')
cursor = conn.cursor()

loggedInUser: User | None = None

def getUsersList():
    res = conn.execute(
        "SELECT name FROM USERS"
    )
    return res.fetchall()

def addUser(user: User):
    res = conn.execute(
        "INSERT INTO USERS VALUES(:mobile,:email,:name)",
        (user.mobile,user.email,user.name)
    )
    conn.commit()
    return res

def updateUser(user: User):
    res = conn.execute(
        "UPDATE USERS SET name=:name WHERE mobile=:mobile",
        (user.name, user.mobile)
    )
    conn.commit()
    return res

def deleteUser(user: User):
    res = conn.execute(
        "DELETE FROM USERS WHERE mobile=:mobile",
        (user.mobile,)
    )
    conn.commit()
    return res

def searchUsersByName(userName: str):
    res = conn.execute(
        "SELECT * FROM USERS WHERE name=:name",
        (userName,)
    )
    return res.fetchall()

def getDiscussions(usermobile: str):
    res = conn.execute(
        "SELECT * FROM DISCUSSIONS WHERE usermobile=:usermobile",
        (usermobile,)
    )
    return res.fetchall()

def addDiscussion(discussion: Discussion):
    discussion.createdon = datetime.datetime.now()
    res = conn.execute(
        "INSERT INTO DISCUSSIONS(usermobile, textfield, imagefield, hashtags, createdon) VALUES(:usermobile,:textfield,:imagefield,:hashtags,:createdon)",
        (discussion.usermobile, discussion.textfield, discussion.imagefield, discussion.hashtags, discussion.createdon)
    )
    conn.commit()
    return res

def updateDiscussion(discussion: Discussion):
    res = conn.execute(
        "UPDATE DISCUSSIONS SET textfield=:textfield,imagefield=:imagefield,hashtags=:hashtags WHERE usermobile=:usermobile",
        (discussion.textfield, discussion.imagefield, discussion.hashtags, discussion.usermobile)
    )
    conn.commit()
    return res

def deleteUserDiscussion(usermobile: str):
    res = conn.execute(
        "DELETE FROM DISCUSSIONS WHERE usermobile=:usermobile",
        (usermobile,)
    )
    conn.commit()
    return res

def searchDiscussionsByTags(tag: str):
    res = conn.execute(
        "SELECT * FROM DISCUSSIONS WHERE hashtags LIKE '%'||?||'%'",
        (tag,)
    )
    return res.fetchall()

def searchDiscussionsByText(text: str):
    res = conn.execute(
        "SELECT * FROM DISCUSSIONS WHERE textfield LIKE '%'||?||'%'",
        (text,)
    )
    return res.fetchall()

def validateAndLoginUser(user: User):
    errorMsg = "User does not exists! Please sign up!"
    res = conn.execute(
        "SELECT * FROM USERS where mobile=:mobile",
        (user.mobile,)
    )
    userslist = res.fetchall()
    if len(userslist) == 0:
        return json.dumps({"error": errorMsg}), 401
    print (len(userslist))
    for row in userslist:
        if (row[0] == user.mobile and
            row[1] == user.email and
            row[2] == user.name):
            loggedInUser = user
            return {"Login Success!"}
    return {"Login Error!!"}

def validateAndSignupUser(user: User):
    if user.mobile == None or user.email == None or user.name == None:
        return {"All fields are required!"}
    res = conn.execute(
        "SELECT * FROM USERS WHERE mobile=:mobile",
        (user.mobile,)
    )
    userslist = res.fetchall()
    if len(userslist) > 0:
        return {"User already exists! Please login to continue"}
    return addUser(user)

def followUser(thisusermobile: str, tobefollowedusermobile: str):
    if (thisusermobile != loggedInUser.mobile):
        return {"User not logged in! Please login first!"}
    res = conn.execute(
        "SELECT * FROM USERS where mobile=:mobile",
        (tobefollowedusermobile,)
    )
    userslist = res.fetchall()
    if (len(userslist) == 0):
        return {"unable to find user with mobile: " + tobefollowedusermobile}
    