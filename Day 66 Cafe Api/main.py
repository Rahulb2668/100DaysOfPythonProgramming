from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1: Manual Mapping (Safest)
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session().execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route("/all")
def get_all():
    results = db.session().execute(db.select(Cafe))
    all_cafes = results.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def find_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location.ilike(f"%{query_location}%")))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe={
        "name": request.form.get("name"),
        "map_url": request.form.get("map_url"),
        "img_url": request.form.get("img_url"),
        "location": request.form.get("location"),
        "seats": request.form.get("seats"),
        "has_toilet": request.form.get("has_toilet"),
        "has_wifi": request.form.get("has_wifi"),
        "has_sockets": request.form.get("has_sockets"),
        "can_take_calls": request.form.get("can_take_calls"),
        "coffee_price": request.form.get("coffee_price"),
    }
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session().get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session().commit()
        return jsonify(response={"Success"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session().get(Cafe, cafe_id)
    if cafe:
        db.session().delete(cafe)
        db.session().commit()
        return jsonify(response={"Success"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
if __name__ == '__main__':
    app.run(debug=True)
