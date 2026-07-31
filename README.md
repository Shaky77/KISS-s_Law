# KISS's Law — Keep Integrity & Steady State

> A structured framework for AI causal reasoning and decision validation.

## What is KISS's Law?

KISS's Law (Keep Integrity & Steady State) is a structured framework that transforms causal reasoning principles into executable rules for AI systems. It provides a rigorous methodology for auditing and projecting decisions through a verifiable causal chain.

**Core Formula:**

```
M = (R × S) / (D × H)
```

| Symbol | Name | Role |
|--------|------|------|
| **R** | Domain Constant | Rigid boundary defining the operational domain |
| **S** | Steady-state Reserve | Minimum value across all subsystems |
| **D** | Perturbation | Maximum disturbance across all sources |
| **H** | Lever | Observable action intensity (subjective choice) |
| **M** | Steady-state Outcome | Auditable & projectable result |

## Three Core Diagrams

| # | Diagram | Purpose |
|---|---------|---------|
| 01 | [Core Architecture](maps/01_core_architecture.jpg) | Causal chain R→S→D→H→M, formula, and Three Core Rules |
| 02 | [Boundary & Positioning](maps/02_boundary_positioning.jpg) | What KISS's Law does — and deliberately does not do |
| 03 | [Operating Mechanism](maps/03_operating_mechanism.jpg) | Bidirectional audit/projection + H leverage + termination conditions |

## Core Principles

1. **No Skipping** — The causal chain R→S→D→H→M cannot be bypassed
2. **No Reversal** — The sequence order is fixed and immutable
3. **No Discontinuity** — Every link in the chain must maintain causal connectivity

## Quick Start

```bash
# Run the demo to see KISS's Law in action
python demo.py
```

The demo includes:
- **AI Output Audit**: Audit AI-generated health claims using causal chain analysis
- **System Optimization**: Project system behavior under parameter changes

## Code Usage

### Basic: Compute Steady-state Outcome

```python
from weiwen_law import WeiwenLaw

system = WeiwenLaw("My System")

system.set_domain_constant(R=8.0, description="Performance requirement")
system.set_steady_state_reserve(S=0, subsystems={
    'component_A': 7.0, 'component_B': 6.0
})
system.set_perturbation(D=0, perturbation_sources={
    'load': 4.0, 'errors': 2.0
})
system.set_lever(H=2.0, description="Control effort")

M = system.compute_steady_state()
print(f"Steady-state: M = {M}")
```

### Audit Mode: Trace Causal Integrity

```python
audit_report = system.audit_backward()
print(f"Integrity: {audit_report['integrity']}")
for finding in audit_report['findings']:
    print(f"  - {finding}")
```

### Projection Mode: Predict Under Changed Conditions

```python
projection = system.project_forward(new_H=3.0)
print(f"Projected M: {projection['projected_state']['M']}")
print(f"Recommendation: {projection['recommendation']}")
```

## Requirements

- Python 3.8+
- No external dependencies (pure Python)

## License

This project is licensed under the **AGPL-3.0 License**.

Network use constitutes distribution — derivative works must be open-sourced under the same license. For commercial licensing, contact the copyright holder.

## Contact

- **Email**: `563003@qq.com`
- **GitHub**: [Shaky77](https://github.com/Shaky77)
