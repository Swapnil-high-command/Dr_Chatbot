from flask import Flask, request, jsonify, render_template
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
print("API KEY:", os.getenv("GROQ_API_KEY"))

app = Flask(__name__)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

prompt = PromptTemplate(
    input_variables=["message"],
    template="""You are Medi-Bot, a helpful medical assistant. 
Answer the following health-related query briefly and clearly.
If it is an emergency, advise the user to seek immediate medical help.
Query: {message}"""
)

chain = prompt | llm


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        response = chain.invoke({"message": user_message})
        return jsonify({"response": response.content})
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"response": str(e)}), 200


if __name__ == '__main__':
    app.run(debug=True)
