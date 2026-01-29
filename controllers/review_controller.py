"""Review controller with proper dependency injection."""
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.base_controller_impl import BaseControllerImpl
from schemas.review_schema import ReviewSchema
from services.review_service import ReviewService


class ReviewController(BaseControllerImpl):
    """Controller for Review entity with CRUD operations."""

    def __init__(self):
        super().__init__(
            schema=ReviewSchema,
            service_factory=lambda db: ReviewService(db),
            tags=["Reviews"]
        )

        @self.router.get("/by_product/{product_id}", response_model=List[ReviewSchema])
        async def get_by_product(product_id: int, db: Session = Depends(get_db)):
            """Get all reviews for a specific product."""
            service = self.service_factory(db)
            return service.get_by_product_id(product_id)