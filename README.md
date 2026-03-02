# 🎮 Game Glitch Investigator: The Impossible Guesser

### TF Notes after completing this Show activity

BUGS I FOUND:
1. The hints were backwards (said guess higher when the secret number was lower and vice versa) (CAUSE: logic is flipped in code)
2. The difficulties don't seem to match (easy should have lowest range and hard should have greatest range) (CAUSE: ranges set incorrectly in code)
3. After winning, if you click new game, it resets the number but won't let you guess anymore (CAUSE: status is not reset to "playing")
4. The random number could be outside the range shown based on difficulty (CAUSE: random number's range is always 1-100)

Used GitHub Copilot to fix bugs 1 and 4 above, as well as refactor so that check_guess and parse_guess were moved into logic_utils.py

A guiding hint I would give a student:
As you find broken parts of the program, don't just tell the AI to fix it, but ask it to explain what it's currently doing so you can understand it first. That way, when you do tell it to fix it, you can critically evaluate the fix to see if it's actually going to fix the problem. And don't be afraid to keep asking questions about the proposed fix, reprompt, or ask for alternatives! The goal is understanding alongside the AI, not just making it do it all for you.

ALSO: I had to use `python -m pytest -q` to run my tests!


## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
