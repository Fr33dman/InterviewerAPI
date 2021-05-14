# Setup
1. Clone this repo to your computer
2. Print this in ur console
```
python manage.py makemigrations
python manage.py migrate
```
3. Then you can go ``/admin``
you have user fr33dman Razbok2002 with roots
# API

### Authentication
``/token/``

### Refresh authentication token
``/token/refresh/``

### Interviews endpoint
General information about interview

#### URL
``/interview/``

#### Fields
|Field          |Type      | Description                                                                                |
|---------------|----------|--------------------------------------------------------------------------------------------|
|name           | string   | name of interview                                                                          |
|start_time     | datetime | example : "2021-05-14 16:32:56", time when interview starts                                |
|end_time       | datetime | example : "2021-05-14 16:32:56", time when interview ends                                  |
|description    | string   | description of interview                                                                   |

### Question endpoint
Questions in each interview

Question can be one of 3 types:
- Text answer (TA)
- One answer (OA)
- Many answers (MA)

#### URL
``/question/``

#### Fields
|Field          |Type      | Description                                                                                |
|---------------|----------|--------------------------------------------------------------------------------------------|
|interview      | int      | id of interview                                                                            |
|text           | string   | text of question                                                                           |
|type           | string   | one of types "TA" / "OA" / "MA"                                                            |

### Possible answer endoint
Possible answers that user can choose if question type is "One answer" or "Many answers"

#### URL
``/possible-answer/``

#### Fields
|Field          |Type      | Description                                                                                |
|---------------|----------|--------------------------------------------------------------------------------------------|
|question       | int      | id of question                                                                             |
|text           | string   | text of possible answer                                                                    |

### Answer endpoint
User's answer on each question

#### URL
``/answer/``

#### Fields
|Field          |Type      | Description                                                                                |
|---------------|----------|--------------------------------------------------------------------------------------------|
|user           | int      | id of interview                                                                            |
|interview      | int      | text of question                                                                           |
|answer         | int      | id of answer if question type is "One answer" or "Many answers"                            |
|text_answer    | string   | answer text if question type is "Text answer"                                              |
