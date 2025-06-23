from AgenticAI.log_triage_agent import triage

sample_log = """Error: throw new Error("Intentional startup failure for triage test");
at Object.<anonymous> (/home/***/AgenticDevOpsDemo/app.js:1:7)
at Module._compile (node:internal/modules/cjs/loader:1364:14)
at Module._extensions..js (node:internal/modules/cjs/loader:1422:10)"""

result = triage(sample_log)
print("\nError Summary:\n", result["summary"])
