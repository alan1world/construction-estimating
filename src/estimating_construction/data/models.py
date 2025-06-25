import typing

import sqlalchemy as sqa
import sqlalchemy.orm as sqo

# from typing import Sequence  # typing.Sequence

# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker


# base_ = 'sqlite:///'
# backend_ = 'links.db'
# records_ = f'{base_}records.db'
# drl_ = f'{base_}drl.db'

# engine = sqa.create_engine()
backend_engine = sqa.create_engine("sqlite:///estimating_construction/data/links.db")

class Model(sqo.DeclarativeBase):
    pass


# class Gateway(Model):
#     __tablename__ = "gateways"
    
#     pass


class FrameworkContract(Model):
    __tablename__ = "contracts"

    contract_id: Mapped[int] = mapped_column(primary_key=True)
    contract: Mapped[str] = mapped_column(String(3))

    def __str__(self) -> str:
        return f"{self.contract}"
    
    def __repr__(self) -> str:
        return f"<FrameworkContract: {self.contract_id=}, {self.contract=}>"

    @classmethod
    def contracts(cls):
        session = Session()
        q = select(cls.contract)
        r = session.scalars(q)
        return r
    
    @classmethod
    def contracts_as_list(cls) -> typing.Sequence[str]:
        session = Session()
        q = select(cls.contract)
        # r = session.execute(q).all()
        r = session.scalars(q).all()
        return r


class Hub(Model):
    __tablename__ = "hubs"

    hub_id: Mapped[int] = mapped_column(primary_key=True)
    hub: Mapped[str]

    def __str__(self) -> str:
        return f"{self.hub}"
    
    def __repr__(self) -> str:
        return f"<Hub: {self.hub_id=}, {self.hub=}>"

    @classmethod
    def hubs(cls):
        session = Session()
        q = select(cls.hub)
        r = session.scalars(q)
        return r
    
    @classmethod
    def hubs_as_list(cls) -> typing.Sequence[str]:
        session = Session()
        q = select(cls.hub)
        # r = session.execute(q).all()
        r = session.scalars(q).all()
        return r


# class Partner(Model):
#     __tablename__ = "partners"
    
#     pass


# class EstimateType(Model):
#     __tablename__ = "estimatetypes"

#     pass

# Model.metadata.create_all(engine)
# Mode.metadata.drop_all(engine)

Session = sessionmaker(backend_engine)

# with Session() as session:
    # with session.begin():



