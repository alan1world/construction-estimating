# import estimating_construction.structures.projects as psp
# import estimating_construction.data.samples as pds
# import estimating_construction.structures.contracts as psc

from flask import render_template, flash, redirect, url_for

from estimating_construction import app
from estimating_construction.forms import NewFullEnquiryForm


enqs = []
options = []

samples = {
    "projects": {"P1": "Test 1", "P2": "Test 2", "P3": "Test 3"},
    "contracts": [
        {"key": "C1", "name": "Con 1", "project": "P1"},
        {"key": "C2", "name": "Con 2", "project": "P2"},
        {"key": "C3", "name": "Con 3", "project": "P3"},
        ]
} 

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NewFullEnquiryForm()
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
    if form.validate_on_submit():
        next_id = len(enqs)
        enq_link = url_for('enquiries', id=next_id)
        enq = {
            "project": form.sop.data,
            "name": form.fullname.data,
            "hub": form.hub.data,
            "type": form.type.data,
            "gateway": form.gateway.data,
            "partner": form.partner.data,
            "contract": form.contract.data,
            "enq": next_id,
            "link": enq_link,
            }
        enqs.append(enq)
        flash('Enquiry added for {}'.format(
            form.sop.data))
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', user=user, posts=posts, form=form, enqs=enqs)

@app.route('/enquiries/<int:id>', methods=['GET'])
def enquiries(id):
    try:
        enq = enqs[id]
    except:
        return redirect(url_for('index'))
    return render_template('enquiries.html', title=f"Enquiry Form {id}", enq=enq)

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

