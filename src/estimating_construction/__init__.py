# SPDX-FileCopyrightText: 2025-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT

from flask import Flask

print(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from estimating_construction import routes

# app.run(debug=False)
app.run(debug=False)

