from fastapi import FastAPI
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"



headers = {
	"X-RapidAPI-Key": "148bc7ae7emsh9ce2312cdf4c7e7p188d53jsn20da7f80baeb",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}




app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getrecipe/{recipe}")
def getrecipe(recipe):
    querystring = {"query":recipe}
    response = requests.get(url, headers=headers, params=querystring)
    if(len(response.json()["results"]) == 0):
        return{'msg': "none"}
    else:
        return {'msg': response.json()["results"]}
    
    
    return {'msg': response.json()["results"]}


