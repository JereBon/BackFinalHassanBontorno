from sqlalchemy.orm import Session
from models.address import AddressModel
from repositories.address_repository import AddressRepository
from schemas.address_schema import AddressSchema
from services.base_service_impl import BaseServiceImpl


class AddressService(BaseServiceImpl):
    def __init__(self, db: Session):
        super().__init__(
            repository_class=AddressRepository,
            model=AddressModel,
            schema=AddressSchema,
            db=db
        )

    def get_by_client(self, client_id: int):
        """Get addresses by client ID."""
        return self.repository.get_by_client(client_id)
