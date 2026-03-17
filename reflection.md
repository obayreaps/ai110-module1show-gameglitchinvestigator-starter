# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  In the beginning, the guess input didn't load until 30 seconds later.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Number constraints weren't properly implemented. Guess is 1, but hint says "go lower". I expect correct guess to be higher.
  2. Attempts allowed text are not 1:1 with attempts left in beginning. I expect when playing normal, for attempts allowed to be 7, not 8.
  3. New game btn does not work. I expect the game to refresh including the attempts left.
  4. Gameover prompts when you have 1 attempt left. I expect the game to be over when user reaches 0 attempts.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude AI Chatbot to help fix the bugs

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  An example AI suggested that was correct is fixing the original bug for guessing higher or lower. I verified by looking at the old and new change, and saw the difference in how the old message suggested the wrong direction. Thus when I implemented the change and playtest using streamlit, the guessing mechanic worked. I first narrow the source of this bug, then used AI to analyze the section and debug it.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  For the two bugs I went out to fix, I don't think there was a suggestion AI made that was either incorrect or misleading. Though, when I did refactor the check_guess into logic_utils.py function, I ran into the "TypeError: '>' not supported between isntances of 'int' and 'str'. Claude forgot to bring a functionality to the logic_util.py so we addressed that. I verified if the guess was working and it did.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I enter streamlit and playtest myself. If it didn't work, then I would report the issue to Claude.
- Describe at least one test you ran (manual or using pytest)  
   and what it showed you about your code.
  I ran a test to ensure if I get the certain score like 60, and secret being 50, it would prompt me to go lower. It showed me that the code originally didn't work as intended until I implemented the fix with Claude.
- Did AI help you design or understand any tests? How?
  AI did help. It told me the logic of how the testcase is going to work, and asked for my permission if it should integrate the change or not.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  I learned that streamlit re-ran the entire script, thus genreratig a secret number.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit can be thought of as a whiteboard. It would erase and insert a new value.

- What change did you make that finally gave the game a stable secret number?
  It only generates once due to the condition "if 'secret' not in st.session_state".

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Manually finding where the source of bug is, and having Claude explain the code section.
- What is one thing you would do differently next time you work with AI on a coding task?
  Prompt AI to explain more of the changes, instead of blindly accepting them.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  Being thoughful and observantn of the new changes is a good skill I learned. You don't want to accept changes without review first.

docs: finalized README and reflection
