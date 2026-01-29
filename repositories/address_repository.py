"""Address repository for database operations."""
from sqlalchemy.orm import Session

from models.address import AddressModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.address_schema import AddressSchema


class AddressRepository(BaseRepositoryImpl):
    """Repository for Address entity database operations."""

    def __init__(self, db: Session):
        super().__init__(AddressModel, AddressSchema, db)

    def get_by_client(self, client_id: int):
        """Get all addresses for a specific client."""
        return self.session.query(self.model).filter(self.model.client_id == client_id).all()
