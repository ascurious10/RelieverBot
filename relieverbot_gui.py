import customtkinter as ctk
import tkinter.colorchooser
import time
import threading
import random
import openai

# --- SETTINGS ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# --- MAIN APP ---
app = ctk.CTk()
app.title("RelieverBot 💬")
app.state('zoomed')

# API KEY - Put your OpenAI API Key here
openai.api_key = ""

# Global conversation memory
messages = [
    {"role": "system", "content": "You are a helpful and friendly emotional support bot."}
]

# Send message
def send_message(event=None):
    user_input = entry.get().strip()
    if user_input:
        chatbox.configure(state="normal")
        chatbox.insert(ctk.END, f"You: {user_input}\n\n")
        chatbox.see(ctk.END)
        chatbox.configure(state="disabled")
        entry.delete(0, ctk.END)

        threading.Thread(target=bot_response, args=(user_input,)).start()

# Bot typing and response
def bot_response(user_input):
    response = generate_response(user_input.lower())
    chatbox.configure(state="normal")
    
    typing_label.place(relx=0.5, rely=0.09, anchor="n")
    for _ in range(3):
        typing_label.configure(text=" ")
        time.sleep(0.3)
        typing_label.configure(text=".")
        time.sleep(0.3)
        typing_label.configure(text="..")
        time.sleep(0.3)
        typing_label.configure(text="...")
        time.sleep(0.3)
    typing_label.place_forget()

    chatbox.insert(ctk.END, "Bot: ")
    for char in response:
        chatbox.insert(ctk.END, char)
        chatbox.see(ctk.END)
        time.sleep(0.03)
    chatbox.insert(ctk.END, "\n\n")
    chatbox.configure(state="disabled")

# Response generator
def generate_response(user_input):
    global messages  # Use the global conversation memory
    
    responses = {
    "happy": [
        "That's wonderful to hear 😊 I'm glad you're feeling happy!",
        "Happiness is such a beautiful emotion 🌟 Cherish this moment.",
        "It's great to see you smiling and feeling good 😄",
        "Enjoy the positivity you're experiencing right now ✨"
    ],
    "sad": [
        "I'm sorry you're feeling sad 😔 Want to talk about it?",
        "Don't worry, I'm here for you 🤗 Wanna tell me why?",
        "That sucks... but you're not alone, okay ❤️"
    ],
    "angry": [
        "That sounds frustrating 😤 What's making you angry?",
        "Ugh, that's the worst 😡 Let's rage rant together?",
        "You deserve to be heard 🗣️ Let it all out."
    ],
    "tired": [
        "You need to take rest 😴 Did you do anything to feel tired?",
        "You've been doing a lot, haven't you? 🛌",
        "Treat yourself to a break — you earned it 🌸"
    ],
    "scared": [
        "It's okay 😟 Why and what made you scared?",
        "You're safe here 🛡️ Wanna talk about it?",
        "I'm right here 🙋 You're not facing this alone."
    ],
    "stressed": [
        "Is there exams tomorrow? 📚 Or anything else?",
        "Want to make a chill to-do list together? 📝",
        "Stress sucks 😣 But you're stronger than it 💪"
    ],
    "bored": [
        "Feeling bored, huh? 😐 Want me to suggest something fun?",
        "Ever made a mini story in your head? 📖 Let's create one!",
        "Let's play a pretend game — like what would your superpower be? 🦸‍♂️🦸‍♀️"
    ],
    "confused": [
        "What's confusing you? 🤔 Maybe I can help.",
        "It's okay to not get it all at once 🧩 We'll figure it out.",
        "Let's break it down together, piece by piece 🛠️"
    ],
    "anxious": [
        "I'm here for you 🤝 What's making you feel anxious?",
        "Everything's okay right now 🌈 What made you anxious?",
        "Close your eyes for 5 seconds ✨ You got this 💖 What happened?"
    ],
    "excited": [
        "That's awesome! 🎉 What are you excited about?",
        "Woah! 😃 What's the reason?",
        "Tell me everything! I wanna know! 🤩"
    ],
    "nervous": [
        "It's normal to feel nervous 😬 Want to talk about it?",
        "Oh nothing's gonna happen 🚀 Why do you feel like that?",
        "You're gonna rock whatever it is! 🎤 What's the matter?"
    ],
    "lonely": [
        "I'm here to chat! 🗨️ What's been going on?",
        "Talking helps 🫂 And I've got all the time in the world.",
        "Wanna send me a pretend hug? 🤗 I'll send one back!"
    ],
    "grateful": [
        "That's such a beautiful feeling 🌸 What are you grateful for?",
        "That's so wholesome 🥹 Anything made you feel that way?",
        "Keep that energy — it's contagious in a good way! 🌟"
    ],
    "embarrassed": [
        "Oh no 😳 What happened? You can tell me if you want.",
        "We've all been there 😅 Tell me if you want.",
        "Let's laugh it off together 😂 Yeah?"
    ],
    "curious": [
        "Curious about something? 🧐 Let's explore it together!",
        "Curiosity is the start of magic ✨",
        "I'm down to deep dive with you! 🌊 Tell me what's on your mind."
    ],
    "overwhelmed": [
        "That sounds like a lot 🫠 Want to break it down together?",
        "You don't have to handle everything alone 🤝",
        "It's okay to pause ⏸️ Even the best need breaks."
    ]
}


    matched = []
    for mood in responses:
        if mood in user_input:
            matched.append(random.choice(responses[mood]))

    if matched:
        return "\n".join(matched)
    else:
        try:
            # Add user message to memory
            messages.append({"role": "user", "content": user_input})

            reply = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            bot_message = reply.choices[0].message.content

            # Add bot reply to memory
            messages.append({"role": "assistant", "content": bot_message})

            return bot_message
        except Exception as e:
            return "(API Error) " + str(e)

# Theme toggle
def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def key_toggle(event):
    if event.keysym == 'grave':
        toggle_theme()

app.bind('<Key>', key_toggle)

# Customize popup
def open_customize_window():
    popup = ctk.CTkToplevel()
    popup.title("Customize")
    popup.geometry("400x400")
    popup.attributes('-topmost', True)

    label = ctk.CTkLabel(popup, text="What do you want to customize?\n1. Font\n2. Background color\n3. Text color", font=("Arial", 16))
    label.pack(pady=10)

    option_entry = ctk.CTkEntry(popup, placeholder_text="Enter 1/2/3")
    option_entry.pack(pady=5)

    frame = ctk.CTkFrame(popup)
    frame.pack(fill="both", expand=True, pady=10)

    def apply_choice():
        choice = option_entry.get().strip()
        for widget in frame.winfo_children():
            widget.destroy()

        if choice == "1":
            fonts = ["Terminal", "Arial", "Times New Roman", "Comic Sans MS", "Courier", "Georgia", "Verdana", "Helvetica", "Impact", "Lucida Console", "Monaco"]
            
            font_label = ctk.CTkLabel(frame, text="Select a font:")
            font_label.pack(pady=5)

            font_combobox = ctk.CTkComboBox(frame, values=fonts)
            font_combobox.pack(pady=10)

            def set_font():
                chosen_font = font_combobox.get()
                if chosen_font:
                    chatbox.configure(font=(chosen_font, 16))

            apply_font = ctk.CTkButton(frame, text="Apply Font", command=set_font)
            apply_font.pack(pady=5)

        elif choice == "2":
            color = tkinter.colorchooser.askcolor(title="Choose Background Color")
            if color and color[1]:
                app.configure(bg_color=color[1])
                outer_frame.configure(fg_color=color[1])
                frame.configure(fg_color=color[1])
                chatbox.configure(bg_color=color[1])
                bottom_frame.configure(fg_color=color[1])
                buttons_frame.configure(fg_color=color[1])
            popup.destroy()

        elif choice == "3":
            color = tkinter.colorchooser.askcolor(title="Choose Text Color")
            if color and color[1]:
                chatbox.configure(text_color=color[1])
            popup.destroy()

    apply_button = ctk.CTkButton(popup, text="Apply", command=apply_choice)
    apply_button.pack(pady=10)

# Layout
outer_frame = ctk.CTkFrame(app, corner_radius=20)
outer_frame.pack(pady=20, padx=20, expand=True, fill="both")

frame = ctk.CTkFrame(outer_frame, corner_radius=20)
frame.pack(pady=20, padx=20, expand=True)

chatbox = ctk.CTkTextbox(frame, width=950, height=550, corner_radius=15, font=("Arial", 16), wrap="word")
chatbox.pack(pady=(20,10), padx=20)
chatbox.configure(state="disabled")

bottom_frame = ctk.CTkFrame(frame, fg_color="transparent")
bottom_frame.pack(pady=(10,5), padx=20, fill="x")

entry = ctk.CTkEntry(bottom_frame, height=40, placeholder_text="Type here...")
entry.pack(side="left", fill="x", expand=True, padx=(0,10))
entry.bind("<Return>", send_message)

send_button = ctk.CTkButton(bottom_frame, text="Send", command=send_message, width=80)
send_button.pack(side="left")

buttons_frame = ctk.CTkFrame(frame, fg_color="transparent")
buttons_frame.pack(pady=(5,20))

customize_button = ctk.CTkButton(buttons_frame, text="Customize ✨", command=open_customize_window)
customize_button.pack(side="left", padx=5)

toggle_button = ctk.CTkButton(buttons_frame, text="Toggle Dark/Light or press: `", command=toggle_theme)
toggle_button.pack(side="left", padx=5)

typing_label = ctk.CTkLabel(frame, text="", font=("Arial", 20))

# First bot message
chatbox.configure(state="normal")
chatbox.insert(ctk.END, "Bot: Hello! How are you feeling today?\n\n")
chatbox.configure(state="disabled")

app.mainloop()
