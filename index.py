import webbrowser
import os

# Save the HTML content to a specific path
file_path = os.path.abspath('quiz.html')  # Get the absolute path

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }
        .quiz-container {
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .question {
            margin-bottom: 15px;
        }
        .answers label {
            display: block;
            margin-bottom: 8px;
        }
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            width: 100%;
        }
        .submit-btn:hover {
            background-color: #45a049;
        }
        .result {
            display: none;
            text-align: center;
            margin-top: 20px;
            font-size: 1.2em;
            color: #4CAF50;
        }
    </style>
</head>
<body>

    <div class="quiz-container">
        <h1>Simple Quiz</h1>
        <form id="quizForm">
            <div class="question">
                <p>1. What is the capital of France?</p>
                <div class="answers">
                    <label><input type="radio" name="q1" value="Paris"> Paris</label>
                    <label><input type="radio" name="q1" value="London"> London</label>
                    <label><input type="radio" name="q1" value="Rome"> Rome</label>
                </div>
            </div>
            <div class="question">
                <p>2. Which language is used for web development?</p>
                <div class="answers">
                    <label><input type="radio" name="q2" value="Python"> Python</label>
                    <label><input type="radio" name="q2" value="JavaScript"> JavaScript</label>
                    <label><input type="radio" name="q2" value="C++"> C++</label>
                </div>
            </div>
            <div class="question">
                <p>3. Who is the creator of Microsoft?</p>
                <div class="answers">
                    <label><input type="radio" name="q3" value="Steve Jobs"> Steve Jobs</label>
                    <label><input type="radio" name="q3" value="Bill Gates"> Bill Gates</label>
                    <label><input type="radio" name="q3" value="Mark Zuckerberg"> Mark Zuckerberg</label>
                </div>
            </div>
            <button type="button" class="submit-btn" onclick="checkAnswers()">Submit</button>
        </form>
        <div class="result" id="result"></div>
    </div>

    <script>
        function checkAnswers() {
            var score = 0;
            var totalQuestions = 3;

            // Get answers
            var q1 = document.querySelector('input[name="q1"]:checked');
            var q2 = document.querySelector('input[name="q2"]:checked');
            var q3 = document.querySelector('input[name="q3"]:checked');

            // Check answers
            if (q1 && q1.value === "Paris") score++;
            if (q2 && q2.value === "JavaScript") score++;
            if (q3 && q3.value === "Bill Gates") score++;

            // Display result
            var result = document.getElementById('result');
            result.innerHTML = "You scored " + score + " out of " + totalQuestions;
            result.style.display = "block";

            // Disable all radio buttons after submission
            var radios = document.querySelectorAll('input[type="radio"]');
            radios.forEach(function(radio) {
                radio.disabled = true;
            });

            // Disable submit button after submission
            document.querySelector('.submit-btn').disabled = true;
        }
    </script>

</body>
</html>
'''

# Save the HTML content to the file
with open(file_path, 'w') as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open_new_tab(file_path)
