from pathlib import Path

from logic_utils import check_guess


def test_check_guess_high_low_messages_are_correct():
    """Regression test for the high/low hint direction bug."""
    too_high_outcome, too_high_message = check_guess(60, 50)
    too_low_outcome, too_low_message = check_guess(40, 50)

    assert too_high_outcome == "Too High"
    assert too_high_message == "📉 Go LOWER!"
    assert too_low_outcome == "Too Low"
    assert too_low_message == "📈 Go HIGHER!"


def test_new_game_uses_difficulty_based_random_range():
    """Regression test for New Game using 1..100 instead of (low, high)."""
    app_path = Path(__file__).resolve().parent.parent / "app.py"
    app_source = app_path.read_text(encoding="utf-8")

    assert "st.session_state.secret = random.randint(low, high)" in app_source
