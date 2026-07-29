# Caaren Amirian — Verifiable AI Systems · Local Models · Systems Engineering

<p align="left">
  <a href="https://github.com/camirian" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.youtube.com/@CaarenAmirian" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/></a>
  <a href="https://x.com/CaarenAmirian" target="_blank"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X"/></a>
  <a href="https://www.linkedin.com/in/caaren-amirian" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

I build and study **evidence-bound AI systems**: systems that expose enough execution, evaluation, and provenance evidence for an independent reviewer or verifier to decide what can and cannot be trusted.

My current work connects three areas:

- **verifier-gated open models** — local inference, task routing, executable evaluation, and bounded self-improvement research;
- **agent evidence and software reliability** — reconstructing what AI-assisted work changed, what was tested, what is missing, and what requires human review;
- **synthetic cyber-physical evaluation** — robotics simulation, MBSE-style traceability, and requirements-to-evidence workflows.

I publish clean-room personal work only. Nothing here contains or represents employer, customer, classified, export-controlled, proprietary, or private operational material, and no employer endorsement is implied.

---

## Current Focus

### Open Verifier

A local research harness for verifiable open-model inference: deterministic scorers, task-class routing, council-plus-verification experiments, model evaluation, and carefully bounded self-improvement.

The repository is currently private while it completes a public-release gate covering:

- removal of private endpoints and machine-specific state;
- calibrated claims and reproducibility artifacts;
- model, dataset, and code provenance;
- security and contribution policies;
- clean-clone verification;
- and an explicit open-source license decision.

The goal is not to claim that local open models replace frontier systems. The narrower thesis is:

> On tasks with a trustworthy verifier, generation and independent checking can be composed into a more reliable system. On open-ended tasks without a credible oracle, the boundary must remain explicit.

### Public Contribution

I am prioritizing useful contributions to existing evaluation and observability communities over creating more standalone repositories. Relevant ecosystems include Inspect Evals, Hugging Face Lighteval, OpenTelemetry GenAI semantic conventions, and local-model runtimes.

I value:

- reproducible experiments over broad claims;
- raw evidence and negative results over polished demos alone;
- small upstream improvements over another platform architecture;
- and honest boundaries over artificial certainty.

---

## Public Projects

| Repository | What it demonstrates |
| --- | --- |
| [`fieldheld-recorder`](https://github.com/camirian/fieldheld-recorder) | A stdlib-only CLI that turns coding-agent-style runs and public GitHub PR metadata into reviewable evidence bundles. The doer does not attest to its own success; verification is independent and fail-closed. |
| [`agentic-systems-verifier-case-study`](https://github.com/camirian/agentic-systems-verifier-case-study) | A sanitized systems-engineering case study connecting requirements, source context, verification records, and human review. |
| [`sim-to-real-control-systems-public`](https://github.com/camirian/sim-to-real-control-systems-public) | A clean-room NVIDIA Isaac Sim and ROS 2 demonstration for synthetic sim-to-real interfaces and observable control behavior. |
| [`articulated-robot-manipulation-public`](https://github.com/camirian/articulated-robot-manipulation-public) | Franka Panda manipulation experiments in Isaac Sim using Lula IK and PhysX. |
| [`robotics-ontology-public`](https://github.com/camirian/robotics-ontology-public) | Executable domain vocabulary and architecture models for robotics and cyber-physical systems. |
| [`repo-preflight-drift-scanner`](https://github.com/camirian/repo-preflight-drift-scanner) | A bounded repository preflight tool for release hygiene and public-surface drift detection. |

These repositories are technical evidence and learning artifacts, not claims of customer adoption, certification, production safety, or commercial operation.

---

## Demonstrations

| Demonstration | Watch |
| --- | --- |
| Fieldheld Recorder — reviewable evidence for autonomous coding-style work | [YouTube](https://www.youtube.com/watch?v=8C4pagZC91g) |
| Agentic Systems Verifier — requirements-to-verification workflow | [YouTube](https://www.youtube.com/watch?v=EoDpMjBUWmA) |
| Articulated robot manipulation in Isaac Sim | [YouTube](https://www.youtube.com/watch?v=tvgWZHi6GRg) |
| Franka robot control with Python | [YouTube](https://www.youtube.com/watch?v=E2jNcWM_f08) |
| Sim-to-real control systems with ROS 2 and OmniGraph | [YouTube](https://www.youtube.com/watch?v=MfsuIWZ5_eg) |

Future videos will emphasize real execution, benchmark design, failure analysis, limitations, and reproducibility rather than generic AI commentary.

---

## Technical Themes

- AI evaluation, executable verifiers, pass@k analysis, calibration, and held-out gates
- local open-weight models, quantization, MoE routing, Ollama, llama.cpp, vLLM, and SGLang
- agent run evidence, review contracts, provenance, rollback boundaries, and unsupported-claim detection
- MBSE, SysML-style traceability, requirements verification, and change-impact reasoning
- NVIDIA Isaac Sim, ROS 2, OmniGraph, Lula IK, PhysX, Jetson, and edge AI hardware
- Python, C++, Linux, Docker, GitHub Actions, and reproducible engineering workflows

---

## Fieldheld Status

[Fieldheld](https://fieldheld.com/) is a preserved personal research/project identity for evidence infrastructure. It is **not an active startup, product company, consulting service, or customer operation**.

Fieldheld Recorder remains public as a technical artifact. Private Fieldheld, Hermetic, Atlas, and related work are preserved but are not part of an active commercial program.

---

## Public Work Standard

For every result I publish, I aim to make clear:

1. what question was tested;
2. what code, data, models, and hardware were used;
3. what was actually observed;
4. what failed or remained uncertain;
5. how another person can reproduce it;
6. and what the evidence does **not** support.

GitHub is the source of truth for code and evidence. YouTube shows execution. X and Reddit are for technical conversation and learning from existing communities.
