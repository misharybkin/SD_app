from flask import Flask, request, jsonify
import subprocess
#API test

app = Flask(__name__)
@app.route('/api/jedna_dg_wiele_userow', methods=['POST'])
def jedna_dg_wiele_userow():
    data = request.get_json()
    nr_ewidencyjny = data.get('nr_ewidencyjny')
    skrzynki = data.get('skrzynki')

    with open("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/dg.txt", "w") as temp_skrzynki:
        temp_skrzynki.truncate()
        temp_skrzynki.write(skrzynki)

    with open("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/userzy.txt", "w") as temp_user:
        temp_user.truncate()
        temp_user.write(nr_ewidencyjny)

    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)