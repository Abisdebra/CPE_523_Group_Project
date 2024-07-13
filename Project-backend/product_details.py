from botocore.exceptions import ClientError
import logging
import uuid

logger = logging.getLogger(__name__)

class ProductDetails:
    def __init__(self, ddb_resource):
        self.ddb_resource = ddb_resource
        try:
            table = ddb_resource.Table("Product_Details_Table")
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Table does not exist!")
            else:
                logger.error("Could not check for existence of table: %s, %s", err.response["Error"]["Code"], err.response["Error"]["Message"])
                raise
        self.table = table

    def add_product(self, name, price, expiry_date):
        try:
            self.table.put_item(
                Item = {
                    "product_id": str(uuid.uuid4()),
                    "name": name,
                    "price": price,
                    "expiry_date": expiry_date
                }
            )
        except ClientError as err:
            logger.error("Could not add product %s to the table %s: %s, %s", name, self.table.name, err.response["Error"]["Code"], err.response["Error"]["Message"])
            raise

    #get_all_products @Jose 
    #update_product_with_id @Jose
    #search with multiple attributes @me
