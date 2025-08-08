from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os

app = Flask(__name__)

# CSV 파일에서 단어 데이터를 읽어오는 함수
def load_word_data():
    words = []
    csv_path = os.path.join('WordUp_Last', 'WordUp_list.csv')
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                words.append({
                    'word': row['단어'],
                    'meaning': row['의미'],
                    'genre': row['장르'],
                    'example': row['예문']
                })
    except Exception as e:
        print(f"CSV 파일 읽기 오류: {e}")
        return []
    
    return words

# 사용 가능한 장르 목록을 가져오는 함수
def get_available_genres():
    words = load_word_data()
    genres = set()
    for word in words:
        if word['genre']:
            genres.add(word['genre'])
    return sorted(list(genres))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/goldenbell')
def goldenbell():
    return render_template('goldenbell.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')

@app.route('/goods')
def goods():
    return render_template('goods.html')

# 단어 데이터를 JSON으로 제공하는 API
@app.route('/api/words')
def get_words():
    words = load_word_data()
    return jsonify(words)

# 특정 단어의 상세 정보를 제공하는 API
@app.route('/api/word/<word_name>')
def get_word_detail(word_name):
    words = load_word_data()
    for word in words:
        if word['word'] == word_name:
            return jsonify(word)
    return jsonify({'error': '단어를 찾을 수 없습니다'}), 404

# 사용 가능한 장르 목록을 제공하는 API
@app.route('/api/genres')
def get_genres():
    genres = get_available_genres()
    return jsonify(genres)

# 특정 장르의 단어들을 제공하는 API
@app.route('/api/words/genre/<genre>')
def get_words_by_genre(genre):
    words = load_word_data()
    filtered_words = [word for word in words if word['genre'] == genre]
    return jsonify(filtered_words)

if __name__ == '__main__':
    app.run(debug=True)
