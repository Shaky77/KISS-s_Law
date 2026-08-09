# Weiwen's Law · Cooperation Mode Finalized Methodology

> **Date**: 2026-08-05
> **Purpose**: Finalize the "black box produces data, white box calibrates direction" cooperation paradigm

---

## Core Paradigm

**Black box (LLM / big data / empirical models)**:
- Responsible for **data-driven projection** (direction + magnitude)
- Holds data, performs numerical computation, generates predictions

**White box (Weiwen's Law)**:
- Responsible for **calibrating whether the projection direction is causally legitimate**
- Does not hold data, does not assign values, only judges structural rationality

---

## Cooperation Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                        Full Pipeline                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    projection     ┌─────────┐    calibration    ┌──┴──┐
│  │  Black   │ ───────────────> │  White  │ ───────────────> │Judge│
│  │   Box    │  (direction +    │   Box   │  (causally       │     │
│  │          │   magnitude)     │         │   legitimate?)   │     │
│  └─────────┘                   └─────────┘                  └─────┘
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Step 1: Black Box Projection

Black box based on data, models, experience, produces:
- **Direction**: Should we proceed with this decision? (Yes / No / Needs more info)
- **Magnitude**: If proceeding, what level of resource commitment is needed?

### Step 2: White Box Calibration

White box does NOT:
- ❌ Assign numerical scores
- ❌ Compute formula results
- ❌ Make decisions based on numbers

White box DOES:
- ✅ Check R: Does this direction violate rigid boundaries?
- ✅ Check S: Does the current stability reserve support this direction?
- ✅ Check D: What disturbances might this direction face?
- ✅ Check H: Are there sufficient leverage points to regulate?
- ✅ Check causal chain completeness: Are there structural breaks?

### Step 3: Comprehensive Judgment

Based on white box calibration results:
- **Causal chain complete + No rigid boundary violations** → Can proceed
- **Causal chain has breaks** → REJECT, need to fix first
- **Causal chain complete but S insufficient** → Can proceed, but need to increase H for regulation

---

## Case: Traffic Signal AI Scheduling

### Background

A city wants to use AI to optimize traffic signal timing, to reduce congestion.

### Black Box Projection

Black box based on historical traffic data, real-time sensor data, ML model training, produces:
- **Direction**: AI scheduling can reduce congestion by ~20%
- **Magnitude**: Need to invest $5M for system upgrade, 6-month construction period

### White Box Calibration

**R (Rigid Boundary)**:
- Traffic signal systems cannot cause traffic paralysis
- Must guarantee emergency vehicle priority passage
- Cannot violate traffic safety regulations

→ R is satisfied, no boundary violations

**S (Stability Reserve)**:
- Current traffic system stability is acceptable
- But AI system is new, has no long-term operational data
- S is at a medium level

**D (Disturbance)**:
- Weather changes (heavy rain, snow)
- Special events (parades, construction)
- System failures (sensor failure, network outage)
- D is at a medium-high level

**H (Leverage)**:
- Can set up manual override mechanisms
- Can establish real-time monitoring systems
- Can design fallback plans (revert to traditional timing)
- H is at a high level

**Causal Chain Check**:
- "AI scheduling" → "Signal timing optimization" → "Congestion reduction"
- Each link has clear causal relationship
- Fallback plan ensures controllability even if AI fails

→ Causal chain is **complete**

### Comprehensive Judgment

- R: Satisfied
- Causal chain: Complete
- S: Medium, but H can compensate
- D: Medium-high, but H can regulate

**Conclusion: PASS** — Can proceed, but need to:
1. Establish comprehensive monitoring system
2. Design fallback plan
3. Gradually roll out, not all at once
4. Maintain manual intervention capability

---

## Cooperation Mode Advantages

1. **Clear division of labor**: Black box does what it's best at (data), white box does what it's best at (structural judgment)
2. **Mutual compensation**: Black box makes up for white box's lack of data; white box makes up for black box's blind spots in causal reasoning
3. **Risk controllable**: White box's Bug-stop rule ensures system won't make irreversible mistakes
4. **Continuously evolvable**: Each cooperation feeds back experience, continuously optimizing both parties' capabilities

---

## Comparison with Previous Error Methods

| Dimension | Previous Error Method | Correct Cooperation Mode |
|---|---|---|
| White box role | Hold data + compute | Only calibrate direction |
| R/S/D/H | Numerical scoring | Structural relationship description |
| M computation | Required | Not required |
| Judgment basis | Compare M with threshold | Judge causal chain completeness |
| Error source | Subjective scoring bias | Black box projection bias (controllable) |

---

## Summary

Cooperation mode is the correct way to use Weiwen's Law:
- **Black box is responsible for "what"**: What does data say? What do models predict?
- **White box is responsible for "why"**: Why is this direction causally legitimate? Where are the breakpoints?

Only when "what" and "why" align, can decisions be truly reliable.

> This document is the final version of the cooperation mode methodology, for use in subsequent case runs.
