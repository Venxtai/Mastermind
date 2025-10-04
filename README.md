# 🎮 Mastermind Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**A classic color-based code-breaking game built in Python with intelligent feedback system**

[About](#-about) • [Installation](#-installation) • [How to Play](#-how-to-play) • [Features](#-features)

</div>

---

## 🎯 About

Mastermind is an interactive command-line game where players attempt to crack a secret 4-color code within 10 guesses. The game provides strategic feedback after each guess, indicating correct positions and correct colors in wrong positions. Built with Python's random module and featuring robust input validation.

## ✨ Features

<table>
<tr>
<td>

### Gameplay
- 🎨 **6 Color Options** - Red, Orange, Yellow, Green, Blue, Purple
- 🔢 **4-Color Code** - Random code generation each game
- 🎯 **10 Attempts** - Strategic guessing with limited tries
- 💡 **Smart Feedback** - Clues for correct colors and positions
- 🔄 **Replay Option** - Play multiple rounds seamlessly

</td>
<td>

### Technical
- ✅ **Input Validation** - Handles invalid entries gracefully
- 🛡️ **Error Handling** - Try-except blocks for robustness
- 🎲 **Seeded Random** - Reproducible results for testing
- 📊 **Pattern Matching** - Advanced guess evaluation algorithm
- 🧩 **Modular Design** - Clean function-based architecture

</td>
</tr>
</table>

## 🚀 Installation

### Prerequisites
```bash
# Requires Python 3.6 or later
python --version
```

### Quick Start

**Clone & Run:**
```bash
# Clone the repository
git clone https://github.com/yourusername/mastermind-game.git
cd mastermind-game

# Run the game
python mastermind.py
```

**Or download and run directly:**
```bash
python mastermind.py
```

## 🎮 How to Play

### Game Rules

1. **Objective:** Guess the secret 4-color code within 10 attempts
2. **Color Options:** Choose from 6 colors (numbered 0-5)
3. **Feedback System:**
   - `2` = Correct color in correct position
   - `1` = Correct color in wrong position
4. **Win Condition:** Get all four colors in the correct positions `[2, 2, 2, 2]`

### Example Gameplay

```
The secret code has been chosen. You have 10 tries to guess the code.
-----------------------------
Make a guess of four colors:
0 - red
1 - orange
2 - yellow
3 - green
4 - blue
5 - purple
-----------------------------
Guess color: 0
Guess color: 1
Guess color: 2
Guess color: 3
-----------------------------
Your guess is:
['red', 'orange', 'yellow', 'green']

Your clue is: [1, 2]
You have 9 guesses left
```

### Understanding Clues

| Clue | Meaning | Example |
|------|---------|---------|
| `[2, 2, 2, 2]` | All correct - You win! | Code: `[red, blue, green, yellow]`<br>Guess: `[red, blue, green, yellow]` ✅ |
| `[2, 2, 1, 1]` | 2 correct positions, 2 correct colors wrong positions | Code: `[red, blue, green, yellow]`<br>Guess: `[red, blue, yellow, green]` |
| `[1, 1, 1]` | 3 correct colors, all in wrong positions | Code: `[red, blue, green, yellow]`<br>Guess: `[blue, yellow, red, orange]` |
| `[]` | No correct colors | Code: `[red, blue, green, yellow]`<br>Guess: `[orange, purple, orange, purple]` ❌ |

## 🔧 Technical Implementation

### Architecture

```python
┌──────────────────────────────┐
│      Main Game Loop          │
├──────────────────────────────┤
│  generateCode()              │  → Creates random 4-color code
│  getGuess()                  │  → Gets player input with validation
│  CheckGuess(guess, code)     │  → Evaluates guess & returns clues
│  main(seedValue)             │  → Controls game flow & replay logic
└──────────────────────────────┘
```

### Key Functions

**🔵 generateCode()**
```python
# Generates a random 4-color code
# Uses random.randint() for index selection
# Returns: List of 4 color strings
```

**🔵 getGuess()**
```python
# Prompts player for 4 color choices (0-5)
# Validates input with try-except blocks
# Handles both invalid numbers and non-numeric input
# Returns: List of 4 color strings
```

**🔵 CheckGuess(guess, co
