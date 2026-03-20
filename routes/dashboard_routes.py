"""
Dashboard routes module.
Handles analytics dashboard and data visualization.
"""

from __future__ import annotations

from functools import wraps

from flask import Blueprint, redirect, render_template, session, url_for

from utils.csv_logger import get_history, init_csv_if_not_exists

dashboard_bp = Blueprint("dashboard", __name__)


def login_required(f):
    """Decorator to require login for routes."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def _norm_status(value: object) -> str:
    return str(value or "").strip().upper()


def _safe_float(value: object) -> float | None:
    try:
        if value is None:
            return None
        text = str(value).strip()
        if not text:
            return None
        return float(text)
    except (TypeError, ValueError):
        return None


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    """Main dashboard view."""
    init_csv_if_not_exists()

    history_all = get_history()
    history = history_all[-200:]  # keep the page fast even if the CSV grows

    total_records = len(history_all)
    good_records = sum(_norm_status(r.get("Status")) == "GOOD" for r in history_all)
    attention_records = sum(
        _norm_status(r.get("Status")) == "ATTENTION REQUIRED" for r in history_all
    )
    critical_records = sum(_norm_status(r.get("Status")) == "CRITICAL" for r in history_all)

    scores = [_safe_float(r.get("Score")) for r in history_all]
    scores = [s for s in scores if s is not None]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0

    recent_alerts = [
        r for r in history_all if _norm_status(r.get("Status")) != "GOOD"
    ][-5:]

    return render_template(
        "dashboard.html",
        history=history,
        total_records=total_records,
        good_records=good_records,
        attention_records=attention_records,
        critical_records=critical_records,
        avg_score=avg_score,
        recent_alerts=recent_alerts,
    )

