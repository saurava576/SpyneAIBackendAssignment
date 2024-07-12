from pydantic import BaseModel

class User(BaseModel):
    mobile: str
    email: str | None = None
    name: str | None = None
    
    # def __conform__(self, protocol):
    #     if protocol is sqlite3.PrepareProtocol:
    #         return f"{self.mobile};{self.email};{self.name}"

class Discussion(BaseModel):
    usermobile: str
    textfield: str
    imagefield: str | None = None
    hashtags: str | None = None
    createdon: str | None = None