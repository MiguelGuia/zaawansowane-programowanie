from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'hello': 'world'})

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

def load_movies():
    movies = []
    with open('data/movies.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            movies.append(Movie(row[0], row[1], row[2]))
    return movies

@app.route('/movies')
def get_movies():
    movies = load_movies()
    return jsonify([movie.__dict__ for movie in movies])


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

@app.route('/links')
def get_links():
    links = []
    with open('data/links.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            links.append(Link(row[0], row[1], row[2]).__dict__)
    return jsonify(links)

@app.route('/ratings')
def get_ratings():
    ratings = []
    with open('data/ratings.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ratings.append(Rating(row[0], row[1], row[2], row[3]).__dict__)
    return jsonify(ratings)

@app.route('/tags')
def get_tags():
    tags = []
    with open('data/tags.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tags.append(Tag(row[0], row[1], row[2], row[3]).__dict__)
    return jsonify(tags)

if __name__ == '__main__':
    app.run(debug=True)