"""Address controller with proper dependency injection."""
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.base_controller_impl import BaseControllerImpl
from schemas.address_schema import AddressSchema
from services.address_service import AddressService


class AddressController(BaseControllerImpl):
    """Controller for Address entity with CRUD operations."""

    def __init__(self):
        super().__init__(
            schema=AddressSchema,
            service_factory=lambda db: AddressService(db),
            tags=["Addresses"]
        )

        @self.router.get("/by_client/{client_id}", response_model=List[AddressSchema])
        async def get_by_client(client_id: int, db: Session = Depends(get_db)):
            """Get all addresses for a specific client."""
            service = self.service_factory(db)
            return service.get_by_client(client_id)