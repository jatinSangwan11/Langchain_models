from typing import Optional
from pydantic import BaseModel

class Check(BaseModel):

    name: str = "Jatin"  # giving default value
    age: Optional[int] = None           # here the default value is passed here that is None and also this field is optional with datatype "int"

new_student = {
    "name": "Jatin",
   # "age": "24"   Pydantic performs type coercion (automatic conversion) by default.
}

student = Check(**new_student)

print(type(Check))
print(student)