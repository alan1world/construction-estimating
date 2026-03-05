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
    # all_answered: bool = False
    status: str = "Draft"
    # answers: list[Any] = field(default_factory=list)
    access: str | None = None
    access_detail: list[str] | None = None
    designations: str | None = None
    designations_detail: list[str] | None = None
    site_compounds: list[str]  | None = None
    site_access: str  | None = None
    price: str  | None = None
    waste: str  | None = None
    ground: str  | None = None
    existing_structures: str | None = None
    existing_structures_detail: list[str] | None = None
    species: list[str]  | None = None
    adverse_influence: str | None = None
    adverse_influence_detail: list[str] | None = None
    milestone: str  | None = None
    missing_utilities: str | None = None
    missing_utilities_detail: list[str] | None = None

    @property
    def access_(self) -> str | list[str] | None:
        _check = None
        if self.access == "Unconstrained":
            _check = self.access
        if self.access == "Constrained":
            _check = self.access_detail
        return _check
    
    @property
    def access_test(self) -> bool:
        _check = False
        if self.access == "Unconstrained":
            _check = True
        if self.access == "Constrained" and self.access_detail:
            _check = True
        return _check

    @property
    def designations_(self) -> str | list[str] | None:
        _check = None
        if self.designations == "No designation":
            _check = self.designations
        if self.designations == "Designations:":
            _check = self.designations_detail
        return _check
    
    @property
    def designations_test(self) -> bool:
        _check = False
        if self.designations == "No designation":
            _check = True
        if self.designations == "Designations:" and self.designations_detail:
            _check = True
        return _check

    @property
    def existing_structures_(self) -> str | list[str] | None:
        _check = None
        if self.existing_structures == "No requirement":
            _check = self.existing_structures
        if self.existing_structures == "Requirements:":
            _check = self.existing_structures_detail
        return _check
    
    @property
    def existing_structures_test(self) -> bool:
        _check = False
        if self.existing_structures == "No requirement":
            _check = True
        if self.existing_structures == "Requirements:" and self.existing_structures_detail:
            _check = True
        return _check

    @property
    def adverse_influence_(self) -> str | list[str] | None:
        _check = None
        if self.adverse_influence == "No":
            _check = self.adverse_influence
        if self.adverse_influence == "Yes":
            _check = self.adverse_influence_detail
        return _check
    
    @property
    def adverse_influence_test(self) -> bool:
        _check = False
        if self.adverse_influence == "No":
            _check = True
        if self.adverse_influence == "Yes" and self.adverse_influence_detail:
            _check = True
        return _check

    @property
    def missing_utilities_(self) -> str | list[str] | None:
        _check = None
        if self.missing_utilities == "None":
            _check = self.missing_utilities
        if self.missing_utilities == "Missing:":
            _check = self.missing_utilities_detail
        return _check
    
    @property
    def missing_utilities_test(self) -> bool:
        _check = False
        if self.missing_utilities == "None":
            _check = True
        if self.missing_utilities == "Missing:" and self.missing_utilities_detail:
            _check = True
        return _check
    
    @property
    def species_test(self) -> bool:
        _check = False
        if self.species:
            _check = True
        return _check
    
    @property
    def site_access_test(self) -> bool:
        _check = False
        if self.site_access:
            _check = True
        return _check
    
    @property
    def price_test(self) -> bool:
        _check = False
        if self.price:
            _check = True
        return _check
    
    @property
    def waste_test(self) -> bool:
        _check = False
        if self.waste:
            _check = True
        return _check
    
    @property
    def ground_test(self) -> bool:
        _check = False
        if self.ground:
            _check = True
        return _check
    
    @property
    def milestone_test(self) -> bool:
        _check = False
        if self.milestone:
            _check = True
        return _check

    @property
    def site_compounds_test(self) -> bool:
        _check = False
        if self.site_compounds:
            _check = True
        return _check
    
    @property
    def species_test(self) -> bool:
        _check = False
        if self.species:
            _check = True
        return _check

    @property
    def all_answered(self):
        return all([
            self.access_test,
            self.designations_test,
            self.site_compounds_test,
            self.site_access_test,
            self.price_test,
            self.waste_test,
            self.ground_test,
            self.existing_structures_test,
            self.species_test,
            self.adverse_influence_test,
            self.milestone_test,
            self.missing_utilities_test,
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
    enq: int
    _person: UserRecord
    _project: ProjectRecord
    cost_driver_draft: CostDrivers = field(default_factory=CostDrivers)
    cost_drivers: list[CostDrivers] = field(default_factory=list)

    # def __post_init__(self):
    #     self.cost_drivers.append(CostDrivers())

    @property
    def link(self) -> str:
        return f"/enquiries/{self.enq}"
    
    @property
    def fullname(self) -> str:
        return self._person.fullname
    
    @property
    def company(self) -> str:
        return self._person.company
    
    @property
    def email(self) -> str:
        return self._person.email
    
    @property
    def phone_number(self) -> str:
        return self._person.phone_number
    
    @property
    def sop(self) -> str:
        return self._project.sop
    
    @property
    def sop_rc(self) -> str:
        return self._project.sop_rc    
    
    @property
    def contract(self) -> str:
        return self._project.contract
    
    @property
    def hub(self) -> str:
        return self._project.hub
    
    @property
    def contract_type(self) -> str:
        return self._project.contract_type
    
    @property
    def gateway(self) -> str:
        return self._project.gateway
    
    @property
    def partner(self) -> str:
        return self._project.partner
    
    @property
    def project(self) -> str:
        return self._project.project
