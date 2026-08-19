#  Gesture Controlled Connect 4

A real-time **gesture-controlled Connect 4 game** built with Python, OpenCV, MediaPipe, Pygame, and NumPy.

Instead of using a mouse or keyboard, players control the game using their **hand movements**. Move your index finger to select a column, then bring your **thumb and index finger together** to drop a piece.

---

##  Features

-  Real-time hand tracking using MediaPipe
-  Index finger based column selection
-  Thumb + index finger pinch gesture to drop pieces
-  Two-player Connect 4 gameplay
- 🔴 Player 1 and 🟡 Player 2 pieces
-  Horizontal, vertical, and diagonal win detection
-  Restart the game using `R`
-  Smooth hand movement for better column selection
-  Transparent column selection indicator
-  Live webcam hand tracking
-  Real-time interaction using OpenCV and Pygame

---

##  How It Works

The game combines computer vision with traditional game logic.

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Detect Index Finger Position
   ↓
Select Connect 4 Column
   ↓
Thumb + Index Finger Touch
   ↓
Drop Game Piece
   ↓
Check Winning Condition
````

### Gesture Controls

| Gesture                | Action                  |
| ---------------------- | ----------------------- |
|  Move index finger   | Select a column         |
|  Thumb + index touch | Drop a piece            |
|  Separate fingers     | Reset pinch gesture     |
| `R`                    | Restart after game over |
| Window close           | Exit game               |

---

## 🛠️ Tech Stack

* **Python** — Core programming language
* **Pygame** — Game window, rendering, and interaction
* **OpenCV** — Webcam access and image processing
* **MediaPipe** — Real-time hand landmark detection
* **NumPy** — Connect 4 board representation and game state

---

## 📁 Project Structure

```text
Gesture_Controlled_Connect4/
│
├── assets/
│
├── game_logic.py
│
├── hand_tracking.py
│
├── main.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

### File Overview

**`main.py`**

Handles the main game loop, rendering, player turns, gestures, and game state.

**`hand_tracking.py`**

Uses OpenCV and MediaPipe to access the webcam and detect hand landmarks.

**`game_logic.py`**

Contains the Connect 4 game logic.

**`requirements.txt`**

Contains the Python dependencies required to run the project.

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gautami-04/Gesture_Controlled_Connect4.git
```

Move into the project:

```bash
cd Gesture_Controlled_Connect4
```

---

### 2. Create a virtual environment

It is recommended to use **Python 3.11** for this project.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the game

```bash
python main.py
```

Allow the application to access your webcam when prompted.

---

##  Gameplay

Once the game starts:

1. Show your hand to the webcam.
2. Move your index finger horizontally.
3. The corresponding Connect 4 column will be highlighted.
4. Bring your thumb and index finger together.
5. A game piece will be placed in the selected column.
6. Separate your fingers before making the next move.
7. Players alternate turns.
8. The game ends when a player connects four pieces.

---

##  Computer Vision

The project uses **MediaPipe Hands** to detect hand landmarks from the webcam.

The important landmarks used for interaction are:

* **Index finger tip** — landmark `8`
* **Thumb tip** — landmark `4`

The index finger's horizontal position is converted into a Connect 4 column:

```text
Camera X Position
       ↓
Normalize X Position
       ↓
Map to 7 Columns
       ↓
Selected Column
```

The distance between the thumb tip and index finger tip is used to detect the pinch gesture.

---

##  Win Detection

The game checks for four connected pieces in four directions:

### Horizontal

```text
🔴 🔴 🔴 🔴
```

### Vertical

```text
🔴
🔴
🔴
🔴
```

### Diagonal

```text
🔴
   🔴
      🔴
         🔴
```

A player wins as soon as four pieces are connected in any of these directions.

---

## 🔮 Future Improvements

Possible improvements for future versions:

*  Animated piece dropping
* 🔊 Sound effects
* ✨ Piece and board animations
* 🏠 Start/menu screen
* 🏆 Improved winner screen
* 🤖 AI opponent
* 📊 Score tracking
* 👥 Online multiplayer
* 📱 Browser/mobile version
* 🌐 Web-based deployment using JavaScript and MediaPipe
* 🎨 More advanced UI and visual effects

---

## 📸 Demo

> Add a gameplay GIF or video here.

For example:

```markdown
![Gesture Connect 4 Demo](assets/demo.gif)
```

A good demo should show:

**Hand movement → column selection → pinch gesture → piece drop → winning move**

---

## 💡 What I Learned

This project helped me explore:

* Computer vision
* Hand landmark detection
* Gesture recognition
* Real-time webcam processing
* Human-computer interaction
* Game state management
* Event-driven programming
* Combining computer vision with game development

The main challenge was making gesture input feel intentional rather than triggering actions from small accidental movements. This led to using pinch detection and cooldown/state logic to distinguish deliberate gestures from normal hand movement.

---

## 👩‍💻 Author

**Gautami**

Built as a hands-on project exploring **Computer Vision, Gesture Recognition, and Interactive Systems**.

---

## ⭐ If You Like This Project

Feel free to ⭐ the repository and explore the code!

```

### One important change before you commit it

Your README currently claims `game_logic.py` contains the game logic. **Make sure that's actually true in your current code.** If your `main.py` currently contains `drop_piece()` and `check_winner()` while `game_logic.py` is unused, we should clean that architecture up before presenting the repo publicly.

Also, once you have a gameplay recording, put it in `assets/demo.gif` and replace the demo placeholder. **A GIF of you moving your hand and dropping the pieces will make this README much stronger.**
```
