# import estimating_construction.structures.projects as psp
# import estimating_construction.data.samples as pds
# import estimating_construction.structures.contracts as psc

import json
import itertools

from pathlib import Path

from flask import render_template, redirect, url_for, request
# from flask import send_from_directory, flash

from estimating_construction import app
from estimating_construction.data import faked  #, models
from estimating_construction.data import structures

# from estimating_construction.forms import NewFullEnquiryForm
from estimating_construction.forms import DesignationsForm
from estimating_construction.forms import ProjectPriceFormRadio
from estimating_construction.forms import SiteAccessRadio
from estimating_construction.forms import HazardousWasteRadio
from estimating_construction.forms import GroundConditionsRadio
from estimating_construction.forms import SpeciesForm
from estimating_construction.forms import AccessConstraintForm
from estimating_construction.forms import AccessConstraintFormYes
from estimating_construction.forms import CostDriversForm

# enqs = []
# options = []

# fake_date = faked.create_full_record()
enqs = faked.create_full_record()

samples = {
    "projects": {"P1": "Test 1", "P2": "Test 2", "P3": "Test 3"},
    "contracts": [
        {"key": "C1", "name": "Con 1", "project": "P1"},
        {"key": "C2", "name": "Con 2", "project": "P2"},
        {"key": "C3", "name": "Con 3", "project": "P3"},
        ]
}

# print(structures.CostDrivers().answers)
# print(structures.EstimateEnquiry())


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # print(models.hubs())
    # print(models.Hub().hubs_as_list())
    # form = NewFullEnquiryForm()
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # if form.validate_on_submit():
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     return redirect('/index')
    # if form.validate_on_submit():
    #     next_id = len(enqs)
    #     enq_link = url_for('enquiries', id=next_id)
    #     enq = {
    #         "project": form.sop.data,
    #         "name": form.fullname.data,
    #         "hub": form.hub.data,
    #         "type": form.type.data,
    #         "gateway": form.gateway.data,
    #         "partner": form.partner.data,
    #         "contract": form.contract.data,
    #         "enq": next_id,
    #         "link": enq_link,
    #         }
    #     enqs.append(enq)
    #     flash('Enquiry added for {}'.format(
    #         form.sop.data))
    #     return redirect(url_for('index'))
    # return render_template('index.html', title='Home', user=user, posts=posts, form=form, enqs=enqs)
    return render_template('index.html', title='Home', user=user, posts=posts, enqs=enqs)


@app.route('/enquiries/<int:id>', methods=['GET', 'POST'])
def enquiries(id):
    try:
        enq = enqs[id]
    except:
        return redirect(url_for('index'))
    dform = DesignationsForm()
    ppform = ProjectPriceFormRadio(enqid=id)
    saform = SiteAccessRadio(enqid=id, access="No (Easily accessible with no major logistical issues)")
    hwform = HazardousWasteRadio(enqid=id, waste="No")
    gcform = GroundConditionsRadio(enqid=id)
    spform = SpeciesForm(enqid=id)
    acfform = AccessConstraintForm(enqid=id)
    cdform = CostDriversForm(enqid=id)
    return render_template('enquiries.html',
                           title=f"Enquiry Form {id}",
                           enq=enq,
                           dform=dform,
                           ppform=ppform,
                           saform=saform,
                           hwform=hwform,
                           gcform=gcform,
                           spform=spform,
                           acfform=acfform,
                           cdform=cdform,
                           )


@app.route('/drl/', methods=['GET',])
@app.route('/drl/index', methods=['GET',])  # GET, POST, PUT, +?UPDATE?
def drl():
    root = "estimating_construction"
    # file_categories = f"{root}/{url_for('static', filename='external/categories_rev72-20250324.json')}"
    file_assets = f"{root}/{url_for('static', filename='external/asset-types_rev72-20250324.json')}"
    # file_attributes = "attributes_rev72-20250324.json"
    # file_elements = "elements_rev72-20250324.json"
    # self.file_picklists = "picklists_rev72-20250324.json"
    # with Path(file_categories).open() as f:
    # # with open("estimating_construction/categories.csv") as f:
    #         categories = json.load(f)
    assets = []
    with Path(file_assets).open() as f:
        assets = json.load(f)
        # for item in json.load(f):
        #     asset = {
        #         "label": item["id"].split("/")[-1],
        #         "description": item["description"],
        #         "category": item["category"].split("/")[-1],
        #     }
        #     assets.append(asset)
        # print(assets[0])
    # return redirect(url_for('index'))
    return render_template('drl.html', assets=assets)


@app.route('/fd6dr/', methods=['GET',])
@app.route('/fd6dr/index', methods=['GET',])  # GET, POST, PUT, +?UPDATE?
def fd6dr():
    for item in itertools.cycle(["Yes", "No"]):
        yield item

# @app.route('/enquiries/<int:id>/options/<int:opt>', methods=['GET'])
# def options(id, opt):
#     enq = enqs[id]
#     return render_template('options.html', title=f"Enquiry Form {id}", enq=enq)

# @app.route('/projects', methods=['GET', 'POST'])
# @app.route('/projects/index', methods=['GET', 'POST'])
# def projects():
#     user = dict()
#     user["username"] = "User 1"
#     # contracts = samples["contracts"]
#     user_projects: list[psp.Project] = []
#     for i in pds.make_projects():
#         user_projects.append(i)
#     return render_template('projects.html', title='Projects', user=user, projects=user_projects)

# @app.route('/enquiries', methods=['GET', 'POST'])
# @app.route('/enquiries/index', methods=['GET', 'POST'])
# def contracts():
#     user = dict()
#     user["username"] = "User 1"
#     # contracts = samples["contracts"]
#     user_contracts: list[psc.Project] = []
#     for i in pds.make_contracts():
#         user_contracts.append(i)
#     return render_template('contracts.html', title='Contracts', user=user, contracts=user_contracts)

# @app.route('/assets', methods=['GET', 'POST'])
# @app.route('/assets/index', methods=['GET', 'POST'])
# def assets():
#     pass


# @app.route('/api/v1/<int:id>', methods=['PUT', 'POST',])
@app.route('/api/v1/q', methods=['PUT', 'POST',])
# def cost_driver_questions(id):
def cost_driver_questions():
    form = ProjectPriceFormRadio()
    return render_template('cost_driver_form.html', cdform=form)


@app.route('/api/v1/a', methods=['PUT', 'POST',])
# def cost_driver_questions(id):
def cost_driver_answers():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    # answer = request.form["designation"]
    # return answer
    cdform = CostDriversForm()
    print(cdform.data)
    return render_template('cost_driver_form.html', cdform=cdform)


@app.route('/api/v1/cd1', methods=['POST',])
# def cost_driver_questions(id):
def cost_driver_1():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    # answer = request.form["answer"]
    # _answers = request.form.getlist("answers")
    # if _answers:
    #     answers = '\n'.join(_answers)
    # else:
    #     answers = ""
    # print(answer)
    # print(answers)
    # if answer == "Constrained":
    #     final = answers
    # else:
    #     final = "Unconstrained"
    # return final
    print(request.form)
    answer = request.form["answer"]
    if answer == "Constrained":
        acfform = AccessConstraintFormYes()
    else:
        acfform = AccessConstraintForm()
    return render_template('cost_driver_questions/cd1b.html', acfform=acfform)
    

@app.route('/api/v1/cd4', methods=['PATCH',])
# def cost_driver_questions(id):
def cost_driver_4():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    print(request.form)
    answer = request.form["access"]
    return answer


@app.route('/api/v1/cd6', methods=['POST', 'PATCH',])
# def cost_driver_questions(id):
def cost_driver_6():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    answer = request.form["waste"]
    print(request.form)
    form = HazardousWasteRadio()
    print(form.data)
    if form.validate_on_submit():
        print(form.waste.data)
        # idx = int(form.enqid.data)
        # print(idx)
        enqs[int(form.enqid.data)]["answers"][6] = form.waste.data
        print(enqs[int(form.enqid.data)]["answers"])
        print(all(enqs[int(form.enqid.data)]["answers"]))
    return answer


@app.route('/api/v1/cd7', methods=['PATCH',])
# def cost_driver_questions(id):
def cost_driver_7():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    print(request.form)
    answer = request.form["ground"]
    return answer


@app.route('/api/v1/cd9', methods=['PATCH',])
# def cost_driver_questions(id):
def cost_driver_9():
    # if form.validate_on_submit():
        # return 'WIN'
    # return 'LOSE'
    print(request.form)
    answer = '\n'.join(request.form.getlist("species"))
    return answer

