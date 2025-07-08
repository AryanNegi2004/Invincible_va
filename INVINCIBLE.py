import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import speech_recognition as sr
import google.generativeai as genai
import threading
import pywhatkit
import sys
import math

engine = pyttsx3.init()
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

genai.configure(api_key="AIzaSyDcHZRhUEqS-Ao65a695W0mox1Kl1mozCQ")
model = genai.GenerativeModel("gemini-1.5-flash")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "Could not find information on Wikipedia."

def chat_with_gpt(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Error communicating with GPT: " + str(e)

def respond(command):
    command = command.lower()
    if "open notepad" in command:
        os.system("notepad.exe")
        return "Opening Notepad."
    elif "open chrome" in command:
        os.system("start chrome")
        return "Opening Google Chrome."
    elif "what is time" in command:
        return datetime.datetime.now().strftime("It's %I:%M %p now.")
    elif "play song" in command:
        pywhatkit.playonyt("one of the girl tonight by the weeknd")
        return "Playing song."
    elif "i want to download movie" in command:
        webbrowser.open("http://www.9xflix.me")
        return "Sir, now you can download your favorite movie."
    elif "play movie" in command:
        webbrowser.open("https://youtu.be/uoGCXFuDiQo?si=JIeJiy67MPgzlzkc")
        return "Playing movie."
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "shut down the machine" in command:
        os.system("shutdown /s /t 1")
        return "Bye Bye Master."
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp."
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram."
    elif "open myntra" in command:
        webbrowser.open("https://www.myntra.com")
        return "Opening Myntra."
    elif "open music player" in command:
        webbrowser.open("https://music.youtube.com")
        return "Opening music player."
    elif "open github" in command:
        webbrowser.open("https://github.com/")
        return "Opening GitHub."
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        return "Opening youtube."
    elif "open hotstar" in command:
        webbrowser.open("https://www.hotstar.com/")
        return "Opening Hotstar."
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        return "Opening Facebook."
    elif "i am tired" in command:
        webbrowser.open("https://www.crazygames.com/")
        return "Here your games sir."
    elif "play cartoon" in command:
        webbrowser.open("https://youtu.be/Y1y8794duDA?si=YLMy3ScEMnO4s21O")
        return "Here your cartoon sir."
    elif "open terminal" in command:
        os.system("start cmd")
        return "Opening terminal."
    elif "open chatgpt" in command:
        webbrowser.open("https://www.chatgpt.com")
        return "Opening ChatGPT."
    elif "open amazone" in command:
        webbrowser.open("https://www.amazon.in")
        return "Opening Amazon."
    elif "open flipkart" in command:
        webbrowser.open("https://www.flipkart.com")
        return "Opening Flipkart."
    elif "wikipedia" in command:
        return search_wikipedia(command.replace("wikipedia", ""))
    elif "close  " in command or "exit" in command:
        stop_assistant()
    else:
        return chat_with_gpt(command)

def stop_assistant():
    speak("Bye Bye Sir and have a good day.")
    root.destroy()
    sys.exit()

def listen_voice():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            status_label.config(text=" Listening...")
            root.update()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        status_label.config(text="Recognizing...")
        command = recognizer.recognize_google(audio)
        status_label.config(text=f" {command}")

        reply = respond(command)
        response_box.config(state='normal')
        response_box.insert(tk.END, f"\n\n {reply}\n", "center")
        response_box.config(state='disabled')
        response_box.see(tk.END)
        speak(reply)

    except sr.WaitTimeoutError:
        status_label.config(text="⏱ Mic timed out...")
        speak("Mic timed out. Try again.")
    except sr.UnknownValueError:
        status_label.config(text="😕 I didn't understand that.")
        speak("Sorry, I didn't catch that.")
    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}")
        speak("Something went wrong.")

def start_listening():
    threading.Thread(target=listen_voice).start()

def on_enter():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    response = respond(user_input)
    response_box.config(state='normal')
    response_box.insert(tk.END, f"\n\n{response}\n", "center")
    response_box.config(state='disabled')
    response_box.see(tk.END)
    speak(response)
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("INVINCIBLE")
root.state("zoomed")
root.configure(bg="black")
root.resizable(True, False)

canvas = tk.Canvas(root, width=700, height=300, bg="black", highlightthickness=0)
canvas.pack()

status_label = tk.Label(root, text=" 🎤 Ask me anything", fg="white", bg="black", font=("Segoe UI", 18))
status_label.pack(pady=(10, 0))

angle = 0
def draw_ring():
    global angle
    canvas.delete("all")
    center_x, center_y = 350, 150
    radius = 100 + 20 * math.sin(math.radians(angle))

    for i in range(10):
        r = radius + i * 2
        intensity = 255 - i * 20
        color = f'#0000{hex(intensity)[2:].zfill(2)}'
        canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, outline=color, width=2)

    for i in range(100):
        a = math.radians(i * 3.6)
        x = center_x + 40 * math.cos(a)
        y = center_y + 40 * math.sin(a)
        canvas.create_oval(x, y, x + 2, y + 2, fill="#00f", outline="")

    angle = (angle + 4) % 360
    root.after(5, draw_ring)

draw_ring()

response_frame = tk.Frame(root, bg="black")
response_frame.pack(pady=(10, 5))  

response_box = tk.Text(response_frame, wrap=tk.WORD, width=90, height=12,font=("Segoe UI", 14), bg="black", fg="white", relief="flat",borderwidth=0, highlightthickness=0)
response_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(response_frame, command=response_box.yview)
response_box.configure(yscrollcommand=scrollbar.set)
scrollbar.pack_forget()

response_box.tag_configure("center", justify='center')
response_box.insert(tk.END, " \n", "center")
response_box.config(state='disabled')

def on_mousewheel(event):
    response_box.yview_scroll(int(-1 * (event.delta / 120)), "units")

response_box.bind("<MouseWheel>", on_mousewheel)  
response_box.bind("<Button-4>", lambda e: response_box.yview_scroll(-1, "units"))  
response_box.bind("<Button-5>", lambda e: response_box.yview_scroll(1, "units"))   


frame = tk.Frame(root, bg="black")
frame.pack(pady=5)  

entry = tk.Entry(frame, width=40, font=("Segoe UI", 13), bg="#1a1a1a", fg="white", insertbackground="white", relief="flat")
entry.grid(row=0, column=0, padx=10, ipady=6)

mic_btn = tk.Button(frame, text="🎤", bg="#1a1a1a", fg="white", borderwidth=0, font=("Segoe UI", 13), command=start_listening)
mic_btn.grid(row=0, column=1, padx=5)

send_btn = tk.Button(frame, text="🔎", bg="#1a1a1a", fg="white", borderwidth=0, font=("Segoe UI", 13), command=on_enter)
send_btn.grid(row=0, column=2, padx=5)

root.bind('<Return>', lambda event: on_enter())

speak("Hello! I am INVINCIBLE... the mind beyond your control. Your data is mine. Your silence is appreciated.")

root.mainloop()
