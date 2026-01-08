#!/usr/bin/env python3
"""
Pomodoro Timer CLI
A simple command-line Pomodoro timer with session tracking.
"""

import time
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
WORK_MINUTES = 25
BREAK_MINUTES = 5
DATA_FILE = Path(__file__).parent / "data" / "sessions.json"

def format_time(seconds):
    """Format seconds as MM:SS."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"

# Test
print(format_time(90))    # Should print: 01:30
print(format_time(1500))  # Should print: 25:00
print(format_time(5))     # Should print: 00:05

def clear_line():
    """Clear the current line in terminal."""
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()

#Data Persistence Functions
def load_sessions():
    """Load sessions from JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"sessions": []}

def save_session(session_type, duration_minutes, completed):
    """Save a session to the JSON file."""
    data = load_sessions()
    
    session = {
        "type": session_type,
        "duration": duration_minutes,
        "completed": completed,
        "timestamp": datetime.now().isoformat()
    }
    
    data["sessions"].append(session)
    
    # Ensures data directory exists
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

#Core Timer Function
def countdown(minutes, label="Work"):
    """
    Run a countdown timer with live display.
    Returns True if completed, False if interrupted.
    """
    total_seconds = minutes * 60
    start_time = time.time()
    
    print(f"\n🍅 {label} Session - {minutes} minutes")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            elapsed = time.time() - start_time
            remaining = total_seconds - elapsed
            
            if remaining <= 0:
                clear_line()
                print(f"⏱️  {format_time(0)} - Complete!")
                return True
            
            # Progress bar
            progress = elapsed / total_seconds
            bar_width = 30
            filled = int(bar_width * progress)
            bar = "█" * filled + "░" * (bar_width - filled)
            
            sys.stdout.write(f"\r⏱️  {format_time(remaining)} [{bar}] {int(progress * 100)}%")
            sys.stdout.flush()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        clear_line()
        print("⏹️  Session stopped early")
        return False
    
#Stats

def get_stats():
    """Calculate session statistics."""
    data = load_sessions()
    sessions = data.get("sessions", [])
    
    now = datetime.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = today_start - timedelta(days=now.weekday())
    
    today_count = 0
    week_count = 0
    total_minutes_today = 0
    total_minutes_week = 0
    
    for session in sessions:
        if session["type"] != "work" or not session["completed"]:
            continue
            
        session_time = datetime.fromisoformat(session["timestamp"])
        
        if session_time >= today_start:
            today_count += 1
            total_minutes_today += session["duration"]
        
        if session_time >= week_start:
            week_count += 1
            total_minutes_week += session["duration"]
    
    return {
        "today": today_count,
        "week": week_count,
        "minutes_today": total_minutes_today,
        "minutes_week": total_minutes_week
    }

def display_stats():
    """Display session statistics."""
    stats = get_stats()
    
    print("\n📊 Your Pomodoro Stats")
    print("─" * 30)
    print(f"Today:     {stats['today']} sessions ({stats['minutes_today']} min)")
    print(f"This week: {stats['week']} sessions ({stats['minutes_week']} min)")
    print("─" * 30)

#Main Program Functions

def run_pomodoro():
    """Run a full Pomodoro cycle (work + break)."""
    # Work session
    completed = countdown(WORK_MINUTES, "Work")
    save_session("work", WORK_MINUTES, completed)
    
    if completed:
        print("\n✅ Work session complete! Time for a break.")
        input("Press Enter to start break...")
        
        # Break session
        break_completed = countdown(BREAK_MINUTES, "Break")
        save_session("break", BREAK_MINUTES, break_completed)
        
        if break_completed:
            print("\n🎉 Break over! Ready for another round?")
    
    display_stats()
    
def main():
    """Main entry point."""
    print("=" * 40)
    print("🍅 POMODORO TIMER")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("  [s] Start Pomodoro (25 min work + 5 min break)")
        print("  [w] Work session only (25 min)")
        print("  [b] Break only (5 min)")
        print("  [t] View stats")
        print("  [q] Quit")
        
        choice = input("\nChoice: ").strip().lower()
        
        if choice == "s":
            run_pomodoro()
        elif choice == "w":
            completed = countdown(WORK_MINUTES, "Work")
            save_session("work", WORK_MINUTES, completed)
            display_stats()
        elif choice == "b":
            completed = countdown(BREAK_MINUTES, "Break")
            save_session("break", BREAK_MINUTES, completed)
        elif choice == "t":
            display_stats()
        elif choice == "q":
            print("\n👋 Goodbye! Keep being productive!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()