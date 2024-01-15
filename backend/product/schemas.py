from ninja import ModelSchema, Schema, Field

from product.models import Category


class CategoryIn(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name"]

class CategoryOut(ModelSchema):
    class Config:
        model = Category
        model_fields = ["id", "name"]
        