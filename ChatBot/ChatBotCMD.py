import google.generativeai as ai

API_KEY = "AIzaSyBwk3AMGSdz2CYr-J_0J4dWkwlkZX7Mq80"

ai.configure(api_key=API_KEY)
model = ai.GenerativeModel('models/gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

while True:
    messageUser = input("Você: ")
    if messageUser == 'sair' or messageUser == 'exit' or messageUser == 'exit':
        break
    else:
        resposta = chat.send_message(messageUser)
        if resposta.text:
            print("Chatbot: ", resposta.text)
        else:
            print("Possivel erro, dá uma olhada ai truta: ", resposta)