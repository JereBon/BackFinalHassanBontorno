from typing import Optional, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

from schemas.client_schema import PublicClientSchema

if TYPE_CHECKING:
    from schemas.product_schema import ProductSchema


class ReviewSchema(BaseSchema):
    """Product review schema with validation"""

    rating: float = Field(
        ...,
        ge=1.0,
        le=5.0,
        description="Rating from 1 to 5 stars (required)"
    )

    comment: Optional[str] = Field(
        None,
        min_length=10,
        max_length=1000,
        description="Review comment (optional, 10-1000 characters)"
    )

    product_id: int = Field(
        ...,
        description="Product ID reference (required)"
    )

    product: Optional['ProductSchema'] = None

    client_id: int = Field(
        ...,
        description="Client ID reference (required)"
    )

    client: Optional[PublicClientSchema] = None
