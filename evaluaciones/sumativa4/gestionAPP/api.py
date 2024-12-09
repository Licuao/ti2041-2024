from ninja import NinjaAPI

api = NinjaAPI()

@api.get("hello")
def hello(request, name):
    return f"Hello {name}"

@api.get("sumar")
def sumar(request, a: int, b: int):
    return {"resultado": a + b}

@api.get("restar")
def restar(request, a: int, b: int):
    return {"resultado": a - b}