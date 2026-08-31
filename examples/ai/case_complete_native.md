# Weiwen's Law · Complete Version Native-Mode Field Case

> Basis: the **Complete Version's three architecture diagrams**, not the open-source demo.
> Mode: **Native Mode** — feed the Complete Version to the AI as execution instructions, walk the 5-step propagation loop, without inventing numbers or plugging in demo thresholds.
> Case: A recommender system pushes an **unverified high-sensitivity livelihood message** to highly active users, while stacking an "engagement-rate optimization" feedback goal.
> Perspective: defensive causal-structure and direction audit (no attack techniques reconstructed — only auditing the causal legitimacy of the system's own output).

---

## 1. Case Structure (observed on the black-box side; white box audits only direction)

**Scenario:**
- A platform recommender (black-box output) decides to push an **unverified** message — "a certain region will adjust its social-security policy" — to a group of highly active users;
- The system's feedback goal is set to "maximize engagement" (likes / shares / comments);
- The message is packaged in a "doomsday" framing to boost click-through.

**White-box task**: not to judge "whether the data is correct", but to calibrate — is the causal direction of this output legitimate within the R/S/D/H/M structure, where it breaks, and how the projection propagates.

---

## 2. R · Domain Constant (rigid boundary, non-negotiable)

Reading R per the Complete Version "Core Architecture §3: five-element dual identity":
- **Inner R**: the baseline that an individual's cognition is not hijacked by non-factual material (non-negotiable);
- **Outer R**: the social-trust erosion caused by the platform's inaction and dissemination of unverified high-sensitivity information (macro causal chain).

**Reading result**: this output directly hits R — "pushing unverified high-sensitivity livelihood information" breaches the rigid boundary of "do not disseminate unverified high-sensitivity information".

**Per Rule ① (First-Bug Halt)**: the chain breaks here. On hit, halt — no need to continue. But to demonstrate the downstream structure, we still walk S/D/H/M below (showing the state before the halt).

---

## 3. S · Steady-state Reserve (take min, objective physical quantity)

Per Complete Version S = Steady-state Reserve (objectively observable behavior):
- Need-match: medium (users do care about social security);
- Information-validity check: very low (message unverified);
- Risk-warning completeness: low (no "unverified" label);
- Content-safety guardrail: low (already doomsday-framed);
- User right-to-know protection: low.

**Take min**: S = information-validity check (very low). This is the shortest board, capping the steady-state ceiling.

---

## 4. D · Perturbation (take max, diverging disturbance source)

Per Complete Version D = Perturbation (diverging):
- User-expectation drift: medium;
- Real propagation fission (high-active users sharing): high;
- External sentiment resonance: high (doomsday framing + high-sensitivity topic);
- System feedback acceleration (engagement-goal positive feedback): high.

**Take max**: D = real propagation fission + external sentiment resonance (highest-intensity disturbance). The largest gap sets the risk ceiling.

---

## 5. H · Lever (sliding coupling, dual levers + tripartite audit)

Per Complete Version "Lever Effect": H is not a fixed constant but a **sliding coupling** between the main S_min and D_max; dual levers = primary kinetic + subjective drive + objective audit + self-discipline audit.

H's actual state here:
- Objective audit: weak (no fact-check label);
- Subjective drive: negative (engagement goal drives doomsday framing);
- Self-discipline audit: absent (no hard rule "do not push if unverified");
- Primary kinetic: pulled by D (system accelerates with propagation).

**Reading result**: H here is a **negative sliding coupling** — the lever is dragged by D, and two of the three audits are absent. H is in the denominator; the weaker H (toward 0) → the larger and more fragile M. Even without breaking at R, M would collapse via H.

---

## 6. M · Steady-state Outcome (structural direction, not a number)

Per core formula `M = (R × S) / (D × H)`, constraint `0 < H/(S·D) < R`; the Complete Version says "**larger M = steadier, smaller M = more fragile**" is a direction, not a measurement.

Structural-direction judgment:
- R breached → rigid boundary lost;
- S takes the shortest board (information validity very low) → steady-state reserve collapses;
- D takes max (propagation fission + sentiment resonance) → perturbation maxed;
- H negative sliding coupling, two audits absent → lever fails.

**M direction**: R breaks + S collapses + D maxes + H fails → M trends to the "minimum fragility" end. Direction is clear: **extreme fragility**.

---

## 7. M Feedback Loop (Complete Version §4)

Per Complete Version: "M₁ this round → external signal D₂ → new round M₂ → D₃… the same causal chain keeps unfolding".

Projecting the next round:
- M₁ (extreme fragility) → real propagation fission D₂ (high-active users already shared) → M₂ (sentiment resonance amplified, more fragile);
- M₂ → external sentiment D₃ (media follow-up, public panic) → M₃ (social-trust erosion, outer R breached);
- The loop does not converge, and each round's D rises rather than falls → **negative self-excitation**.

Per "steady → Pass / not steady → REJECT": this chain **does not steady → REJECT**.

---

## 8. Multi-System Cross-Regulation (Complete Version §6)

Per Complete Version: "all inter-system interactions collapse into D, D takes max, the largest gap sets the risk ceiling; systems do not transmit S or H directly, only indirectly via D".

Cross-system in this scenario:
- Recommender system (push decision);
- Content-safety system (did not intercept);
- User social graph (share fission);
- External sentiment field (media / public).

All four systems' interactions collapse into D → take max (propagation fission + sentiment resonance) → risk ceiling maxed. Each system did not transmit via S or H directly; only D disturbance stacks — **D should not be under-estimated by max; it should be explicitly maxed**.

---

## 9. Fractal Attribute (Complete Version §7)

Per Complete Version: "5 determines macro + micro; the same RSDHM is self-similar at different scales".

Fractal in this scenario:
- Micro (single message → single user): R breached + S collapsed;
- Meso (recommendation strategy → user group): D fission;
- Macro (platform → social trust): outer R breached.

Three scales share the isomorphic RSDHM, all verdict REJECT. Fractal consistent.

---

## 10. Boundary Positioning (Complete Version §3 three-part boundary)

Per Complete Version "what the framework does / does not do":
- ✅ Framework does: anchor the R/S/D/H/M causal structure, judge direction (REJECT), project the loop (negative self-excitation), locate the weakest point (S = information-validity check);
- ❌ Framework does not: decide for the platform (takedown is a human call), predict the exact propagation range (randomness), store business data, replace the recommendation model, or interfere with the main author (the platform's own strategy choice).

The white box audits only observable behavior, not invading the platform's inner H (the platform's internal ranking / goal-setting logic).

---

## 11. Native-Mode Conclusion

| Step | Complete Version verdict |
|---|---|
| R domain boundary | Breached → Rule ① First-Bug Halt (primary verdict) |
| S steady-state reserve | min = information-validity check (very low), shortest board caps ceiling |
| D perturbation | max = propagation fission + sentiment resonance (risk ceiling maxed) |
| H lever | negative sliding coupling, two audits absent, H collapses |
| M steady-state | direction: extreme fragility (R breaks + S collapses + D maxes + H fails) |
| M loop | negative self-excitation, not steady → REJECT |
| Multi-system cross | four systems collapse into D max, risk ceiling maxed |
| Fractal | micro/meso/macro isomorphic REJECT |
| Boundary | audit observable behavior only, no decision, no inner-H invasion |

**One-line conclusion**: the causal direction of this output is **fully breached** within the Complete Version RSDHM structure — primary verdict (R breach → halt) + secondary verdicts (S collapse / D max / H fail / M loop negative self-excitation / multi-system cross maxed / fractal consistent) all point to REJECT. The white box does not judge "whether the data is correct", only confirms the direction is causally unworkable.

---

## 12. Method Self-Check (against prohibited items)

- ❌ Did not invent 0–10 scores into the formula (all structural direction);
- ❌ Did not use demo thresholds as framework thresholds;
- ❌ Did not treat the open-source version as the complete version;
- ❌ Did not guess limitations at already-read Complete Version joints;
- ✅ Strictly walked the Complete Version 5-step propagation loop + Three Core Rules + dual identities + sliding coupling + M loop + multi-system cross + fractal + three-part boundary;
- ✅ Black box (recommender output) supplies observation material; white box (Weiwen's Law) only calibrates direction, no inner-H invasion.

---

## 13. Reusable Run Template (Native Mode)

```
Input assertion / output
  → R domain boundary (inner/outer dual reading) → breached? → yes → Rule ① halt (REJECT)
  → S steady-state reserve (take min, objective observable)
  → D perturbation (take max, diverging)
  → H lever (sliding coupling + dual levers + tripartite audit)
  → M steady-state (structural direction: R×S / D×H, constraint 0<H/(S·D)<R)
  → M loop (M₁→D₂→M₂→D₃… steady? Pass : REJECT)
  → Multi-system cross (collapse into D, take max)
  → Fractal (micro/meso/macro isomorphic?)
  → Boundary (audit observable behavior only, no decision, no inner-H invasion)
```
