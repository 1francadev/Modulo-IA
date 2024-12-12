import google.generativeai as ai
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

API_KEY = "AIzaSyBwk3AMGSdz2CYr-J_0J4dWkwlkZX7Mq80"
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel('models/gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if not user_message:
        messagebox.showwarning("Aviso", "Por favor, digite uma mensagem antes de enviar.")
        return

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Você: {user_message}\n")
    chat_display.config(state=tk.DISABLED)
    user_input.delete("1.0", tk.END)

    try:
        response = chat.send_message(user_message)
        chat_display.config(state=tk.NORMAL)
        if response.text:
            chat_display.insert(tk.END, f"Chatbot: {response.text}\n")
        else:
            chat_display.insert(tk.END, "Chatbot: Algo deu errado. Tente novamente.\n")
        chat_display.config(state=tk.DISABLED)
    except Exception as e:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"Erro: {e}\n")
        chat_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Chatbot com Google Generative AI")
root.geometry("1024x768")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

chat_label = tk.Label(root, text="Histórico do Chat:", font=("Arial", 12), bg="#f0f0f0")
chat_label.pack(pady=5)

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state=tk.DISABLED, font=("Arial", 10))
chat_display.pack(pady=10)

input_label = tk.Label(root, text="Digite sua mensagem:", font=("Arial", 12), bg="#f0f0f0")
input_label.pack(pady=5)

user_input = tk.Text(root, wrap=tk.WORD, height=5, width=70, font=("Arial", 10))
user_input.pack(pady=10)

send_button = tk.Button(root, text="Enviar", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=5)
send_button.pack(pady=10)

root.mainloop()
