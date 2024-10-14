# Python Random Words API

Django app for querying random words from an API endpoint.

All endpoints return a JSON array containing zero, one, or multiple words.

| Endpoint           | Description |
| :----------------- | :------------------------- |
| /api/word          | Returns one random word from the database |
| /api/word/$length  | Returns one random word of length $length from the database   |
| /api/words         | Returns all words from the database   |
| /api/words/$length | Returns all words of length $length from the database   |

* This app is a work-in-progress and not fully functional.

## TODO

- Handle responses when no words are in the database
- Make production ready
- Setup initial data migrations from JSON or TXT
- Docker container