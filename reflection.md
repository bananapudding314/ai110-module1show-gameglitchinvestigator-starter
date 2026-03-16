# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran the game, the number of attempts left displayed on screen would not decrement after the first guess, leading to the attempts left still displaying "1" when the game is over. In addition, the hint feature was telling the user to do the opposite of what they were supposed to. For instance, if the guess is higher than the answer, the hint said go higher, when it should be go lower. When I tried to start a new game by pressing the new game button, it would reset the mystery number but would not reset the game parameters (such as attempts left) and would not let me submit any guesses.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used the claude extension to explain why/where the bugs were happening in the code and to suggest fixes. For instance, for the hints bug, I told claude that my guess was that the logic for the condition detecting whether the guess was too high or too low is incorrect. It examined the code and suggested to fix the print statements, which worked. The issue was that it was printing "go higher" when the guess is higher than the answer and "go lower" when the guess is lower than the answer. When I brought up the issue of the attempts left not dislaying correctly because it was displaying "game over" when the attempts remaining still displayed 1. It 'fixed' the problem except when I tested it, it still didn't work. I looked more carefully to see what was actually happening and saw that the attempts didn't decrease after the first guess submission.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I tested the feature to see if it was fixed by playing the game. For instance, I looked at the secret number in the debugger tools to check the answer and entered guesses to make sure the hints output was correct. I also looked to see that the number of attempts left displayed decreased by 1 every time I hit submit and that "game over" was displayed when it hit 0. I did ask AI to design some test cases but the main bugs I saw were ones that could be tested by just playing the game.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Streamlit reruns are when streamlit runs the entire python code from top to bottom, which happens every time the user makes an interaction or the developer makes edits to the code. Each rerun happens on a blank state which means variables are initialized again unless stated otherwise in the code. The secret number was already stable when I initially ran the code, because st.session_state remains constant across reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy that I would reuse is using AI to examine errors and think through solutions. Next time, I want to use AI to design more detailed and intentional tests to ensure bug fixes were effective. This project made me rethink the way we can and are supposed to use AI when it comes to generating code. It acts more like a thinking partner rather than something that just writes code for you.