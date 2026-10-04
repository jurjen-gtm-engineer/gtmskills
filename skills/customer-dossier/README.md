# customer-dossier

Free foundation skill for ICP analysis. Before you analyze who your best customers are, you need ground truth about what your systems actually say about each account, and where they disagree.

Most ICP analysis fails at the input: CRM says Active, billing says cancelled, the call system attributes recordings to the wrong company, and one test account inflates ARR. Any pattern you extract from that is fiction that looks plausible. Plausible is the enemy of correct.

This skill builds the artifact everything else reads from: one dossier per account, every field with provenance and an explicit confidence state, every conflict surfaced. Run it once, then run ICP analysis, win-loss analysis, and churn analysis on top of the same artifact.

Concept: Jordan Crawford (Blueprint GTM). Implementation: NeuralFlow.

See `SKILL.md` for the full build process.
