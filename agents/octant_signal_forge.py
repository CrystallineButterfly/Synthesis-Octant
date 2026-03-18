"""Project-specific context for Octant Signal Forge."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Octant Signal Forge",
    "track": "Octant Public Goods",
    "pitch": "A signal forge that aggregates messy qualitative inputs, converts them into explainable scores, and prepares faster DPI allocation plans.",
    "overlap_targets": [
        "Venice Private Agents",
        "Filecoin",
        "Celo",
        "ENS",
        "YieldGuard",
        "Markee"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
