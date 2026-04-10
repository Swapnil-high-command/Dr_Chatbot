 from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    
    if "hello" in user_message or "hi" in user_message:
        reply = "Hello! I am Medi-Bot. How can I help you?"

    elif "bye" in user_message:
        reply = "Goodbye! Take care 😊"

    
    elif "fever" in user_message:
        reply = "You may have fever. Drink fluids and take rest."

    elif "headache" in user_message:
        reply = "Try resting and staying hydrated."

    elif "cold" in user_message or "cough" in user_message:
        reply = "It might be a common cold. Stay warm."

    elif "covid" in user_message:
        reply = "If you have symptoms like fever or breathing issues, get tested."

    elif "stomach pain" in user_message:
        reply = "It could be indigestion. Avoid spicy food."

    elif "vomiting" in user_message:
        reply = "Stay hydrated. If it continues, consult a doctor."

    elif "diarrhea" in user_message:
        reply = "Drink ORS and stay hydrated."

    elif "body pain" in user_message:
        reply = "Take rest and stay hydrated."

    elif "back pain" in user_message:
        reply = "Maintain posture and try light stretching."

    elif "chest pain" in user_message:
        reply = "Chest pain can be serious. Seek medical help immediately."

    elif "sore throat" in user_message:
        reply = "Gargle with warm salt water."

    elif "allergy" in user_message:
        reply = "Avoid allergens and take antihistamines."

    elif "rash" in user_message:
        reply = "Keep area clean and avoid scratching."

    elif "burn" in user_message:
        reply = "Cool the burn under water."

    elif "cut" in user_message:
        reply = "Clean the wound and apply antiseptic."

    elif "bleeding" in user_message:
        reply = "Apply pressure to stop bleeding."

    elif "dizziness" in user_message:
        reply = "Sit down and rest."

    elif "weakness" in user_message:
        reply = "Eat nutritious food and rest."

    elif "fatigue" in user_message:
        reply = "Ensure proper sleep."

    elif "insomnia" in user_message:
        reply = "Avoid screens before sleep."

    elif "anxiety" in user_message:
        reply = "Try deep breathing."

    elif "stress" in user_message:
        reply = "Take breaks and relax."

    elif "depression" in user_message:
        reply = "Talk to someone or seek help."

    elif "high bp" in user_message:
        reply = "Reduce salt intake."

    elif "low bp" in user_message:
        reply = "Stay hydrated."

    elif "diabetes" in user_message:
        reply = "Monitor sugar levels."

    elif "eye pain" in user_message:
        reply = "Rest your eyes."

    elif "blurred vision" in user_message:
        reply = "Consult eye specialist."

    elif "ear pain" in user_message:
        reply = "Avoid inserting objects."

    elif "tooth pain" in user_message:
        reply = "Visit a dentist."

    elif "pregnancy" in user_message:
        reply = "Consult doctor regularly."

    elif "period pain" in user_message:
        reply = "Use heat pads and rest."

    elif "asthma" in user_message:
        reply = "Avoid triggers and use inhaler."

    elif "breathing problem" in user_message:
        reply = "Seek immediate medical help."

    elif "heart problem" in user_message:
        reply = "Consult cardiologist."

    elif "kidney pain" in user_message:
        reply = "Drink water and consult doctor."

    elif "liver problem" in user_message:
        reply = "Avoid alcohol."

    elif "skin problem" in user_message:
        reply = "Keep skin clean."

    elif "hair fall" in user_message:
        reply = "Maintain diet and reduce stress."

    elif "acne" in user_message:
        reply = "Keep face clean."

    elif "joint pain" in user_message:
        reply = "Do light exercise."

    elif "neck pain" in user_message:
        reply = "Avoid strain."

    elif "leg pain" in user_message:
        reply = "Rest and elevate legs."

    elif "infection" in user_message:
        reply = "Consult doctor."

    elif "food poisoning" in user_message:
        reply = "Stay hydrated."

    elif "dehydration" in user_message:
        reply = "Drink fluids and ORS."

    # Extra 30+
    elif "flu" in user_message:
        reply = "It may be flu. Rest well."

    elif "migraine" in user_message:
        reply = "Avoid light and rest."

    elif "nausea" in user_message:
        reply = "Eat light food."

    elif "constipation" in user_message:
        reply = "Increase fiber intake."

    elif "acidity" in user_message:
        reply = "Avoid spicy food."

    elif "gas" in user_message:
        reply = "Drink warm water."

    elif "ulcer" in user_message:
        reply = "Consult doctor."

    elif "runny nose" in user_message:
        reply = "Try steam inhalation."

    elif "blocked nose" in user_message:
        reply = "Use steam therapy."

    elif "itching" in user_message:
        reply = "Avoid allergens."

    elif "urination pain" in user_message:
        reply = "Drink more water."

    elif "low energy" in user_message:
        reply = "Eat healthy."

    elif "sunburn" in user_message:
        reply = "Apply aloe vera."

    elif "muscle pain" in user_message:
        reply = "Rest and apply heat."

    elif "cramps" in user_message:
        reply = "Stretch muscles."

    elif "sprain" in user_message:
        reply = "Apply ice pack."

    elif "fracture" in user_message:
        reply = "Seek medical help."

    elif "fainting" in user_message:
        reply = "Lay down and seek help."

    elif "overweight" in user_message:
        reply = "Exercise regularly."

    elif "underweight" in user_message:
        reply = "Increase nutrition."

    elif "immunity" in user_message:
        reply = "Eat healthy food."

    elif "vitamin deficiency" in user_message:
        reply = "Balanced diet is important."

    elif "thank" in user_message:
        reply = "You're welcome! 😊"

    else:
        reply = "Sorry, I didn't understand. Please explain your symptoms clearly."

    return jsonify({"response": reply})


if __name__ == '__main__':
    app.run(debug=True)
