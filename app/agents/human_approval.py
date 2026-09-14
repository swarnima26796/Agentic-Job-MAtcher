from app.models.approval import ApprovalResult
from app.models.gap_analysis import GapAnalysis


def get_human_approval(gap_analysis: GapAnalysis) -> ApprovalResult:
    """Present recommendations to the user and collect approval."""

    approved_changes = []

    print("\n===== HUMAN APPROVAL =====")

    for i, recommendation in enumerate(
        gap_analysis.recommended_changes,
        start=1,
    ):
        print(f"\nRecommendation {i}")
        print(f"Target: {recommendation.target}")
        print(f"Suggestion: {recommendation.recommendation}")
        print(f"Evidence: {recommendation.evidence}")

        while True:
            decision = input(
                "\nApprove this change? [y/n]: "
            ).strip().lower()

            if decision in {"y", "n"}:
                break

            print("Please enter 'y' or 'n'.")

        approved_changes.append(
            {
                "target": recommendation.target,
                "recommendation": recommendation.recommendation,
                "evidence": recommendation.evidence,
                "decision": "approved" if decision == "y" else "rejected",
            }
        )

    return ApprovalResult(changes=approved_changes)