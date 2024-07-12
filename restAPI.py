from executeDB import *
from fastapi import FastAPI

description = """
These API serves the requirements of backend developer assignment for SpyneAI

## Users
You can create new users, update existing users, get a list of all users, search users based on name, delete a user

## Discussions
You can create new discussions, get all discussions, update a discussion, search discussions based on tags and text

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="BackendAssignmentSpyneAI",
    description=description,
    summary="Exposing python APIs for the assignment",
    version="0.0.1",
)

@app.get("/get-users")
async def read_users():
    return getUsersList()

@app.get("/search-user-name/")
async def search_user_by_name(userName: str):
    return searchUsersByName(userName)

@app.post("/create-user/")
async def create_user(user: User):
    return addUser(user)

@app.post("/update-user/")
async def update_user(user: User):
    return updateUser(user)

@app.delete("/delete-user/")
async def delete_user(user: User):
    return deleteUser(user)

@app.get('/get-discussions-for-user/')
async def get_discussions(usermobile: str):
    return getDiscussions(usermobile)

@app.post('/create-discussion-for-user/')
async def create_discussion_for_user(discussion: Discussion):
    return addDiscussion(discussion)

@app.post('/update-discussion-for-user/')
async def update_discussion_for_user(discussion: Discussion):
    return updateDiscussion(discussion)

@app.delete('/delete-discussion-for-user/')
async def delete_discussion_for_user(usermobile: str):
    return deleteUserDiscussion(usermobile)

@app.get('/search-discussion-by-tags/')
async def search_discussion_by_tags(tag: str):
    return searchDiscussionsByTags(tag)

@app.get('/search-discussion-by-text/')
async def search_discussion_by_texts(text: str):
    return searchDiscussionsByText(text)

@app.post('/login/')
async def validate_and_log_user(user: User):
    return validateAndLoginUser(user)

@app.post('/signup/')
async def validate_and_signup_user(user: User):
    return validateAndSignupUser(user)

@app.post('/follow-user/')
async def follow_user(thisusermobile: str, tobefollowedusermobile: str):
    return followUser(thisusermobile, tobefollowedusermobile)