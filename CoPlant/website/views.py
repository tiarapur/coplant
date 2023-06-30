from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Plant, Guide
from . import db
import json

views = Blueprint('views', __name__)

""" Note """

@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard ():
    return render_template("dashboard.html", user=current_user)

@views.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
    all_post = Note.query.order_by(Note.date)
    return render_template("blog.html", user=current_user, all_post=all_post)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

""" Market """

@views.route('/market', methods=['GET', 'POST'])
@login_required
def plant():
    if request.method == 'POST': 
        plant = request.form.get('plant')

        if len(plant) < 1:
            flash('There is no such plant', category='error') 
        else:
            new_plant = Plant(plantname=plant, user_id=current_user.id) 
            db.session.add(new_plant)
            db.session.commit()
            flash('Plant added!', category='success')
    all_plant = Plant.query.order_by(Plant.plant_date)
    return render_template("market.html", user=current_user, all_plant=all_plant)

@views.route('/delete-plant', methods=['POST'])
def delete_plant():  
    plant = json.loads(request.data)
    plantId = plant['plantId']
    plant = Plant.query.get(plantId)
    if plant:
        if plant.user_id == current_user.id:
            db.session.delete(plant)
            db.session.commit()

    return jsonify({})
    

@views.route('/guide', methods=['GET', 'POST'])
@login_required
def guide():
    if request.method == 'POST': 
        guide_title = request.form.get('guide_title')
        guide_content = request.form.get('guide_content')
        if len(guide_title) < 1:
            flash('Choose a title', category='error')
        elif len(guide_content) < 3:
            flash('Write more', category='error')
        else:
            new_post = Guide(guide_title=guide_title, guide_content=guide_content, user_id=current_user.id) 
            db.session.add(new_post)
            db.session.commit()
            flash('Post added!', category='success')
    return render_template("Guide.html", user=current_user)

@views.route('/user', methods=['GET', 'POST'])
@login_required
def user ():
    return render_template("user.html", user=current_user)