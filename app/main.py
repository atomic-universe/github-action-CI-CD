from fastapi import FastAPI
from app.schemas.input_format import InputValue,ResultResponse


app = FastAPI(title="GitHub action workflow",version="0.0.1")

@app.get('/')
def home():
    return {
        'message':'Welcome to my calculator application',
        'version':app.version,
        'title':app.title
    }

@app.post('/add',response_model=ResultResponse,tags=['basic arithmatic operations'])
def add_values(inp:InputValue):
    ans = inp.val_1+inp.val_2
    return ResultResponse(result=ans)

@app.post('/sub',response_model=ResultResponse,tags=['basic arithmatic operations'])
def add_values(inp:InputValue):
    ans = inp.val_1-inp.val_2
    return ResultResponse(result=ans)

@app.post('/mult',response_model=ResultResponse,tags=['basic arithmatic operations'])
def add_values(inp:InputValue):
    ans = inp.val_1 * inp.val_2
    return ResultResponse(result=ans)

@app.post('/div',response_model=ResultResponse,tags=['basic arithmatic operations'])
def add_values(inp:InputValue):
    ans = inp.val_1 / inp.val_2
    return ResultResponse(result=ans)

@app.post('/pow',response_model=ResultResponse,tags=['basic arithmatic operations'])
def add_values(inp:InputValue):
    ans = inp.val_1 ** inp.val_2
    return ResultResponse(result=ans)


