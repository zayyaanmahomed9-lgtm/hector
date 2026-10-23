from fastapi import FastAPI
import pyttsx3

app = FastAPI()

# Initialize Voice Synthesis for HECTOR
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Speaking speed

def speak(text: str):
    print(f"HECTOR: {text}")
    engine.say(text)
    engine.runAndWait()

@app.get("/")
def home():
    return {"status": "HECTOR Core Systems Online"}

@app.post("/ask")
def process_voice(prompt: str):
    print(f"Received from user: {prompt}")
    reply = f"Online and operational, sir. You said: '{prompt}'."
    
    # Make HECTOR speak out loud on your PC speakers!
    speak(reply)
    
    return {"response": reply}

if __name__ == "__main__":
    import uvicorn
    print("HECTOR initialization complete. Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)