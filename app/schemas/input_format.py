from pydantic import BaseModel, Field 


class InputValue(BaseModel):
    val_1 :float = Field(default=1)
    val_2 :float= Field(default=1)

class ResultResponse(BaseModel):
    message:str|None = Field(default='This is the answer of your given operation')
    result:float