# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

### BUGS I FOUND:
1. The hints were backwards (said guess higher when the secret number was lower and vice versa) (CAUSE: logic is flipped in code)
2. The difficulties don't seem to match (easy should have lowest range and hard should have greatest range) (CAUSE: ranges set incorrectly in code)
3. After winning, if you click new game, it resets the number but won't let you guess anymore (CAUSE: status is not reset to "playing")
4. The random number could be outside the range shown based on difficulty (CAUSE: random number's range is always 1-100)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Used GitHub Copilot to fix bugs 1 and 4 above, as well as refactor so that check_guess and parse_guess were moved into logic_utils.py

A guiding hint I would give a student:
As you find broken parts of the program, don't just tell the AI to fix it, but ask it to explain what it's currently doing so you can understand it first. That way, when you do tell it to fix it, you can critically evaluate the fix to see if it's actually going to fix the problem. And don't be afraid to keep asking questions about the proposed fix, reprompt, or ask for alternatives! The goal is understanding alongside the AI, not just making it do it all for you.
ALSO: I had to use `python -m pytest -q` to run my tests!

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
