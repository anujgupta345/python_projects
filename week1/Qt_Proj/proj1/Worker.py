from PySide6.QtCore import (QObject, Signal, QThread, Slot)
#AI imports
import os
from dotenv import load_dotenv
from openai import OpenAI

class Worker(QThread):
    responseGenerated = Signal(str)
    finished = Signal(str)

    def __init__(self, message, role="user"):
        super().__init__()
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.message = message
        self.role = role
    
    def getDict(self, role, content):
        return {"role":role, "content": content}
    
    @Slot()
    def run(self):
        print(f"run: { QThread.currentThread()}")
        print(f"message: { self.message}")
        print(f"role: { self.role}")
        response = self.client.chat.completions.create(model = "gpt-4o-mini", messages=[self.getDict(self.role, self.message)])
        print(response.choices[0].message.content)
        self.responseGenerated.emit(response.choices[0].message.content)
        print("emitted signal")
        self.finished.emit("done")