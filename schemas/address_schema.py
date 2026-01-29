"""Address schema for request/response validation."""
from typing import Optional
from pydantic import Field

from schemas.base_schema import BaseSchema


class AddressSchema(BaseSchema):
    """Schema for Address entity with validations."""

    street: Optional[str] = Field(None, min_length=1, max_length=200, description="Street name")
    number: Optional[str] = Field(None, max_length=20, description="Street number")
    city: Optional[str] = Field(None, min_length=1, max_length=100, description="City name")
    state: Optional[str] = Field(None, min_length=1, max_length=100, description="State/Province")
    zip_code: Optional[str] = Field(None, max_length=20, description="Postal/Zip Code")
    client_id: int = Field(..., description="Client ID reference (required)")
