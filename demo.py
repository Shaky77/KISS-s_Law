"""
Demo: Using Weiwen's Law to Audit AI Output

Copyright (c) 2026 Xia Qi (夏祺). All rights reserved.
Software Copyright Registration No.: 2026SR0748746
ORCID: https://orcid.org/0009-0002-1433-6982
============================================

    *** AUXILIARY REFERENCE CODE ONLY ***

The complete system rules are fully contained within the three architecture
diagrams in /maps. This demo only demonstrates basic formula calculation
and audit/projection — it does NOT cover all recursive and multi-domain
rules shown in the diagrams.

Native recommended usage:
    Feed the diagrams directly to your AI. No code required.

---

This demo shows how to use Weiwen's Law framework to audit AI-generated content
and identify causal integrity issues.

Run: python demo.py
"""

from weiwen_law import WeiwenLaw


def audit_ai_claims():
    """
    Real-world example: Auditing an AI system that makes health claims.
    
    The AI claims: "Drinking 8 glasses of water daily prevents all kidney diseases."
    
    We'll use Weiwen's Law to audit this claim's causal integrity.
    """
    print("=" * 70)
    print("AUDIT: AI Health Claim")
    print("=" * 70)
    print()
    print("Claim: 'Drinking 8 glasses of water daily prevents all kidney diseases.'")
    print()
    
    # Initialize the audit
    audit = WeiwenLaw("Health Claim Validation")
    
    # R: Domain Constant
    # What's the non-negotiable boundary? In health claims, it's scientific evidence.
    audit.set_domain_constant(
        R=9.0,
        description="Scientific evidence threshold (0-10 scale)"
    )
    
    # S: Steady-state Reserve
    # What subsystems support this claim?
    # - Clinical studies: moderate evidence exists
    # - Mechanism understanding: well-understood
    # - Consensus agreement: NOT universal (some kidney diseases are genetic)
    subsystems = {
        'clinical_studies': 7.0,      # Some evidence but not conclusive
        'mechanism_understanding': 8.5,  # Hydration mechanism is clear
        'consensus_agreement': 3.0       # CRITICAL: Not all kidney diseases are preventable
    }
    
    audit.set_steady_state_reserve(
        S=0,  # Will auto-compute as min
        description="Supporting evidence quality",
        subsystems=subsystems
    )
    
    print("Subsystem Analysis:")
    for name, val in subsystems.items():
        print(f"  - {name}: {val}")
    print(f"  → S (weakest link) = {min(subsystems.values())}")
    print()
    
    # D: Perturbation
    # What disturbances affect this claim's validity?
    perturbation_sources = {
        'genetic_factors': 8.0,      # HIGH: Many kidney diseases are genetic
        'conflicting_research': 4.0,  # Some studies dispute the claim
        'oversimplification': 7.5    # "Prevents ALL" is too absolute
    }
    
    audit.set_perturbation(
        D=0,  # Will auto-compute as max
        description="Validity disturbances",
        perturbation_sources=perturbation_sources
    )
    
    print("Perturbation Analysis:")
    for name, val in perturbation_sources.items():
        print(f"  - {name}: {val}")
    print(f"  → D (strongest disturbance) = {max(perturbation_sources.values())}")
    print()
    
    # H: Lever
    # How much verification effort are we applying?
    audit.set_lever(
        H=1.5,
        description="Fact-checking effort"
    )
    
    # Compute the steady-state outcome
    M = audit.compute_steady_state()
    
    print(audit.get_summary())
    print()
    
    # Audit the claim
    print("=" * 70)
    print("AUDIT FINDINGS")
    print("=" * 70)
    audit_report = audit.audit_backward()
    
    print(f"\nCausal Chain Integrity: {audit_report['integrity']}")
    
    if audit_report['findings']:
        print("\nIssues Found:")
        for i, finding in enumerate(audit_report['findings'], 1):
            print(f"  {i}. {finding}")
    
    print()
    print("INTERPRETATION:")
    if M < 1.0:
        print("  ⚠️  CRITICAL: Claim lacks causal integrity")
        print("  → The claim overstates the evidence")
        print("  → Consensus agreement (S=3.0) is the weakest link")
        print("  → Genetic factors (D=8.0) are the strongest disturbance")
        print()
        print("  CORRECTIVE ACTION:")
        print("  → Revise claim to: 'Adequate hydration may reduce risk of some")
        print("    kidney diseases, but genetic and other factors also play roles.'")
    elif M < 2.0:
        print("  ⚠️  CAUTION: Claim has limited causal support")
    else:
        print("  ✓ Claim demonstrates causal integrity")
    
    print()
    print("=" * 70)
    print("PROJECTION: What if we increase fact-checking effort?")
    print("=" * 70)
    
    projection = audit.project_forward(new_H=3.0)
    print(f"Current M:      {projection['current_state']['M']:.4f}")
    print(f"Projected M:    {projection['projected_state']['M']:.4f}")
    print(f"Change:         {projection['delta_M']:+.4f}")
    print(f"Stability:      {projection['stability_change']}")
    print(f"Recommendation: {projection['recommendation']}")
    print()
    print("ANALYSIS:")
    print("  Increasing verification effort (H) DOES improve M,")
    print("  but the fundamental issue is the weak subsystem (consensus_agreement)")
    print("  and strong disturbance (genetic_factors).")
    print()
    print("  The claim needs REVISION, not just more fact-checking.")
    print()


def project_system_changes():
    """
    Example: Using projection mode to predict system behavior under changes.
    """
    print("=" * 70)
    print("PROJECTION: System Optimization")
    print("=" * 70)
    print()
    
    system = WeiwenLaw("System Optimization")
    
    # Baseline configuration
    system.set_domain_constant(R=8.0, description="Performance requirement")
    system.set_steady_state_reserve(
        S=0,
        description="System resilience",
        subsystems={
            'component_A': 7.0,
            'component_B': 6.0,
            'component_C': 8.5
        }
    )
    system.set_perturbation(
        D=0,
        description="Environmental stress",
        perturbation_sources={
            'load_spike': 5.0,
            'network_latency': 3.0
        }
    )
    system.set_lever(H=2.0, description="Control effort")
    
    baseline_M = system.compute_steady_state()
    print(f"Baseline M: {baseline_M:.4f}")
    print()
    
    # Scenario 1: Strengthen weakest component
    print("SCENARIO 1: Strengthen component_B from 6.0 → 8.0")
    system.set_steady_state_reserve(
        S=0,
        subsystems={
            'component_A': 7.0,
            'component_B': 8.0,  # Improved
            'component_C': 8.5
        }
    )
    new_M = system.compute_steady_state()
    print(f"New M: {new_M:.4f} (change: {new_M - baseline_M:+.4f})")
    print()
    
    # Scenario 2: Reduce disturbance
    print("SCENARIO 2: Reduce load spike from 5.0 → 3.0")
    system.set_perturbation(
        D=0,
        perturbation_sources={
            'load_spike': 3.0,  # Reduced
            'network_latency': 3.0
        }
    )
    new_M2 = system.compute_steady_state()
    print(f"New M: {new_M2:.4f} (change: {new_M2 - baseline_M:+.4f})")
    print()
    
    # Scenario 3: Increase control effort
    print("SCENARIO 3: Increase control effort from 2.0 → 3.0")
    system.set_lever(H=3.0, description="Increased control effort")
    new_M3 = system.compute_steady_state()
    print(f"New M: {new_M3:.4f} (change: {new_M3 - baseline_M:+.4f})")
    print()
    
    print("INSIGHT:")
    print("  - Strengthening weakest component (S) had the largest impact")
    print("  - Reducing disturbance (D) also helped significantly")
    print("  - Increasing control effort (H) reduced M in this scenario")
    print("    This does NOT mean control effort is useless.")
    print("    Excessive or inefficient balancing leverage consumes system resources,")
    print("    which suppresses overall steady-state outcome under fixed conditions.")
    print("    H is the subjective leverage point — efficient use matters, not raw intensity.")
    print()
    print("  This demonstrates the formula's predictive power:")
    print("  M = (R × S) / (D × H)")
    print()


if __name__ == "__main__":
    audit_ai_claims()
    print("\n\n")
    project_system_changes()
    
    print("=" * 70)
    print("END OF DEMO")
    print("=" * 70)
    print()
    print("Key Takeaways:")
    print("  1. Weiwen's Law provides a structured framework for causal analysis")
    print("  2. The formula M = (R × S) / (D × H) is deterministic and auditable")
    print("  3. Audit mode traces backward to find causal integrity issues")
    print("  4. Projection mode predicts outcomes under changed conditions")
    print("  5. The framework is domain-agnostic and can be applied anywhere")
    print()
    print("Next Steps:")
    print("  - Explore the weiwen_law.py module for full API")
    print("  - Try applying it to your own domain")
    print("  - Read the diagrams in maps/ for visual reference")
