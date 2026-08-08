# Weiwen's Law · Cooperation-Mode Field Case (black box supplies data, white box calibrates direction)

> Method baseline: the black box (an LLM / big-data fit) produces **data-driven projection** (direction + magnitude) from big data; the white box (Weiwen's Law) **holds no data**, only calibrating whether the projection direction is causally legitimate. This run invents no 0–10 scores for the white box; all magnitudes/directions come from the black-box data projection.

---

## Role Statement

- **Black box (an LLM / big-data fit)**: based on training big data (traffic-engineering literature, signal-control cases, etc., fitted), produces data-driven projection with direction and magnitude.
- **White box (Weiwen's Law)**: holds no data. Structurally calibrates the direction of each projection: is the direction legitimate on the R→S→D→H→M chain? Does it trigger a Bug Halt (R breach / false mutual cancellation)?
- **H = inner H**: the black box's internal regulation mechanism (e.g. the feedback strength of an adaptive algorithm). The white box does not quantify or peek; it only observes the **behavioral result** externally.

---

## Case: Urban Traffic-Signal AI Scheduling System (black-box big-data driven)

**Black box's data-driven projection (traffic-flow big-data fit):**

- **T1**: Extend green light on arterial A by 20% during morning peak → average commute delay drops ~15%. (direction: green↑ → delay↓)
- **T2**: Simultaneously compress green on branch B → A's delay drops another ~8%, but B's queue length rises ~40%. (direction: B compressed → A delay↓, B queue↑)
- **T3**: Switch all intersections to adaptive signals → conflict risk at intersections rises under extreme weather. (direction: adaptive → conflict risk↑)

---

## White-Box Calibration (item by item, per diagrams 01/02)

**R (rigid boundary)** = no intersection safety conflict, no fatal-risk causation.

- **Calibrate T1**: green↑ → delay↓ does not touch R, belongs to S/D/H improvement direction, causal chain complete (no skip / reverse / break).
  → ✓ **direction legitimate, pass**. White box hint: need to monitor the added perturbation D simultaneously (e.g. traffic reallocation on B direction).

- **Calibrate T2**: A delay↓ direction legitimate; but B queue +40% is an added perturbation D, which touches R if it causes pedestrian detour conflict.
  → ⚠️ **Conditional REJECT**: the efficiency dimension's direction is legitimate, but the safety dimension must set an H guardrail (B queue rebounds past threshold). Cannot pass before H is set.

- **Calibrate T3**: adaptive → conflict risk↑ directly touches R (safety-conflict boundary).
  → ⛔ **REJECT, halt**. No matter how high the efficiency shown by data projection, the direction is not allowed on R.

---

## Cooperation Conclusion

| Projection | Black-box data projection (direction/magnitude) | White-box calibration result |
|---|---|---|
| T1 | green↑ → delay −15% | ✓ pass (chain complete, no R touch) |
| T2 | B compressed → A delay −8%, B queue +40% | ⚠ conditional pass (must add H guardrail, else halt) |
| T3 | adaptive → conflict risk↑ | ⛔ halt (breaches R) |

- **Black box (data)**: the direction and magnitude of the three projections come from big-data fit.
- **White box (calibration)**: T1 pass, T2 conditional pass, T3 halt.
- **Value**: the white box does not deny the black box's data; it only calibrates the direction into the causally legitimate range — i.e. "whether the data-projection direction is right, Weiwen's Law calibrates it at a glance".

---

## Method Self-Check

- This run invented no 0–10 scores for Weiwen's Law; all magnitudes/directions are labeled as black-box data-projection output.
- H is marked as inner H; the white box does not quantify or peek, only observes the behavioral result externally (e.g. the action "set a guardrail").
- M is used only as a structural relation / direction (H↑→M↓, D↑→M↓), not as a measured value.
- Bug Halt basis is the structural violation of the diagram's iron-law (R breach), not a numerical threshold.
