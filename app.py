from flask import jsonify, request

from configfile import create_app

from master import master_api

from account import account_api

import pdb


app = create_app()

app.register_blueprint(master_api)
app.register_blueprint(account_api)


if __name__ ==  "__main__":
    app.run(debug=True, use_debugger=True)
