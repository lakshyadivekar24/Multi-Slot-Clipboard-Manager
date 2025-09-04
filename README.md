# 📝 Multi-Slot Clipboard Manager

Tired of copying and pasting one thing at a time?  
With the **Multi-Slot Clipboard Manager**, you can save multiple clipboard entries (up to 9) and recall them anytime with simple keyboard shortcuts. 🚀  

---

## ✨ Features
- 📋 **Multi-slot clipboard** → Save up to 9 different text entries.  
- ⚡ **Quick access** → Use simple hotkeys to store and paste.  
- 💻 **Cross-platform design** → Works on macOS (tested) and adaptable for Windows/Linux.  
- 🔔 **Terminal feedback** → Shows what’s saved/pasted in real-time.  

---

## 🎮 Usage
### On macOS:
- **Save to slot:**  
  Press `Cmd + C + <num>` → saves current copied text into slot `<num>`  
  Example: `Cmd + C + 1` → Saves clipboard into Slot 1  

- **Paste from slot:**  
  Press `Ctrl + <num>` → sets slot `<num>` back into clipboard  
  Then press `Cmd + V` normally to paste.  

---

## 🔮 Future Enhancements
- 🔔 **Native notifications** → Show popup alerts when text is saved/pasted to slots.  
- 🪟 **Direct auto-paste (Windows)** → Simulate `Ctrl+V` automatically after recalling slot.  
- 🎨 **GUI manager** → A small window to view, edit, and manage all slots visually.  
- ⚙️ **Auto-start on boot** → Make the clipboard manager run automatically when your PC starts, so you don’t need to manually launch it every time.  
- ☁️ **Cloud sync (optional)** → Sync clipboard slots across devices.
- 

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-clipboard.git
   cd multi-clipboard


2. Create Virtual Enviroment :
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run the app:
   ```bash
   python main.py

## 🖥️ Demo

1. Save multiple lines:
   
    Cmd+C+1 → "Hello World" saved to Slot 1
    Cmd+C+2 → "Multi-slot clipboard" saved to Slot 2

2. Recall and paste:
   
   Ctrl+1 → "Hello World" ready to paste
   Ctrl+2 → "Multi-slot clipboard" ready to paste
