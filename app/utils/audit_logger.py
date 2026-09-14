import json
from datetime import datetime
from pathlib import Path

from app.models.approval import ApprovalResult


def save_audit_log(
    approval_result: ApprovalResult,
    output_path: str = "output/audit_log.json",
) -> None:
    """Save human approval decisions for traceability."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    audit_record = {
        "timestamp": datetime.now().isoformat(),
        "changes": [
            change.model_dump()
            for change in approval_result.changes
        ],
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(audit_record, file, indent=2)

    print(f"\nAudit log saved to: {path}")