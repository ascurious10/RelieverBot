import customtkinter as ctk

# Setup
ctk.set_appearance_mode("System")  # or "Dark" or "Light"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x800")
app.title("Reliever Bot 💬")

# The chat container (main rounded box)
chat_frame = ctk.CTkFrame(app, width=600, height=600, corner_radius=20)
chat_frame.pack(pady=40)
chat_frame.pack_propagate(False)  # allow manual control of size

# Inside the box: this will hold messages
message_area = ctk.CTkScrollableFrame(chat_frame, width=580, height=580, corner_radius=20)
message_area.pack(pady=10, padx=10, fill="both", expand=True)

# Function to add messages
def add_message(text, sender="bot"):
    msg_frame = ctk.CTkFrame(message_area, fg_color="transparent")  # transparent background
    msg_frame.pack(fill="x", pady=5)

    if sender == "user":
        msg_label = ctk.CTkLabel(
            msg_frame, text=text,
            font=("Helvetica", 16),
            anchor="e",  # align to right inside frame
            justify="right",
            wraplength=400
        )
        msg_label.pack(anchor="e", padx=10)
    else:
        msg_label = ctk.CTkLabel(
            msg_frame, text=text,
            font=("Helvetica", 16),
            anchor="w",  # align to left inside frame
            justify="left",
            wraplength=400
        )
        msg_label.pack(anchor="w", padx=10)

# Entry box to type message
entry = ctk.CTkEntry(app, placeholder_text="Type your message...", width=500, height=40, corner_radius=20)
entry.pack(pady=10)

# Send button
def send_message():
    user_text = entry.get()
    if user_text.strip() != "":
        add_message(user_text, sender="user")
        entry.delete(0, ctk.END)
        
        # Example: bot reply (you can later replace with real AI)
        bot_reply = "You said: " + user_text
        add_message(bot_reply, sender="bot")

send_btn = ctk.CTkButton(app, text="Send", command=send_message, width=100, height=40, corner_radius=20)
send_btn.pack()

# Allow pressing "Enter" key
def on_enter(event):
    send_message()

entry.bind("<Return>", on_enter)

# Start
app.mainloop()
