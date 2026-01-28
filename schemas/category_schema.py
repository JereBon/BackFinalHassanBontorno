"""Category schema with validation."""
from typing import Optional, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

# Remove import to break cycle
# if TYPE_CHECKING:
#     from schemas.product_schema import ProductSchema


class CategorySchema(BaseSchema):
    """Schema for Category entity with validations."""

    name: str = Field(..., min_length=1, max_length=100, description="Category name (required, unique)")
    # Removed recursive products list to prevent infinite loop
    # products: Optional[List['ProductSchema']] = []
