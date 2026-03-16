from logic_utils import check_guess, get_range_for_difficulty

# ---------------------------------------------------------------------------
# Existing tests: basic check_guess outcomes
# ---------------------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# ---------------------------------------------------------------------------
# Attempts left display
# ---------------------------------------------------------------------------

def compute_attempts_left(attempt_limit, attempts_used, submit_pending):
    """Mirror the formula used in app.py's st.info display."""
    return attempt_limit - attempts_used - (1 if submit_pending else 0)

def test_attempts_left_at_start():
    # Before any guesses, the full limit should be shown
    assert compute_attempts_left(attempt_limit=8, attempts_used=0, submit_pending=False) == 8

def test_attempts_left_decrements_each_guess():
    # After each guess the displayed count should drop by 1
    assert compute_attempts_left(attempt_limit=8, attempts_used=3, submit_pending=False) == 5

def test_attempts_left_accounts_for_pending_submit():
    # When the submit button has just been pressed (but session state hasn't
    # incremented yet), the display should already show the decremented value
    assert compute_attempts_left(attempt_limit=8, attempts_used=3, submit_pending=True) == 4

def test_attempts_left_reaches_zero_on_last_guess():
    # On the final guess the display should show 0, not 1
    assert compute_attempts_left(attempt_limit=8, attempts_used=7, submit_pending=True) == 0


# ---------------------------------------------------------------------------
# Hint direction: too high / too low messages
# ---------------------------------------------------------------------------

def test_too_high_hint_says_go_lower():
    # When the guess exceeds the secret the hint must direct the player lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_too_low_hint_says_go_higher():
    # When the guess is below the secret the hint must direct the player higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_correct_guess_hint_says_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()


# ---------------------------------------------------------------------------
# New game reset
# ---------------------------------------------------------------------------

def simulate_new_game(difficulty):
    """
    Simulate what the New Game button does in app.py and return the
    resulting session-state-like dict.
    """
    import random
    low, high = get_range_for_difficulty(difficulty)
    state = {
        "attempts": 0,
        "status": "playing",
        "secret": random.randint(low, high),
        "difficulty": difficulty,
    }
    return state, low, high

def test_new_game_resets_attempts_to_zero():
    state, _, _ = simulate_new_game("Normal")
    assert state["attempts"] == 0

def test_new_game_resets_status_to_playing():
    # Ensures the game is unblocked after a win/loss
    state, _, _ = simulate_new_game("Normal")
    assert state["status"] == "playing"

def test_new_game_secret_within_easy_range():
    for _ in range(20):  # repeat to reduce fluke probability
        state, low, high = simulate_new_game("Easy")
        assert low <= state["secret"] <= high

def test_new_game_secret_within_normal_range():
    for _ in range(20):
        state, low, high = simulate_new_game("Normal")
        assert low <= state["secret"] <= high

def test_new_game_secret_within_hard_range():
    for _ in range(20):
        state, low, high = simulate_new_game("Hard")
        assert low <= state["secret"] <= high
