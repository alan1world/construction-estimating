from typing import Any

from faker import Faker
# from flask import render_template, flash, redirect, url_for
# from flask import url_for

# from estimating_construction import app
# from estimating_construction import routes
from estimating_construction.data import models


def setup_fake_data() -> Faker:
    return Faker(["en-GB",])

# @app.app_context  # try moving the link to html so it only needs the int?
def create_full_record(
                    # route_link: str,
                    source: Faker | None = None, 
                    number: int | None = None
                    ) -> list[dict[str, Any]]:
    
    record_list = []

    fake = source or setup_fake_data()
    record_counter = number or fake.random_digit_above_two()  # x2 later to test more results

    for idx in range(record_counter):
        record = dict()

        record["fullname"] = fake.name()
        record["company"] = fake.company()
        record["email"] = fake.ascii_safe_email()
        record["phone_number"] = fake.phone_number()
        record["sop"] = fake.numerify(text="ENV%%%%")
        record["sop_rc"] = fake.random_element(elements=("R", "C"))
        # record["hub"] = "North East"
        record["hub"] = fake.random_element(elements=models.Hub().hubs_as_list())
        record["type"] = "Target"
        record["gateway"] = "0 - Mandate"
        record["partner"] = "Lot 1"
        # record["contract"] = "PSC"
        record["contract"] = fake.random_element(
            elements=models.FrameworkContract().contracts_as_list()
            )

        record["project"] = ''.join((record["sop"], record["sop_rc"]))
        record["name"] = record["fullname"]

        record["enq"] = idx
        # enq_link = url_for('enquiries', id=idx)
        # with app.app_context():
        #     enq_link = url_for('enquiries', id=idx)
        # enq_link = f"http://127.0.0.1:5000/enquiries/{idx}"
        enq_link = f"/enquiries/{idx}"
        record["link"] = enq_link
        

        record_list.append(record)

    return record_list

def create_user_record(
                    source: Faker | None = None, 
                    number: int | None = None
                    ) -> list[dict[str, Any]]:
    
    record_list = []

    fake = source or setup_fake_data()
    record_counter = number or fake.random_digit_above_two()  # x2 later to test more results

    for _ in range(record_counter):
        record = dict()

        record["fullname"] = fake.name()
        record["company"] = fake.company()
        record["email"] = fake.ascii_safe_email()
        record["phone_number"] = fake.phone_number()

        record["name"] = record["fullname"]

        record_list.append(record)

    return record_list

