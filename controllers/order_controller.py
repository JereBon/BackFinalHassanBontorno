from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.base_controller_impl import BaseControllerImpl
from schemas.order_schema import OrderSchema
from services.order_service import OrderService


class OrderController(BaseControllerImpl):
    """Controller for Order entity with CRUD operations."""

    def __init__(self):
        super().__init__(
            schema=OrderSchema,
            service_factory=lambda db: OrderService(db),
            tags=["Orders"]
        )

        @self.router.get("/by_client/{client_id}", response_model=List[OrderSchema])
        async def get_by_client(client_id: int, db: Session = Depends(get_db)):
            """Get all orders for a specific client."""
            service = self.service_factory(db)
            return service.get_by_client_id(client_id)