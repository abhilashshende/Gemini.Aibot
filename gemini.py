import google.generativeai as genai 

API_KEY = "AIzaSyB6hT-5zjN4_wBMvs7PhBe2Ybe9n2Hr8bk"
genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()

    print("Chat with Gemini! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

except Exception as e:
    print("Error:", e)
