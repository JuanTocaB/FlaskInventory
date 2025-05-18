from services.product import Query, Mutation
from flask import jsonify, request
from graphene import Schema
from exceptions.productError import ProductError

class ProductController:

    def __init__ (self) -> None:
        self.schema = Schema(
            query=Query, 
            mutation=Mutation
        )

    def graphql(self):
        try:
            data = request.get_json()
            result = self.schema.execute(
                data.get("query"),
                variable_values=data.get("variables"),
                operation_name=data.get("operationName"),
            )
            if result.errors:
                raise ProductError(
                    result.errors[0].message,
                    500
                )
            return jsonify({
                "data": result.data,
                "messages": "Stock updated successfully",
                "status": 200
            }), 200
        except ProductError as e:
            return jsonify({
                "messages": str(e),
                "status": e.error_code
            }), e.error_code