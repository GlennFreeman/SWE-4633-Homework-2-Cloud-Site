from django_bolt import BoltAPI

api = BoltAPI()


@api.get("/")
async def hello_world():
    return {"hello": "world"}
