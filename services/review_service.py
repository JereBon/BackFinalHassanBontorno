"""Review service with proper dependency injection."""
from sqlalchemy.orm import Session

from models.review import ReviewModel
from repositories.review_repository import ReviewRepository
from schemas.review_schema import ReviewSchema
from services.base_service_impl import BaseServiceImpl


class ReviewService(BaseServiceImpl):
    """Service for Review entity business logic."""

    def __init__(self, db: Session):
        super().__init__(
            repository_class=ReviewRepository,
            model=ReviewModel,
            schema=ReviewSchema,
            db=db
        )

    def get_by_product_id(self, product_id: int) -> list[ReviewSchema]:
        """Get all reviews for a specific product."""
        from sqlalchemy import select
        from sqlalchemy.orm import joinedload
        stmt = select(ReviewModel).where(ReviewModel.product_id == product_id).options(joinedload(ReviewModel.client))
        models = self._repository.session.scalars(stmt).all()
        return [ReviewSchema.model_validate(model) for model in models]
