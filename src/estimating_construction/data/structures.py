from dataclasses import dataclass
from dataclasses import field
# from typing import NamedTuple
from typing import ClassVar
from typing import Any
# from typing import Literal


_questions: tuple[str] = (
    "What is the level of access to the site?",  # 1
    "Are there any official designations for the site?",  # 2
    "What types of site compounds do you have?",  # 3
    "Is the project in a remote location with difficult access to resources?",  # 4
    "How is the project classified?",  # 5
    "Is there any hazardous waste present on the site?",  # 6
    "How would you describe the ground conditions on the site?",  # 7
    "What is required for the existing non-EA structures at the site?",  # 8
    "What type of species are present/anticipated on the site?",  # 9
    "Is the project adversely influenced by any of the following?",  # 10
    "Is the project completion milestone constrained due to an external factor?",  # 11
    "What utilities are not available to connect for the construction works?",  # 12
    )

_answers: tuple[tuple[str]] = (
    (
        "Unconstrained access", 
        "Physically constrained access", 
        "Time limited access (e.g. certain hours accessible)", 
        "Third party access (e.g. access through land owned by others, access rights needed)",
    ),  # 1
    (
        "No designation", 
        "Area of outstanding natural beauty (AONB)", 
        "National Park", 
        "SSSIS, SACs, SPAs, Ramsar wetlands",
        "Marine Conservation Zones",
        "Conservation Zones",
        "TPO (Tree Protection Orders)",
    ),   # 2
    (
        "No compound (welfare only)", 
        "Standard/main compound", 
        "Satellite compound", 
        "Highways",
    ),   # 3
    (
        "No (Easily accessible with no major logistical issues)", 
        "Yes (Significant challenges in accessing materials and labour)",
    ),   # 4
    (
        "Standard Project (£1m-£50m)",
        "Major Project (£50m+)",
        "Minor Project (below £1m)",
    ),   # 5
    (
        "No",
        "Yes",
    ),   # 6
    (
        "No issues",
        "Minor issues",
        "Severe issues",
    ),   # 7
    (
        "No requirement", 
        "Removal (Complete demolition and disposal)", 
        "Relocation or Diversion (Moving structures to a new location, service or road diversion)", 
        "Partial Removal (Selective demolition and disposal)",
        "Protection of existing structures (existing structures in place)",
    ),   # 8
    (
        "Common Species (e.g. native species with no special status)", 
        "Protected Species (e.g. endangered or threatened species)", 
        "Invasive Species (e.g. species that disrupt local ecosystems)", 
        "Migratory Species (e.g. species that move through the area seasonally)",
    ),   # 9
    (
        "No", 
        "Water", 
        "Railway", 
        "Highways",
        "Process Plants",
        "Buries pipelines",
        "Electricity routes",
    ),   # 10
    (
        "Completion date set by programme logic (no constraints)",
        "Desirable completion used for completion date",
        "Seasonal deadline used for completion date",
        "Critical to complete by completion date",
    ),   # 11
    (
        "None", 
        "Water", 
        "Foul Water", 
        "Power",
        "Data/Telecommunications",
    ),   # 12
    )

_answer_type: tuple[str] = (
    "OneOrMany",  # 1
    "OneOrMany",  # 2
    "Many",  # 3
    "One",  # 4
    "One",  # 5
    "One",  # 6
    "One",  # 7
    "OneOrMany",  # 8
    "Many",  # 9
    "OneOrMany",  # 10
    "One",  # 11
    "OneOrMany",  # 12
    )

# @dataclass
# class ProjectRecord:
#     pass


# @dataclass(slots=True, frozen=True)
# class CostDriverQuestion:
#     '''
#     Question Text
#     Answers
#     Answer Type
#     slots and Frozen
#     '''
#     question: str
#     answers: str
#     answer_type: str


# class CostDriverQuestion(NamedTuple):
#     '''
#     TODO: Create literal type for answer_type
#     '''
#     question: str
#     answer_type: str  # Single, Multi, YesNoMulti => One, Many, OneOrMany
#     answers: tuple[str]


# @dataclass(slots=True)
# class CostDrivers:
#     '''
#     Questions 1-12 - list of questions
#     Answers
#     Answer Type
#     Has it been answered? / Have all been answered
#     Status - Ready, Draft, Final
#     Version nbr int
#     slots
#     '''
#     version: int = 0
#     all_answered: bool = False
#     status: str = "Draft"
#     questions: ClassVar[tuple[CostDriverQuestion]] = field(
#         default_factory=lambda: (
#             CostDriverQuestion(
#                 question="What is the level of access to the site?",
#                 answer_type="OneOrMany",
#                 answers=(
#                     "Unconstrained access",
#                     "Physically constrained access",
#                     "Time limited access (e.g. certain hours accessible)",
#                     "Third party access (e.g. access through land owned by others, access rights needed)",
#                 )
#             ),
#             CostDriverQuestion(
#                 question="What is the level of access to the site?",
#                 answer_type="OneOrMany",
#                 answers=(
#                     "Unconstrained access",
#                     "Physically constrained access",
#                     "Time limited access (e.g. certain hours accessible)",
#                     "Third party access (e.g. access through land owned by others, access rights needed)",
#                 )
#             ), 
#             CostDriverQuestion(
#                 question="What is the level of access to the site?",
#                 answer_type="OneOrMany",
#                 answers=(
#                     "Unconstrained access",
#                     "Physically constrained access",
#                     "Time limited access (e.g. certain hours accessible)",
#                     "Third party access (e.g. access through land owned by others, access rights needed)",
#                 )
#             ),
#         )
#     )


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
    # questions: ClassVar[tuple[str]] = field(default_factory=lambda:
    questions: ClassVar[tuple[str]] = _questions
    answers: ClassVar[tuple[str]] = _answers
    answer_type: ClassVar[tuple[str]] = _answer_type
    responses: list[Any] = field(default_factory=list)


@dataclass(slots=True)
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
    fullname: str
    company: str
    email: str
    phone_number: str
    sop_rc: str
    contract: str
    hub: str
    enq: int
    cost_drivers: list[CostDrivers] = field(default_factory=list)
    type: str = "Target"
    gateway: str = "Lot 1"

    def __post_init__(self):
        self.cost_drivers.append(CostDrivers())

    @property
    def link(self):
        return f"/enquiries/{self.idx}"

    @property
    def project(self):
        return ''.join(self.sop, self.sop_rc)

