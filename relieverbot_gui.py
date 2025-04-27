import customtkinter as ctk
from tkinter import colorchooser  # Standard tkinter color picker
import time
import threading
import random

# Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main App
app = ctk.CTk()
app.title("RelieverBot 💬")
app.state('zoomed')

current_font = ("Arial", 16)  # default font
current_text_color = "white"
current_bg_color = "#2b2b2b"

# Send message function
def send_message(event=None):
    user_input = entry.get().strip()
    if user_input:
        chatbox.configure(state="normal")
        chatbox.insert(ctk.END, f"You: {user_input}\n")
        chatbox.see(ctk.END)
        chatbox.configure(state="disabled")
        entry.delete(0, ctk.END)

        threading.Thread(target=bot_response, args=(user_input,)).start()

# Typing animation
def bot_response(user_input):
    response = generate_response(user_input.lower())
    chatbox.configure(state="normal")
    
    # Typing animation
    typing_label.place(relx=0.5, rely=0.9, anchor="s")
    for _ in range(3):
        typing_label.configure(text=".")
        time.sleep(0.3)
        typing_label.configure(text="..")
        time.sleep(0.3)
        typing_label.configure(text="...")
        time.sleep(0.3)
    typing_label.place_forget()

    # Show bot's response
    chatbox.insert(ctk.END, "Bot: ", ("bot",))
    for char in response:
        chatbox.insert(ctk.END, char, ("bot",))
        chatbox.see(ctk.END)
        time.sleep(0.03)
    chatbox.insert(ctk.END, "\n\n", ("bot",))
    chatbox.configure(state="disabled")

# Responses
def generate_response(mood):
    responses = {
        "happy": ["That's wonderful to hear. I'm glad you're feeling happy.",
                  "Happiness is such a beautiful emotion. Cherish this moment.",
                  "It's great to see you smiling and feeling good.",
                  "Enjoy the positivity you're experiencing right now."],
        "sad": ["I'm sorry you're feeling sad. Want to talk about it?", 
                "Don't worry, I'm here for you. Wanna tell me why?", 
                "That sucks... but you're not alone, okay?"],
        "angry": ["That sounds frustrating. What's making you angry?", 
                  "Ugh, that's the worst. Let's rage rant together?", 
                  "You deserve to be heard. Let it all out."],
        "tired": ["You need to take rest. Did you do anything to feel tired?", 
                  "You've been doing a lot, haven't you?", 
                  "Treat yourself to a break — you earned it."],
        "scared": ["It's okay. Why and what made you to be scared?", 
                   "You're safe here. Wanna talk about it?", 
                   "I'm right here. You're not facing this alone. Tell me why."],
        "stressed": ["Is there exams tomorrow? Or anything else?", 
                     "Want to make a chill to-do list together?", 
                     "Stress sucks. But you're stronger than it. Right?"],
        "bored": ["Feeling bored, huh? Want me to suggest something fun?", 
                  "Ever made a mini story in your head? Let's create one!", 
                  "Let's play a pretend game — like what would your superpower be?"],
        "confused": ["What's confusing you? Maybe I can help.", 
                     "It's okay to not get it all at once. We'll figure it out.", 
                     "Let's break it down together, piece by piece."],
        "anxious": ["I'm here for you. What's making you feel anxious?", 
                    "Everything's okay right now. What made you to be anxious?", 
                    "Close your eyes for 5 seconds. You got this. What happened?"],
        "excited": ["That's awesome! What are you excited about?", 
                    "Woah! What's the reason?", 
                    "Tell me everything! I wanna know!"],
        "nervous": ["It's normal to feel nervous. Want to talk about it?", 
                    "Oh nothing's gonna happen. Why do you feel like that?", 
                    "You're gonna rock whatever it is. What's the matter?"],
        "lonely": ["I'm here to chat! What's been going on?", 
                   "Talking helps. And I've got all the time.", 
                   "Wanna send me a pretend hug? I'll send one back 🤗"],
        "grateful": ["That's such a beautiful feeling. What are you grateful for?", 
                     "That's so wholesome 🥹. Anything made you like that?", 
                     "Keep that energy — it's contagious in a good way!"],
        "embarrassed": ["Oh no, what happened? You can tell me if you want.", 
                        "We've all been there. Tell me if you want.", 
                        "Let's laugh it off together, yeah?"],
        "curious": ["Curious about something? Let's explore it together!", 
                    "Curiosity is the start of magic ✨", 
                    "I'm down to deep dive with you! Tell me what's on your mind."],
        "overwhelmed": ["That sounds like a lot. Want to break it down together?", 
                        "You don't have to handle everything alone.", 
                        "It's okay to pause. Even the best need breaks."]
    }
    return random.choice(responses.get(mood, ["I'm here for you. Feel free to share whatever is on your mind."]))

# Dark mode toggle
def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def key_toggle(event):
    if event.keysym == '`':
        toggle_theme()

app.bind('<Key>', key_toggle)

# Customization function
def start_customization():
    # Clear old widgets if any
    for widget in customize_frame.winfo_children():
        widget.destroy()
    
    instruction_label = ctk.CTkLabel(customize_frame, text="What do you want to customize?\n1. Font\n2. Colour of the text\n3. Background colour\nEnter your choice (1/2/3):", font=("Arial", 18))
    instruction_label.pack(pady=(10,5))
    
    choice_entry = ctk.CTkEntry(customize_frame, placeholder_text="Type 1 / 2 / 3 here...")
    choice_entry.pack(pady=(5,10))
    
    def handle_choice(event=None):
        choice = choice_entry.get().strip()
        if choice == "1":
            show_fonts()
        elif choice == "2":
            choose_text_color()
        elif choice == "3":
            choose_background_color()
        else:
            instruction_label.configure(text="Invalid choice. Please type 1, 2, or 3.")

    choice_entry.bind("<Return>", handle_choice)

def show_fonts():
    for widget in customize_frame.winfo_children():
        widget.destroy()
    
    fonts = ["Arial", "Terminal", "Comic Sans MS", "Courier", "Times New Roman", "Verdana", "Helvetica", "Impact"]
    font_list_label = ctk.CTkLabel(customize_frame, text="Choose a font from below:", font=("Arial", 18))
    font_list_label.pack(pady=(10,5))
    
    fonts_text = "\n".join(fonts)
    fonts_display = ctk.CTkLabel(customize_frame, text=fonts_text, font=("Arial", 16))
    fonts_display.pack(pady=(5,10))
    
    font_entry = ctk.CTkEntry(customize_frame, placeholder_text="Type font name here...")
    font_entry.pack(pady=(5,10))
    
    def apply_font(event=None):
        global current_font
        selected_font = font_entry.get().strip().lower()
        for font in fonts:
            if font.lower() == selected_font:
                current_font = (font, 16)
                chatbox.configure(font=current_font)
                return
        font_list_label.configure(text="Font not found. Please try again.")
    
    font_entry.bind("<Return>", apply_font)

def choose_text_color():
    color = colorchooser.askcolor(title="Pick a Text Color")[1]
    if color:
        chatbox.tag_config("bot", foreground=color)

def choose_background_color():
    color = colorchooser.askcolor(title="Pick a Background Color")[1]
    if color:
        chatbox.configure(fg_color=color)

# Layout
outer_frame = ctk.CTkFrame(app, corner_radius=20)
outer_frame.pack(pady=20, padx=20, expand=True, fill="both")

frame = ctk.CTkFrame(outer_frame, corner_radius=20)
frame.pack(pady=20, padx=20, expand=True)

chatbox = ctk.CTkTextbox(frame, width=950, height=550, corner_radius=15, font=current_font, wrap="word")
chatbox.pack(pady=(20,10), padx=20)
chatbox.configure(state="disabled")

bottom_frame = ctk.CTkFrame(frame, fg_color="transparent")
bottom_frame.pack(pady=(10,5), padx=20, fill="x")

entry = ctk.CTkEntry(bottom_frame, height=40, placeholder_text="Type here...")
entry.pack(side="left", fill="x", expand=True, padx=(0,10))
entry.bind("<Return>", send_message)

send_button = ctk.CTkButton(bottom_frame, text="Send", command=send_message, width=80)
send_button.pack(side="left")

customize_frame = ctk.CTkFrame(frame, fg_color="transparent")
customize_frame.pack()

customize_button = ctk.CTkButton(frame, text="Customize ✨", command=start_customization)
customize_button.pack(pady=(5,5))

theme_button = ctk.CTkButton(frame, text="Toggle Dark/Light (`)", command=toggle_theme)
theme_button.pack(pady=(5,20))

typing_label = ctk.CTkLabel(frame, text="", font=("Arial", 20))

# Initial bot message
chatbox.configure(state="normal")
chatbox.insert(ctk.END, "Bot: Hi. How are you feeling today?\n\n", ("bot",))
chatbox.configure(state="disabled")

app.mainloop()
