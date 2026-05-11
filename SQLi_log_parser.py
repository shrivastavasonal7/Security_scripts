import re

patterns_with_advice = {
    "'": "String escape - use parameterized queries or escape single quotes.",
    "--": "Comment Injection - sanitize input",
    ";": "Statement Termination - use paramterized queries and validate input",
    "/*": "Comment Injection - sanitize input",
    "OR 1=1": "Boolean-based SQL Injection - use Parametrized queries and validate inoput",
    "Union Select": "Union-based SQL Injection - use parameterized queries and validate input",
    "xp_cmdshell": "OS command execution - disable xp_cmdshell",
    "sleep" : "Time-based BlindSQL Injection - use parameterized queries and validate input",
    "DROP" : "Data Destruction - enforce least privilege",
    "INSERT" : "Data Manipulation - enforce least privilege",
    "LOAD_FILE" : "File read via SQL Injection - restrict file privileges",
}

def detect_sqli(log_file):
    findings = []
    with open(log_file, "r") as f:
        for line in f:
            line_findings = []
            for pattern, advice in patterns_with_advice.items():
                if pattern.lower() in line.lower():
                    line_findings.append((pattern, advice))

            if line_findings:
                print(f"\n [Suspicious] {line.strip()}")
                for pattern, advice in line_findings:
                    print(f" - Pattern: {pattern}")
                    print(f"   Advice: {advice}")
                findings.extend(line_findings)
            else:
                print(f"\n [Clean] {line.strip()}")

    return findings

if __name__ == "__main__":
    log_file = "sql_logs.txt"
    result = detect_sqli(log_file)
    print(f" \n Total findings: {len(result)}")




