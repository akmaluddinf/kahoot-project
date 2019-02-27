# Kahoot Project

#### Kahoot Project adalah sebuah klon dari kahoot.com. Project ini dibuat menggunakan bahasa pemrograman [Python](https://www.python.org/), untuk _framework_ menggunakan [Flask](http://flask.pocoo.org/). Kemudian format datanya menggunakan [JSON](https://www.json.org/) dan [Insomnia](https://insomnia.rest/) untuk melakukan uji coba sebagai _client_.

## Cara _Setup_
- Install [Visual Studia Code](https://code.visualstudio.com/) 
- Install Pyton : `pip install python`
- Install Flask : `pip install flask`
- Install [Insomnia](https://insomnia.rest/)

## Cara Pakai
- **Register**
#### Buka Insomnia, buat _request_ method `POST`, dengan alamat `/register`, dan JSON Body seperti berikut:
```json
{
  "user-id": 101,
  "username": "akmal123", 
  "password": "pass123",
  "email": "akmal@gmail.com",
  "todo": "encrypt"
}
```

- Login
#### Buka Insomnia, buat _request_ method `POST`, dengan alamat `/login`, dan JSON Body seperti berikut:
```json
{
  "username": "akmal123", 
  "password": "akmal123",
  "todo": "encrypt"
}
```

- Create Quiz
#### Buka Insomnia, buat _request_ method `POST` dengan alamat `/quizzes`, dengan JSON Body seperti berikut:
```json
{
  "quiz-id": 124,
  "quiz-name": "tentang aku",
  "quiz-category": "personal",
  "question-list": []
}
```

- Get Quiz
#### Buka Insomnia, buat _request_ method `GET` dengan alamat `/quizzes/<quizId>`

- **Update Quiz**
#### Buka Insomnia, buat _request_ method `PUT` dengan alamat `/quizzes/<quizId>`, dengan JSON Body seperti berikut:
```json
{
	"quiz-id": 123,
	"quiz-name": "tentang dia",
	"quiz-category": "personal",
	"question-list": []
}
```

- Create Game
#### Buka Insomnia, buat _request_ method `POST` dengan alamat `/game`, dengan JSON Body seperti berikut:
```json
{
	"quiz-id": 123
}
```

- Join Game
#### Buka Insomnia, buat _request_ method `POST` dengan alamat `/game/join`, dengan JSON Body seperti berikut:
```json
{
  "game-pin": 179547,
  "username": "akmal"
}
```

## Fitur
- [x] Register
- [x] Login
- [x] Create quiz
- [x] Get quiz
- [x] Update quiz
- [x] Delete quiz
- [x] Create question
- [x] Get question
- [x] Update question
- [x] Delete question
- [x] Create game
- [x] Join game
- [x] Answer the question
- [x] Get leaderboard



