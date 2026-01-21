from pydantic import BaseModel

class User(BaseModel):
    id:int
    name: str
    is_activate: bool

input_data={'id':101, #'101' dile pydantic eitake convert korar try korbe int error dibe '101a' dile error dibe
            'name':'Zarin Saima',
            'is_activate':True}

user =User(**input_data) #** to unpack the dict--> now the dictionary will not be treated as one obj but all the inside object will scrttered around. 
print(user)