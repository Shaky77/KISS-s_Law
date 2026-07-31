"""
Weiwen's Law (KISS's Law) - Core Implementation
================================================

A structured framework for AI causal reasoning and decision validation.

Core Formula: M = (R × S) / (D × H)

Where:
- R: Domain Constant (rigid boundary)
- S: Steady-state Reserve (min across subsystems)
- D: Perturbation (max across disturbances)
- H: Lever (observable action intensity)
- M: Steady-state Outcome (auditable & projectable)

Three Core Rules:
1. No Skipping: R→S→D→H→M chain cannot be bypassed
2. No Reversal: Sequence order is fixed
3. No Discontinuity: Every link must maintain causal connectivity

License: AGPL-3.0
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json


@dataclass
class CausalNode:
    """Represents a node in the causal chain"""
    name: str
    value: float
    description: str = ""
    subsystems: Optional[List['CausalNode']] = None


class WeiwenLaw:
    """
    Weiwen's Law framework implementation.
    
    Provides methods for:
    - Computing steady-state outcome (M)
    - Auditing decisions backward through causal chain
    - Projecting future states forward
    - Validating causal chain integrity
    """
    
    def __init__(self, domain_name: str = "System"):
        self.domain_name = domain_name
        self.causal_chain = {}
        self.audit_log = []
    
    def set_domain_constant(self, R: float, description: str = "") -> None:
        """
        Set the Domain Constant (R) - rigid boundary of the operational domain.
        This is the non-negotiable constraint that defines the system.
        """
        self.causal_chain['R'] = CausalNode('R', R, description)
        self._log(f"R set: {R} ({description})")
    
    def set_steady_state_reserve(self, S: float, description: str = "", 
                                  subsystems: Optional[Dict[str, float]] = None) -> None:
        """
        Set the Steady-state Reserve (S) - minimum across all subsystems.
        The weakest subsystem determines overall stability.
        """
        subsystem_nodes = None
        if subsystems:
            subsystem_nodes = [CausalNode(name, val, f"Subsystem: {name}") 
                             for name, val in subsystems.items()]
            actual_S = min(subsystems.values())
            self._log(f"S computed as min of subsystems: {actual_S}")
            self._log(f"  Subsystems: {subsystems}")
        else:
            actual_S = S
        
        self.causal_chain['S'] = CausalNode('S', actual_S, description, subsystem_nodes)
        self._log(f"S set: {actual_S} ({description})")
    
    def set_perturbation(self, D: float, description: str = "",
                        perturbation_sources: Optional[Dict[str, float]] = None) -> None:
        """
        Set the Perturbation (D) - maximum across all disturbance sources.
        The strongest disturbance determines system stress.
        """
        perturbation_nodes = None
        if perturbation_sources:
            perturbation_nodes = [CausalNode(name, val, f"Source: {name}") 
                                 for name, val in perturbation_sources.items()]
            actual_D = max(perturbation_sources.values())
            self._log(f"D computed as max of sources: {actual_D}")
            self._log(f"  Sources: {perturbation_sources}")
        else:
            actual_D = D
        
        self.causal_chain['D'] = CausalNode('D', actual_D, description, perturbation_nodes)
        self._log(f"D set: {actual_D} ({description})")
    
    def set_lever(self, H: float, description: str = "") -> None:
        """
        Set the Lever (H) - observable action intensity.
        This is the subjective choice point where agency applies force.
        """
        self.causal_chain['H'] = CausalNode('H', H, description)
        self._log(f"H set: {H} ({description})")
    
    def compute_steady_state(self) -> float:
        """
        Compute the Steady-state Outcome (M) using the core formula.
        M = (R × S) / (D × H)
        """
        self._validate_chain_completeness()
        
        R = self.causal_chain['R'].value
        S = self.causal_chain['S'].value
        D = self.causal_chain['D'].value
        H = self.causal_chain['H'].value
        
        if D * H == 0:
            raise ValueError("D and H cannot be zero (division by zero)")
        
        M = (R * S) / (D * H)
        self.causal_chain['M'] = CausalNode('M', M, "Steady-state Outcome")
        self._log(f"M computed: ({R} × {S}) / ({D} × {H}) = {M:.4f}")
        
        return M
    
    def audit_backward(self) -> Dict[str, Any]:
        """
        Audit mode: Trace backward from outcome (M) through causal chain.
        Returns audit report showing causal connectivity.
        """
        self._validate_chain_completeness()
        
        audit_report = {
            'mode': 'AUDIT (Backward)',
            'domain': self.domain_name,
            'chain': [],
            'integrity': 'PASS',
            'findings': []
        }
        
        # Start from M and trace backward
        M = self.causal_chain['M'].value
        H = self.causal_chain['H'].value
        D = self.causal_chain['D'].value
        S = self.causal_chain['S'].value
        R = self.causal_chain['R'].value
        
        # Verify causal connectivity
        expected_M = (R * S) / (D * H)
        
        audit_report['chain'] = [
            {'node': 'M', 'value': M, 'description': 'Outcome'},
            {'node': 'H', 'value': H, 'description': 'Lever (action intensity)'},
            {'node': 'D', 'value': D, 'description': 'Perturbation'},
            {'node': 'S', 'value': S, 'description': 'Steady-state Reserve'},
            {'node': 'R', 'value': R, 'description': 'Domain Constant'},
        ]
        
        if abs(M - expected_M) > 1e-6:
            audit_report['integrity'] = 'FAIL'
            audit_report['findings'].append(
                f"Causal discontinuity: M={M:.4f} ≠ expected={expected_M:.4f}"
            )
        
        # Check for violations
        if self.causal_chain['S'].subsystems:
            min_S = min(n.value for n in self.causal_chain['S'].subsystems)
            if S != min_S:
                audit_report['findings'].append(
                    f"S should be min of subsystems: {S} ≠ {min_S}"
                )
        
        if self.causal_chain['D'].subsystems:
            max_D = max(n.value for n in self.causal_chain['D'].subsystems)
            if D != max_D:
                audit_report['findings'].append(
                    f"D should be max of sources: {D} ≠ {max_D}"
                )
        
        self._log(f"Audit completed: {audit_report['integrity']}")
        return audit_report
    
    def project_forward(self, new_H: float, new_D: Optional[float] = None) -> Dict[str, Any]:
        """
        Projection mode: Predict future steady-state under changed conditions.
        Returns projection report.
        """
        if 'R' not in self.causal_chain or 'S' not in self.causal_chain:
            raise ValueError("R and S must be set before projection")
        
        R = self.causal_chain['R'].value
        S = self.causal_chain['S'].value
        old_H = self.causal_chain['H'].value if 'H' in self.causal_chain else 1.0
        old_D = self.causal_chain['D'].value if 'D' in self.causal_chain else 1.0
        
        proj_H = new_H
        proj_D = new_D if new_D is not None else old_D
        
        old_M = (R * S) / (old_D * old_H)
        new_M = (R * S) / (proj_D * proj_H)
        
        projection_report = {
            'mode': 'PROJECTION (Forward)',
            'domain': self.domain_name,
            'current_state': {
                'M': old_M,
                'H': old_H,
                'D': old_D
            },
            'projected_state': {
                'M': new_M,
                'H': proj_H,
                'D': proj_D
            },
            'delta_M': new_M - old_M,
            'stability_change': 'IMPROVED' if new_M > old_M else 'DEGRADED',
            'recommendation': self._generate_recommendation(old_M, new_M)
        }
        
        self._log(f"Projection: M changes from {old_M:.4f} to {new_M:.4f}")
        return projection_report
    
    def _validate_chain_completeness(self) -> None:
        """Validate that all nodes R, S, D, H are present"""
        required = ['R', 'S', 'D', 'H']
        missing = [n for n in required if n not in self.causal_chain]
        
        if missing:
            raise ValueError(f"Missing nodes in causal chain: {missing}")
    
    def _generate_recommendation(self, old_M: float, new_M: float) -> str:
        """Generate recommendation based on projection"""
        if new_M > old_M * 1.2:
            return "Significant improvement - proceed with confidence"
        elif new_M > old_M:
            return "Moderate improvement - monitor closely"
        elif new_M > old_M * 0.8:
            return "Slight degradation - consider adjustment"
        else:
            return "Major degradation - halt and reassess"
    
    def _log(self, message: str) -> None:
        """Log audit trail"""
        self.audit_log.append(message)
    
    def get_summary(self) -> str:
        """Get human-readable summary of current state"""
        if not self.causal_chain:
            return "No causal chain configured"
        
        lines = [f"=== Weiwen's Law: {self.domain_name} ==="]
        
        for key in ['R', 'S', 'D', 'H', 'M']:
            if key in self.causal_chain:
                node = self.causal_chain[key]
                lines.append(f"{key}: {node.value:.4f} - {node.description}")
        
        if 'M' in self.causal_chain:
            M = self.causal_chain['M'].value
            if M > 1.0:
                status = "STABLE"
            elif M > 0.5:
                status = "CAUTION"
            else:
                status = "CRITICAL"
            lines.append(f"\nSteady-state: {status} (M={M:.4f})")
        
        return "\n".join(lines)
    
    def export_audit_log(self) -> str:
        """Export audit log as formatted string"""
        return "\n".join(self.audit_log)


def demo_ai_audit():
    """
    Demo: Using Weiwen's Law to audit AI output quality.
    
    Scenario: An AI system is generating content. We want to audit
    whether the output maintains causal integrity.
    """
    print("=" * 60)
    print("DEMO: AI Output Audit using Weiwen's Law")
    print("=" * 60)
    print()
    
    # Initialize framework
    system = WeiwenLaw("AI Content Generator")
    
    # Set domain constant - what's the non-negotiable constraint?
    # In this case: content must be factually accurate
    system.set_domain_constant(
        R=10.0,
        description="Factual accuracy requirement (scale 1-10)"
    )
    
    # Set steady-state reserve - what are the subsystems?
    # Breaking down into: research depth, source quality, citation accuracy
    subsystems = {
        'research_depth': 7.5,
        'source_quality': 8.0,
        'citation_accuracy': 6.5  # Weakest link
    }
    system.set_steady_state_reserve(
        S=0,  # Will be computed as min
        description="Composite quality reserve",
        subsystems=subsystems
    )
    
    # Set perturbation - what disturbances exist?
    # Breaking down into: time pressure, conflicting sources, ambiguous query
    perturbation_sources = {
        'time_pressure': 3.0,
        'conflicting_sources': 4.5,  # Strongest disturbance
        'ambiguous_query': 2.0
    }
    system.set_perturbation(
        D=0,  # Will be computed as max
        description="Operational disturbances",
        perturbation_sources=perturbation_sources
    )
    
    # Set lever - how much action intensity are we applying?
    # In this case: verification effort
    system.set_lever(
        H=2.0,
        description="Verification effort multiplier"
    )
    
    # Compute steady-state
    M = system.compute_steady_state()
    
    print(system.get_summary())
    print()
    
    # Audit the result
    print("--- AUDIT REPORT ---")
    audit = system.audit_backward()
    print(json.dumps(audit, indent=2))
    print()
    
    # Projection: What if we increase verification effort?
    print("--- PROJECTION: Increase verification effort to H=3.0 ---")
    projection = system.project_forward(new_H=3.0)
    print(f"Current M: {projection['current_state']['M']:.4f}")
    print(f"Projected M: {projection['projected_state']['M']:.4f}")
    print(f"Change: {projection['delta_M']:+.4f}")
    print(f"Stability: {projection['stability_change']}")
    print(f"Recommendation: {projection['recommendation']}")
    print()
    
    # Projection: What if disturbance increases?
    print("--- PROJECTION: Disturbance increases to D=6.0 ---")
    projection2 = system.project_forward(new_H=3.0, new_D=6.0)
    print(f"Projected M: {projection2['projected_state']['M']:.4f}")
    print(f"Stability: {projection2['stability_change']}")
    print(f"Recommendation: {projection2['recommendation']}")
    print()
    
    print("--- FULL AUDIT LOG ---")
    print(system.export_audit_log())


if __name__ == "__main__":
    demo_ai_audit()
