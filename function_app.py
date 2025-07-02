import logging
import uuid
import json
from azure.data.tables import TableServiceClient, TableEntity
import azure.functions as func
from azure.identity import DefaultAzureCredential

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
##output binding
@app.table_output(arg_name="message",
                  connection="AZURE_COSMOS_CONNECTIONSTRING",
                  table_name="dev00cosmosdbtable"
            ) 
def http_trigger(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info("Processing request to insert into Cosmos DB Table API")

    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    partition_key = data.get("partitionKey")
    row_key = data.get("rowKey") or str(uuid.uuid4())
    value = data.get("value")

    if not (partition_key and value):
        return func.HttpResponse("Missing required fields: 'partitionKey' and 'value'", status_code=400)


# Cosmos DB connection
    try:
        new_entity = {
            "PartitionKey": partition_key,
            "RowKey": row_key,
            "Value": value
        }

        table_json = json.dumps(new_entity)
        message.set(table_json)
        return table_json

    except Exception as e:
        logging.error(f"Error inserting entity: {e}")
        return func.HttpResponse("Error inserting entity", status_code=500)