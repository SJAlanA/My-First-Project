# MCQ Application

A Python-based desktop application for creating and taking multiple-choice quizzes. Built with Tkinter and SQLite, this application allows users to both take quizzes and modify quiz questions through an intuitive graphical interface.

## Features

- Interactive GUI for taking quizzes
- Question editor interface for modifying quiz content
- Score tracking and feedback
- Persistent storage using SQLite database
- Support for 5 questions per quiz
- Options to retry quiz if score is below threshold

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)
- SQLite3 (built into Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mcq-application.git
```

2. Navigate to the project directory:
```bash
cd mcq-application
```

3. Run the application:
```bash
python mcq_app.py
```

## Usage

### Taking a Quiz

1. Launch the application
2. Click the "Start" button
3. Answer each question by selecting a radio button
4. Use the ">>" button to move to the next question
5. After the final question, click "Submit" to see your score
6. If you score less than 3 out of 5, you'll have the option to retry

### Modifying Questions

1. From the main menu, click "Change Questions"
2. Use the editor interface to modify questions, options, and correct answers
3. Navigate between questions using the ">>" button
4. Click "Save" to save changes for each question
5. Click "Exit" when finished editing

## Database Structure

The application uses an SQLite database with the following schema:

```sql
CREATE TABLE MCQDB(
    Question text,
    option1 text,
    option2 text,
    option3 text,
    option4 text,
    crtoption integer
)
```

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest new features
3. Submit pull requests

Please ensure your pull requests are well-documented and include relevant test cases.

## Potential Improvements

- Add support for multiple quizzes
- Implement user authentication
- Add a timer feature
- Support for different question types
- Export/import functionality for quiz data

## Author

Sahai Jordi Alan A

## Acknowledgments

- Thanks to the Python community for Tkinter
- All contributors and testers
