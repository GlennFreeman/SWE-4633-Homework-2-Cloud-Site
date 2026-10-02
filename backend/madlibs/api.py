from django_bolt import BoltAPI

api = BoltAPI()


@api.get("/api/hello")
async def hello_world():
    return {"hello": "world"}
