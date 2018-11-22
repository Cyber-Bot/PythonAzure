from flask import (
    Flask,
    render_template,
	request, jsonify
)

app = Flask(__name__)

plans = [
    {'planId': 1,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '1 Weeks',
     'filename': 'S1P1W1.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	 ,
	 "createdDate": "2018-11-16"
	 },
    {'planId': 3,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '2 Weeks',
     'filename': 'S1P1W2.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	 ,
	 "createdDate": "2018-11-16"
	 },
    {'planId': 3,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '3 Weeks',
     'filename': 'S1P1W3.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	,
	 "createdDate": "2018-11-16"
	 },
]

@app.route('/', methods=['GET'])

def home():
    return "OK"

@app.route('/plans', methods=['GET'])
def api_all():
    return jsonify(plans)
	
@app.route('/BuildPlan', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for plan in plans:
        if plan['planId'] == id:
            results.append(plan)
    return jsonify(id)

app.run()