import os
from log_triage_agent import triage
from fix_suggestion_agent import suggest_fix
from auto_fix_agent import apply_fix_to_file

LOG_FILE = "app.log"
APP_FILE = "app.js"

# Check if agentic AI is enabled
if os.getenv("AGENTIC_AI_ENABLED", "false").lower() != "true":
    print("⚠️ Agentic AI is disabled. Exiting.")
    exit(0)

print("🤖 Agentic AI is enabled. Starting triage...")

# Step 1: Read log file
if not os.path.exists(LOG_FILE):
    print(f"❌ Log file {LOG_FILE} not found.")
    exit(1)

with open(LOG_FILE) as f:
    log_data = f.read()

# Step 2: Triage the log
triage_result = triage(log_data)
summary = triage_result.get("summary", "")
print("🔎 Summary:", summary)

# Step 3: Ask for fix suggestion
fix = suggest_fix(summary)
print("💡 Suggestion:", fix)

# Step 4: Apply fix (if enabled)
if os.getenv("AUTO_FIX_ENABLED", "false").lower() == "true":
    print("🛠️ Auto-fix is enabled.")
    success = apply_fix_to_file(APP_FILE, fix)
    if success:
        print("✅ Fix applied successfully.")
    else:
        print("❌ Failed to apply fix.")
else:
    print("🛑 Auto-fix is disabled. Manual fix required.")

print("============================================================")
print("📢 Deployment Notification")
print("------------------------------------------------------------")
print("🔍 Issue Summary:\n", summary)
print("🛠️ Suggested Fix:\n", fix)
print("============================================================")
