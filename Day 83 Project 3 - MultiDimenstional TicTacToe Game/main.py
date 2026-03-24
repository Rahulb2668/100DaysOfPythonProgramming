from logic import Board
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

players = ['X', 'O']

game_board = Board()
current_player = 1 # 1 for X and 2 for O

@app.route("/")
def init_game():
    global game_board, current_player

    game_board = Board()

    current_player = 1

    return render_template('index.html')

@app.route("/move",methods=["POST"])
def move():
    global current_player
    data = request.json
    row = int(data['row'])
    col = int(data['col'])

    if game_board.place_mark(row, col, current_player):

        # 2. Check for Win
        if game_board.check_win(current_player):
            return jsonify({"status": "win", "player": current_player})

        # 3. Check for Draw
        if game_board.is_draw():
            return jsonify({"status": "draw"})

        # 4. Switch Player
        current_player = 2 if current_player == 1 else 1
        return jsonify({"status": "success", "next_player": current_player})

    return jsonify({"status": "error", "message": "Invalid Move"}), 400

if __name__ == "__main__":
    app.run()



