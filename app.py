from flask import Flask, request, render_template


from stories import *

app = Flask(__name__)

storyDict = {'story1': story1, "story2":story2, 'story3':story3}

@app.route('/')
def show_home():
  return render_template('home.html')

@app.route('/form/<story_id>')
def show_form(story_id):
  return render_template('form.html', story= storyDict.get(story_id))

@app.route('/form/<story_id>/results')
def show_results(story_id):
  return render_template('form.html', story= storyDict.get(story_id))