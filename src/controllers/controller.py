from flask import request
FORM = 'name'


def get_form_data():
    data = request.form.get(FORM)  # pega o valor do campo 'name'
    if data:
        return 200, data
    else:
        return 400, None