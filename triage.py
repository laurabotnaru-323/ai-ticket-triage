import json

# -----------------------------
# AI-style summary generator
# -----------------------------
def ai_summary(ticket):
    issue = ticket["issue"].lower()

    if "password" in issue:
        return "User is unable to log in due to password-related issues. Recommend verifying identity and resetting credentials."
    if "access" in issue:
        return "User is requesting access to a system or resource. Suggest reviewing permissions and applying least-privilege principles."
    if "error" in issue or "fail" in issue:
        return "System-related error detected. Recommend checking logs and validating system health."
    return "General support request. Recommend reviewing details and following standard triage procedures."


# -----------------------------
# Ticket categorization
# -----------------------------
def categorize(issue):
    issue = issue.lower()
    if "password" in issue:
        return "Access Issue"
    if "access" in issue:
        return "Permission Request"
    if "error" in issue or "fail" in issue:
        return "System Issue"
    return "Other"


# -----------------------------
# Priority assignment
# -----------------------------
def assign_priority(issue):
    issue = issue.lower()
    if "password" in issue or "cannot log in" in issue:
        return "High"
    if "access" in issue:
        return "Medium"
    return "Low"


# -----------------------------
# Main triage function
# -----------------------------
def triage_tickets(file_path):
    with open(file_path, "r") as f:
        tickets = json.load(f)

    for ticket in tickets:
        issue = ticket["issue"]

        category = categorize(issue)
        priority = assign_priority(issue)
        summary = ai_summary(ticket)

        print(f"\nTicket #{ticket['id']}: {ticket['title']}")
        print(f"Category: {category}")
        print(f"Priority: {priority}")
        print(f"AI Summary: {summary}")


# -----------------------------
# Run script
# -----------------------------
if __name__ == "__main__":
    triage_tickets("tickets.json")
