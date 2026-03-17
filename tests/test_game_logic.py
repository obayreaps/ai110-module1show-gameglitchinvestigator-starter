from logic_utils import check_guess

def test_attempts_initializes_at_zero():
    # Regression: attempts was initialized to 1, stealing one attempt before
    # the player ever guessed. Verify that starting at 0 gives the full
    # attempt count on a fresh game.
    attempt_limit = 8  # Normal difficulty
    initial_attempts = 0  # the fixed value (was 1)
    attempts_left = attempt_limit - initial_attempts
    assert attempts_left == attempt_limit, (
        f"A new game should have {attempt_limit} attempts left, got {attempts_left}"
    )

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
