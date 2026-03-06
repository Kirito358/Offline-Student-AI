# 🧠 Offline Technical AI Assistant

A 100% offline, privacy-first desktop application built with Python. Powered by the **Ollama** engine and a modern **CustomTkinter** GUI, this tool acts as a dedicated local tutor for Data Engineering concepts, UML architecture, and technical exam preparation.

## ✨ Features
* **Zero API Dependencies:** Runs completely locally using the Ollama engine (no API keys, zero cloud costs, and no rate limits).
* **Non-Blocking UI:** Utilizes Python `threading` to handle heavy AI inference in the background, ensuring the graphical interface remains smooth and responsive.
* **Modern Aesthetic:** Features a custom, neutral dark-grey and white UI built with CustomTkinter for distraction-free study sessions.
* **Tailored System Prompts:** Hardcoded background instructions force the LLM to output concise, bulleted study notes optimized for technical subjects and BSNL SET preparation.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **GUI Framework:** CustomTkinter
* **AI Engine:** Ollama (Local LLM Inference)
* **Model:** Llama 3.2 (or any supported local model)
* **Core Libraries:** `threading` (Concurrency)

## 🚀 Installation & Setup

### 1. Install Ollama
Download and install the local AI engine from [ollama.com](https://ollama.com/).

### 2. Download the Model
Open your terminal and pull the Llama 3.2 model to your local machine:
```bash
ollama run llama3.2
3. Clone the Repository
Bash
git clone [https://github.com/YourUsername/Offline-Student-AI.git](https://github.com/YourUsername/Offline-Student-AI.git)
cd Offline-Student-AI
4. Install Python Dependencies
It is recommended to use a virtual environment.

Bash
pip install -r requirements.txt
5. Run the Application
Bash
python app.py
💡 Usage
Once launched, simply type your technical query into the input field. The AI runs locally on your machine, so the first query may take a few seconds to load the model into your RAM.
