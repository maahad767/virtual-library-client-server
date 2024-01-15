from typing import List
from ninja import Router

from product.models import Category
from product.schemas import CategoryIn, CategoryOut

router = Router()


@router.get("/categories/", response=List[CategoryOut])
def list_categories(request):
    categories = Category.objects.all()
    return categories


@router.get("/categories/<int:pk>/", response=CategoryOut)
def get_category(request, pk: int):
    category = Category.objects.get(pk=pk)
    return category


@router.post("/categories/", response=CategoryIn)
def create_category(request, category_in: CategoryIn):
    category = Category.objects.create(**category_in.dict())
    return category
