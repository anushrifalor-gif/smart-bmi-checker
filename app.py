from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = None

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100

        bmi = weight / (height ** 2)

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"
            suggestion = "Increase nutritious food intake and maintain a balanced diet."

        elif bmi < 25:
            category = "Normal Weight"
            suggestion = "Great! Maintain your healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            suggestion = "Increase physical activity and reduce processed foods."

        else:
            category = "Obese"
            suggestion = "Consider consulting a healthcare professional."
        if bmi < 18.5:
            score = 65

        elif bmi < 25:
            score = 92
    
        elif bmi < 30:
            score = 75

        else:
            score = 55

        # Water Intake Recommendation
        water = round(weight * 0.033, 1)

        result = {
    "name": name,
    "age": age,
    "gender": gender,
    "bmi": round(bmi, 2),
    "category": category,
    "water": water,
    "suggestion": suggestion,
    "score": score
}

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)