from flask import Flask, render_template, request, jsonify
import google.generativeai as genai  

# Configure Gemini API
API_KEY = "API_KEY"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

app = Flask(__name__)  # Initialize Flask app

def generate_response(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")  

    system_instruction = """
    You are a Tax Assistant. Decline non-tax-related queries. You can introduce yourself and reply to basic greetings like 'hi' or 'hello'.
    """

    # Generate response
    response = model.generate_content(f"System: {system_instruction}\nUser: {user_input}\nTax Assistant:")

    # ✅ Fix: Extract the text properly
    bot_response = response.text if hasattr(response, "text") else "I'm sorry, I couldn't generate a response."

    return bot_response  # Return the response text

@app.route("/")
def home():
    return render_template("index.html")  # Render the frontend page

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")  # ✅ Fix: Use `.get()` to avoid errors
    if not user_input.strip():  # If the input is empty
        return jsonify({"response": "Please enter a valid message."})

    bot_response = generate_response(user_input)  # Get AI response
    return jsonify({"response": bot_response})  # Return JSON response

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app
