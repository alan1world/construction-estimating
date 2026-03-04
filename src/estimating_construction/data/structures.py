from dataclasses import dataclass
from dataclasses import field
# from typing import NamedTuple
from typing import ClassVar
from typing import Any
# from typing import Literal


@dataclass(slots=True)
class UserRecord:
    fullname: str
    company: str
    email: str
    phone_number: str | None = None


@dataclass(slots=True)
class ProjectRecord:
    sop_rc: str
    sop: str
    contract: str
    hub: str
    contract_type: str = "Target"
    gateway: str = "Lot 1"

    @property
    def project(self):
        return ''.join([self.sop, self.sop_rc])


@dataclass(slots=True)
class CostDrivers:
    '''
    Questions 1-12 - list of questions
    Answers
    Answer Type
    Has it been answered? / Have all been answered
    Status - Ready, Draft, Final
    Version nbr int
    '''
    version: int = 0
    all_answered: bool = False
    status: str = "Draft"
    # answers: list[Any] = field(default_factory=list)
    access: str | list[str] | None = None
    designations: str | list[str] | None = None
    site_compounds: list[str]  | None = None
    site_access: str  | None = None
    price: str  | None = None
    waste: str  | None = None
    ground: str  | None = None
    existing_structures: str | list[str]  | None = None
    species: list[str]  | None = None
    adverse_influence: str | list[str]  | None = None
    milestone: str  | None = None
    missing_utilities: str | list[str]  | None = None

    @property
    def all_answered1(self):
        return all([
            self.access,
            self.designations,
            self.site_compounds,
            self.site_access,
            self.price,
            self.waste,
            self.ground,
            self.existing_structures,
            self.species,
            self.adverse_influence,
            self.milestone,
            self.missing_utilities,
        ])



@dataclass
class EstimateEnquiry:
    '''    
    User fields:
        record["fullname"] = fake.name()
        record["company"] = fake.company()
        record["email"] = fake.ascii_safe_email()
        record["phone_number"] = fake.phone_number()
        record["name"] = record["fullname"]

    Project fields:
        record["sop_rc"] = fake.random_element(elements=("R", "C"))
        record["type"] = "Target"
        record["gateway"] = "0 - Mandate"
        record["partner"] = "Lot 1"
        record["project"] = ''.join((record["sop"], record["sop_rc"]))
        record["contract"] = fake.random_element(
            # elements=models.FrameworkContract().contracts_as_list()
            elements=("PSC", "ECC")
            )
        record["hub"] = fake.random_element(elements=("North East",
                                                      "North West",
                                                      "South East",
                                                      "South West",
                                                      "Midlands",
                                                      "Eastern",))

    Enquiry / Estimate fields:
        record["enq"] = idx
        enq_link = f"/enquiries/{idx}"
        record["link"] = enq_link

    Attach a User object, use properties to get / set as if top level fields.
    Hubs as ClassVar; Hub as the chosen value.

    Eventually? attach Project and Contract objects, use properties to function as top-level.

    Cost Drivers fields:
        TBC
    '''
    person: UserRecord
    project: ProjectRecord
    enq: int
    cost_drivers: list[CostDrivers] = field(default_factory=list)

    def __post_init__(self):
        self.cost_drivers.append(CostDrivers())

    @property
    def link(self) -> str:
        return f"/enquiries/{self.enq}"
    
    @property
    def fullname(self) -> str:
        return self.person.fullname
    
    @property
    def company(self) -> str:
        return self.person.company
    
    @property
    def email(self) -> str:
        return self.person.email
    
    @property
    def phone_number(self) -> str:
        return self.person.phone_number
    
    @property
    def sop(self) -> str:
        return self.project.sop
    
    @property
    def sop_rc(self) -> str:
        return self.project.sop_rc    
    
    @property
    def contract(self) -> str:
        return self.project.contract
    
    @property
    def hub(self) -> str:
        return self.project.hub
    
    @property
    def contract_type(self) -> str:
        return self.project.contract_type
    
    @property
    def gateway(self) -> str:
        return self.project.gateway
    
    @property
    def partner(self) -> str:
        return self.project.partner
    
    @property
    def project(self) -> str:
        return self.project.project