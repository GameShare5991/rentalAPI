from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, firestore
import json
from flask_cors import CORS

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
CORS(app)

#to add user renting the game: http://localhost:3005/addRental/?gameId=GAMEIDHERE&rentalUser=USERNAMEHERE

#for retriving all games the user rented, go to http://localhost:3005/rentals?rentalUser=USERNAMEHERE

#add rental user
def addRentalUser(gameId, newrentalUser):
    request_data = {"id": gameId, "rentalUser": newrentalUser}
    games = db.collection('games').where("id", "==", gameId).get()
    docid = games[0].id
    data = {}

    if 'rentalUser' in request_data:
        rentalUser = request_data['rentalUser']
        data['rentalUser'] = rentalUser


    data = {"rentalUser" : rentalUser}
    db.collection('games').document(docid).update(data)
    
    return '',200

#display games in db with rental id = to the user
@app.route('/addRental/', methods=['GET', 'POST'])
def addRental():
    gameId = request.args.get('gameId')
    rentalUser = request.args.get('rentalUser')
    return addRentalUser(gameId, rentalUser)
    

#display all games the user has rented
#get game by rentalUser
@app.route('/rentals', methods=['GET'])
def getRentals():
    rentalUser = request.args.get('rentalUser')
    games = db.collection('games').where("rentalUser", "==", rentalUser).get()
    game = games[0].to_dict()
    return json.dumps(game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005, debug=True)