from AgenticAI.fix_suggestion_agent import suggest_fix

error = 'throw new Error("Intentional startup failure for triage test");'
fix = suggest_fix(error)
print("\n Suggested Fix:\n", fix)
