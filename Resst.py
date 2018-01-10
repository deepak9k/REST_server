from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

record = [
    {
        'id': 1,
        'Name': u'Team 1',
        'about': u'Software department'

    },
    {
        'id': 2,
        'Name': u'Team 2',
        'about': u'Finance department'

    }
]


@app.route("/console/data/company/<int:team_id>", methods=['GET'])
def get_record(team_id):
    task = [task1 for task1 in record if task1['id'] == team_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/console/data/company", methods=['POST'])
def create_record():
    if not request.json or not 'Name' in request.json:
        abort(404)
    task = {
        'id': record[-1]['id'] + 1,
        'Name': request.json['Name'],
        'about': request.json['about']
    }
    record.append(task)
    return jsonify({'task': task}), 201



if __name__ == "__main__":
    app.run()
