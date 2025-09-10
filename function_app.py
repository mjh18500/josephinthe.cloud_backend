import logging
import uuid
import json
from azure.data.tables import TableServiceClient
import azure.functions as func
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request to increment visitor count")

    partition_key = "visitorcount"
    row_key = "count"

    try:
        # Connect to the table
        connection_string = os.getenv("AZURE_COSMOS_CONNECTIONSTRING")
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
        table_name = os.getenv("AZURE_COSMOS_TABLENAME")
        table_client = table_service.get_table_client(table_name=table_name)

        try:
            entity = table_client.get_entity(partition_key=partition_key, row_key=row_key)
            current_value = int(entity.get("Value", 0))
            logging.info(f"Current visitor count: {current_value}")
        except:
            entity = {"PartitionKey": partition_key, "RowKey": row_key, "Value": 0}
            current_value = 0
            logging.info("Entity not found. Initializing count to 0.")

        # Increment
        new_value = current_value + 1
        entity["Value"] = new_value

        # Upsert entity (create or replace)
        table_client.upsert_entity(entity)

        return func.HttpResponse(
            json.dumps({"new_visitor_count": new_value}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error updating visitor count: {e}")
        return func.HttpResponse("Error updating visitor count", status_code=500)