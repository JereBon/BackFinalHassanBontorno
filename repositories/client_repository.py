"""Client repository for database operations."""
from sqlalchemy.orm import Session
from sqlalchemy import select
from passlib.hash import bcrypt

from models.client import ClientModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.client_schema import ClientSchema


class ClientRepository(BaseRepositoryImpl):
    """Repository for Client entity database operations."""

    def __init__(self, db: Session):
        super().__init__(ClientModel, ClientSchema, db)

    def create(self, schema: ClientSchema):
        """Create a new client with hashed password."""
        if schema.password:
            schema.password = bcrypt.hash(schema.password)
        return super().create(schema)

    def get_by_email(self, email: str):
        """Return a ClientModel instance matching the given email, or None."""
        stmt = select(self.model).where(self.model.email == email)
        return self.session.scalars(stmt).first()