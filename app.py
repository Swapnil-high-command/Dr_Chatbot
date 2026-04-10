from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')   # make sure file is in templates folder

# Chat API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    
if "hello" in user_message or "hi" in user_message:
        reply = "Hello! I am Medi-Bot. How can I help you?"
    
elif "stomach pain" in user_message:
    reply = "It could be due to indigestion. Avoid spicy food and rest."

elif "vomiting" in user_message:
    reply = "Stay hydrated. If vomiting continues, consult a doctor."

elif "diarrhea" in user_message:
    reply = "Drink ORS and stay hydrated. Seek medical help if severe."

elif "body pain" in user_message:
    reply = "Take rest and stay hydrated. Mild pain relievers may help."

elif "back pain" in user_message:
    reply = "Maintain good posture and try light stretching."

elif "chest pain" in user_message:
    reply = "Chest pain can be serious. Seek medical help immediately."

elif "sore throat" in user_message:
    reply = "Gargle with warm salt water and drink warm fluids."

elif "allergy" in user_message:
    reply = "Avoid allergens and consider antihistamines."

elif "rash" in user_message:
    reply = "Keep the area clean and avoid scratching."

elif "burn" in user_message:
    reply = "Cool the burn under running water and avoid applying ice."

elif "cut" in user_message:
    reply = "Clean the wound and apply antiseptic."

elif "bleeding" in user_message:
    reply = "Apply pressure to stop bleeding and seek help if needed."

elif "dizziness" in user_message:
    reply = "Sit down and rest. Stay hydrated."

elif "weakness" in user_message:
    reply = "Eat nutritious food and get enough rest."

elif "fatigue" in user_message:
    reply = "Ensure proper sleep and balanced diet."

elif "insomnia" in user_message:
    reply = "Avoid screens before bed and maintain a sleep routine."

elif "anxiety" in user_message:
    reply = "Try deep breathing and relaxation techniques."

elif "stress" in user_message:
    reply = "Take breaks and practice meditation."

elif "depression" in user_message:
    reply = "Consider talking to a professional or trusted person."

elif "high bp" in user_message or "hypertension" in user_message:
    reply = "Reduce salt intake and monitor your BP regularly."

elif "low bp" in user_message:
    reply = "Stay hydrated and eat small frequent meals."

elif "diabetes" in user_message:
    reply = "Monitor sugar levels and maintain a healthy diet."

elif "weight loss" in user_message:
    reply = "Maintain balanced diet and consult a nutritionist."

elif "weight gain" in user_message:
    reply = "Exercise regularly and follow a healthy diet."

elif "eye pain" in user_message:
    reply = "Rest your eyes and avoid screen exposure."

elif "blurred vision" in user_message:
    reply = "Consult an eye specialist."

elif "ear pain" in user_message:
    reply = "Avoid inserting objects and consult a doctor if severe."

elif "tooth pain" in user_message:
    reply = "Maintain oral hygiene and visit a dentist."

elif "gum pain" in user_message:
    reply = "Use salt water rinse and maintain oral care."

elif "pregnancy" in user_message:
    reply = "Consult a doctor for proper guidance and care."

elif "period pain" in user_message:
    reply = "Use heat pads and rest."

elif "pcos" in user_message:
    reply = "Maintain healthy lifestyle and consult doctor."

elif "thyroid" in user_message:
    reply = "Regular checkups and medication are important."

elif "asthma" in user_message:
    reply = "Avoid triggers and carry inhaler."

elif "breathing problem" in user_message:
    reply = "Seek immediate medical help if severe."

elif "heart problem" in user_message:
    reply = "Consult a cardiologist immediately."

elif "kidney pain" in user_message:
    reply = "Drink water and consult doctor."

elif "liver problem" in user_message:
    reply = "Avoid alcohol and fatty food."

elif "skin problem" in user_message:
    reply = "Keep skin clean and hydrated."

elif "hair fall" in user_message:
    reply = "Maintain good diet and reduce stress."

elif "acne" in user_message:
    reply = "Keep face clean and avoid oily products."

elif "feeling cold" in user_message:
    reply = "Wear warm clothes and rest."

elif "feeling hot" in user_message:
    reply = "Stay hydrated and cool."

elif "joint pain" in user_message:
    reply = "Do light exercise and maintain posture."

elif "neck pain" in user_message:
    reply = "Avoid strain and use proper support."

elif "leg pain" in user_message:
    reply = "Rest and elevate your legs."

elif "hand pain" in user_message:
    reply = "Avoid overuse and rest."

elif "infection" in user_message:
    reply = "Consult doctor for proper treatment."

elif "food poisoning" in user_message:
    reply = "Stay hydrated and avoid solid food temporarily."

elif "dehydration" in user_message:
    reply = "Drink plenty of fluids and ORS."

elif "thank you" in user_message:
    reply = "You're welcome! Stay healthy 😊"

# Run server
if __name__ == '__main__':
    app.run(debug=True)