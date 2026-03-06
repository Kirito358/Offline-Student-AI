import customtkinter as ctk
import ollama
import threading

class OfflineStudentAssistant(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Bot |  Local AI")
        self.geometry("850x650")
        ctk.set_appearance_mode("dark")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Chat Frame
        self.chat_frame = ctk.CTkFrame(self, corner_radius=10)
        self.chat_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.chat_frame.grid_rowconfigure(0, weight=1)
        self.chat_frame.grid_columnconfigure(0, weight=1)

        # Display Area
        self.display = ctk.CTkTextbox(self.chat_frame, font=("Segoe UI", 15), wrap="word")
        self.display.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.display.configure(state="disabled")

        # Input Frame
        self.input_area = ctk.CTkFrame(self.chat_frame, fg_color="transparent")
        self.input_area.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
        self.input_area.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self.input_area, 
            placeholder_text="Ask Me About Your Studies...", 
            height=45
        )
        self.entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.entry.bind("<Return>", lambda e: self.handle_send())

        self.btn_send = ctk.CTkButton(self.input_area, text="Send", width=90, height=45, fg_color="#34a853", command=self.handle_send)
        self.btn_send.grid(row=0, column=1)

        self.append_chat("Chat Bot", "Ready!")

    def append_chat(self, sender, msg):
        self.display.configure(state="normal")
        self.display.insert("end", f"\n{sender}:\n{msg}\n\n")
        self.display.configure(state="disabled")
        self.display.see("end")

    def handle_send(self):
        prompt = self.entry.get()
        if not prompt.strip(): return
        
        self.append_chat("You", prompt)
        self.entry.delete(0, 'end')
        
        self.btn_send.configure(state="disabled", text="Thinking...")
        
        # Run AI in the background so the UI doesn't freeze
        threading.Thread(target=self.generate_response, args=(prompt,), daemon=True).start()

    def generate_response(self, prompt):
        try:
            # Talking to your local Ollama engine
            response = ollama.chat(model='llama3.2', messages=[
                {
                    'role': 'system',
                    'content': 'You are a Data Engineering  Keep answers concise with bullet points.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            ai_text = response['message']['content']
            
            # Update UI back on the main thread
            self.after(0, self.append_chat, "Local AI", ai_text)
        except Exception as e:
            self.after(0, self.append_chat, "System Error", f"Make sure Ollama is running! Error: {e}")
        finally:
            self.after(0, lambda: self.btn_send.configure(state="normal", text="Send"))

if __name__ == "__main__":
    app = OfflineStudentAssistant()
    app.mainloop()