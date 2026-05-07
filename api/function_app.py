import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="CalculateArea")
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:

    value = req.params.get('value')

    if not value:
        return func.HttpResponse("Missing value", status_code=400)

    number = int(value)

    result = number * number

    return func.HttpResponse(
        json.dumps({"result": result}),
        mimetype="application/json",
        status_code=200
    )