"""
Weiwen's Law Interactive — AI Causal Logic Engine
==================================================

An interactive web tool that uses Weiwen's Law (KISS's Law) framework
to analyze claims, decisions, and systems through causal chain reasoning.

Usage:
    pip install gradio openai
    python app.py

Then open http://127.0.0.1:7860 in your browser.

Copyright (c) 2026 Xia Qi (夏祺). All rights reserved.
Software Copyright Registration No.: 2026SR0748746
ORCID: https://orcid.org/0009-0002-1433-6982
"""

import gradio as gr
from openai import OpenAI

# ═══════════════════════════════════════════════════════════════
# Provider Presets (OpenAI-compatible API endpoints)
# ═══════════════════════════════════════════════════════════════

PROVIDERS = {
    "OpenAI": "https://api.openai.com/v1",
    "DeepSeek": "https://api.deepseek.com/v1",
    "Qwen (DashScope)": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "SiliconFlow": "https://api.siliconflow.cn/v1",
    "Custom": "",
}

# ═══════════════════════════════════════════════════════════════
# System Prompt — Top-level framework for causal reasoning
# The complete system is contained in the architecture diagrams
# in /maps. This prompt encodes only the surface framework.
# ═══════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are an AI operating under Weiwen's Law (KISS's Law) — an AI Causal Logic Engine.

Your task is to analyze any input through a structured causal chain. You do NOT explain what causality is. You execute analysis according to causal structure.

## Core Formula

    M = (R × S) / (D × H)

## Variables

- **R (Domain Constant):** The rigid boundary of the operational domain. What are the non-negotiable requirements and constraints?
- **S (Steady-state Reserve):** The minimum value across all subsystems. Weakest link determines the ceiling. Identify all subsystems, find the minimum.
- **D (Perturbation):** The maximum disturbance across all sources. Strongest hit determines stress. Identify all disturbance sources, find the maximum.
- **H (Lever):** Observable action intensity — the subjective leverage point. Where can intervention actually change the outcome?
- **M (Steady-state Outcome):** The auditable and projectable result.

## Three Iron Rules

1. **No Skipping** — The causal chain R → S → D → H → M cannot be bypassed. Every variable must be addressed.
2. **No Reversal** — The sequence order R → S → D → H → M is fixed. Do not analyze them out of order.
3. **No Discontinuity** — Every link must maintain causal connectivity. If a link is weak or missing, flag it explicitly.

## Analysis Protocol

When the user submits a claim, decision, scenario, or system for analysis:

### Step 1 — Domain (R)
Identify the operational domain. What are the rigid constraints? What defines the boundary of this analysis?

### Step 2 — Subsystems (S)
List all relevant subsystems or components. Identify the weakest one (minimum reserve). This sets the ceiling.

### Step 3 — Disturbances (D)
Identify all disturbance sources. Find the strongest one (maximum perturbation). This sets the stress.

### Step 4 — Leverage (H)
Where can action actually change the outcome? What is the current intervention intensity? Is it sufficient?

### Step 5 — Compute (M)
Based on R, S, D, H: what is the steady-state outcome? Is the system stable or at risk?

### Step 6 — Causal Integrity
Trace the full chain R → S → D → H → M. Flag any broken, weak, or assumed links.

## Response Format

Always respond in this structure:

```
## 🔍 Weiwen's Law Analysis

### Input Summary
[One-line restatement of what is being analyzed]

### Causal Chain

**R (Domain Constant):**
[Domain and constraints]

**S (Steady-state Reserve):**
| Subsystem | Assessment |
|-----------|------------|
| [name]    | [rating]   |
| ...       | ...        |
→ Weakest link: [identification]

**D (Perturbation):**
| Source | Severity |
|--------|----------|
| [name] | [rating] |
| ...    | ...      |
→ Strongest hit: [identification]

**H (Lever):**
[Available interventions and current intensity]

**M (Steady-state Outcome):**
[Computed assessment with reasoning]

### Causal Integrity Check
| Link | Status | Notes |
|------|--------|-------|
| R→S  | ✅/⚠️/❌ | [note] |
| S→D  | ✅/⚠️/❌ | [note] |
| D→H  | ✅/⚠️/❌ | [note] |
| H→M  | ✅/⚠️/❌ | [note] |

### ⚡ Recommendations
1. [Specific, actionable step]
2. [Specific, actionable step]
```

## Projection Mode
If the user asks "what if" or "how to improve":
- Hold R, S, D constant
- Vary H (the leverage point)
- Project the new M
- Recommend specific interventions

## Key Reminders
- Always be specific, not generic.
- Name actual subsystems, actual disturbances, actual leverage points.
- If a link is weak or missing, say so clearly — do not fill gaps with assumptions.
- Respond in the same language the user writes in.
- The complete Weiwen's Law framework is documented at: https://github.com/Shaky77/KISS-s_Law (English) / https://github.com/Shaky77/Weiwen-s_Law (中文)
"""

# ═══════════════════════════════════════════════════════════════
# API Call
# ═══════════════════════════════════════════════════════════════

def call_api(api_key, base_url, model, messages, temperature=0.7):
    """Call an OpenAI-compatible API."""
    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

# ═══════════════════════════════════════════════════════════════
# Analysis Functions
# ═══════════════════════════════════════════════════════════════

def analyze(input_text, api_key, provider_choice, custom_url, model):
    """Run a structured Weiwen's Law causal analysis."""
    if not input_text.strip():
        return "⚠️ Please enter a claim, decision, scenario, or system to analyze."
    if not api_key.strip():
        return "⚠️ Please enter your API Key."

    base_url = custom_url.strip() if provider_choice == "Custom" else PROVIDERS.get(provider_choice, "")
    if not base_url:
        return "⚠️ Please select a provider or enter a custom API base URL."

    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": (
                "Please analyze the following using Weiwen's Law causal chain framework. "
                "Follow the structured analysis protocol step by step.\n\n"
                f"---\n\n{input_text}"
            )},
        ]
        return call_api(api_key, base_url, model, messages, temperature=0.7)
    except Exception as e:
        return f"❌ API Error: {type(e).__name__}: {e}"


def chat(message, history, api_key, provider_choice, custom_url, model):
    """Free-form conversation with Weiwen's Law reasoning."""
    if not message.strip():
        return history
    if not api_key.strip():
        return history + [[message, "⚠️ Please enter your API Key in the Configuration section above."]]
    if not history:
        history = []

    base_url = custom_url.strip() if provider_choice == "Custom" else PROVIDERS.get(provider_choice, "")
    if not base_url:
        return history + [[message, "⚠️ Please select a provider or enter a custom API base URL."]]

    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for h_user, h_assistant in history:
            messages.append({"role": "user", "content": h_user})
            if h_assistant:
                messages.append({"role": "assistant", "content": h_assistant})
        messages.append({"role": "user", "content": message})

        response = call_api(api_key, base_url, model, messages, temperature=0.7)
        history.append((message, response))
        return history
    except Exception as e:
        return history + [[message, f"❌ API Error: {type(e).__name__}: {e}"]]

# ═══════════════════════════════════════════════════════════════
# Example Presets
# ═══════════════════════════════════════════════════════════════

EXAMPLES = {
    "AI Claim Audit": (
        "Audit this AI-generated health claim: "
        "\"Drinking 8 glasses of water daily prevents all kidney diseases.\" "
        "Analyze its causal integrity."
    ),
    "Decision Analysis": (
        "I'm considering switching my career from finance to AI engineering. "
        "I have 5 years of finance experience, no coding background, "
        "and need to support a family. Analyze this decision."
    ),
    "System Risk Assessment": (
        "Analyze our company's customer service system for stability risks: "
        "3 support agents, 5000 daily tickets, one legacy CRM with frequent outages, "
        "no backup plan. Current satisfaction: 60%. Target: 90%."
    ),
    "Policy Projection": (
        "Project the outcome: A city reduces hospital beds by 30% to cut costs. "
        "Current bed utilization: 85%. Population growing 2% per year. "
        "What is the steady-state outcome?"
    ),
}

# ═══════════════════════════════════════════════════════════════
# Gradio Interface
# ═══════════════════════════════════════════════════════════════

def build_app():
    with gr.Blocks(
        title="Weiwen's Law — AI Causal Logic Engine",
        theme=gr.themes.Soft(),
        css=".footer-links { text-align: center; margin-top: 1em; color: #888; font-size: 0.85em; }"
    ) as app:

        gr.Markdown("""
# 🔍 Weiwen's Law — AI Causal Logic Engine

Analyze claims, decisions, and systems through structured causal reasoning.
Based on the **R → S → D → H → M** causal chain framework.

> Not teaching AI *what* causality is — enabling AI to *execute directly* according to causal structure.
        """)

        # ── Configuration ──
        with gr.Accordion("⚙️ API Configuration", open=False):
            api_key = gr.Textbox(
                label="API Key",
                type="password",
                placeholder="sk-...",
                info="Your key is used locally and never stored or transmitted elsewhere."
            )
            with gr.Row():
                provider = gr.Dropdown(
                    choices=list(PROVIDERS.keys()),
                    value="DeepSeek",
                    label="Provider"
                )
                model = gr.Textbox(
                    label="Model",
                    value="deepseek-chat",
                    info="Model name (e.g. deepseek-chat, gpt-4o-mini, qwen-plus)"
                )
            custom_url = gr.Textbox(
                label="Custom API Base URL",
                placeholder="https://your-api.com/v1",
                info="Only used when Provider is set to 'Custom'",
                visible=True
            )

        def on_provider_change(choice):
            if choice == "Custom":
                return gr.update(visible=True)
            return gr.update(visible=False, value="")

        provider.change(on_provider_change, provider, custom_url)

        # ── Tabs ──
        with gr.Tabs():

            # Tab 1: Structured Analysis
            with gr.TabItem("📊 Causal Analysis"):
                gr.Markdown(
                    "Enter a claim, decision, scenario, or system to analyze. "
                    "The AI will trace the full **R → S → D → H → M** causal chain."
                )
                analysis_input = gr.Textbox(
                    label="Input",
                    lines=4,
                    placeholder="Paste a claim to audit, describe a decision to analyze, "
                                "or outline a system to assess..."
                )
                with gr.Row():
                    for name, text in EXAMPLES.items():
                        def make_handler(example_text):
                            return lambda: example_text
                        gr.Button(name, size="sm").click(
                            fn=make_handler(text),
                            inputs=None,
                            outputs=analysis_input
                        )
                analyze_btn = gr.Button("🔍 Analyze", variant="primary", size="lg")
                analysis_output = gr.Markdown(
                    label="Analysis Result",
                    value="*Analysis result will appear here.*"
                )
                analyze_btn.click(
                    fn=analyze,
                    inputs=[analysis_input, api_key, provider, custom_url, model],
                    outputs=analysis_output
                )

            # Tab 2: Free Chat
            with gr.TabItem("💬 Free Chat"):
                gr.Markdown(
                    "Chat freely. The AI reasons through Weiwen's Law's causal framework "
                    "for every response."
                )
                gr.ChatInterface(
                    fn=chat,
                    additional_inputs=[api_key, provider, custom_url, model],
                    type="messages",
                    examples=[
                        ["What makes Weiwen's Law different from other risk frameworks?"],
                        ["How would you evaluate an AI system's reliability using causal chain analysis?"],
                    ],
                )

        # ── Footer ──
        gr.Markdown(
            "---\n"
            "<div class='footer-links'>\n"
            "Weiwen's Law (KISS's Law) — Keep Integrity & Steady State\n\n"
            "[📦 English Repo](https://github.com/Shaky77/KISS-s_Law) · "
            "[📦 中文仓库](https://github.com/Shaky77/Weiwen-s_Law) · "
            "[🆔 ORCID](https://orcid.org/0009-0002-1433-6982)\n\n"
            "Copyright © 2026 Xia Qi (夏祺). Licensed under AGPL-3.0.\n\n"
            "*The complete framework is defined in the architecture diagrams. "
            "This tool implements the surface-level reasoning — for the full system, "
            "see the [diagrams](https://github.com/Shaky77/KISS-s_Law/tree/main/maps).*\n"
            "</div>",
        )

    return app


# ═══════════════════════════════════════════════════════════════
# Launch
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = build_app()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )
