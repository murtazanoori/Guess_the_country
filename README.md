# 🌍 Guess The Country — Python Game

An interactive **Guess The Country** game built with **Python**, where players identify countries based on their **flags** under time pressure.

The game gets harder every round and tracks your **current score** and **highest score**, making it replayable and competitive.

---

## 🎮 Game Features

- 🏳️ Flag-based country guessing
- ⏱️ 10-second timer per round
- ❤️ 3 lives system (wrong answer or timeout = lose a life)
- 🎯 Multiple difficulty levels (gets harder each round)
- ⌨️ Keyboard-controlled answers (arrow keys + enter)
- 📊 Live score tracking
- 🏆 Highest score saved across sessions
- ❌ Game over screen with final stats

---

## 🕹️ How It Works

1. A country **flag** is displayed on screen.
2. You get **4 possible answers**.
3. Use your **keyboard arrow keys** to select an option.
4. Press **Enter** to confirm.
5. Answer correctly to gain points and move to the next round.
6. Answer wrong or run out of time → lose a life.
7. Lose all 3 lives → game over.

---

## 📦 Requirements

- Python 3.9+
- Pygame

Install dependencies:

```bash
pip install pygame
