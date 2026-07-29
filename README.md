# Caaren Amirian — Verifiable AI & Physical AI Systems

<p align="left">
  <a href="https://github.com/camirian" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.youtube.com/@CaarenAmirian" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/></a>
  <a href="https://x.com/CaarenAmirian" target="_blank"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X"/></a>
  <a href="https://www.linkedin.com/in/caaren-amirian" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

I build and study **evidence-bound AI and Physical AI systems**: systems that expose enough execution, evaluation, simulation, and provenance evidence for an independent reviewer or verifier to decide what can and cannot be trusted.

My current work connects four areas:

- **verifier-gated open models** — local inference, task routing, executable evaluation, and bounded fine-tuning research;
- **agent evidence and software reliability** — reconstructing what AI-assisted work changed, what was tested, what is missing, and what requires human review;
- **Physical AI and robotics simulation** — closed-loop simulation, ROS 2 integration, manipulation, deterministic scenario campaigns, and sim-to-real boundaries;
- **systems engineering and MBSE** — requirements, interfaces, traceability, verification, safety boundaries, and change-impact reasoning.

The common principle is:

> AI systems that produce software decisions or physical actions should expose enough evidence for independent review and bounded deployment decisions.

I publish clean-room personal work only. Nothing here contains or represents employer, customer, classified, export-controlled, proprietary, or private operational material, and no employer endorsement is implied.

---

## Current Focus

### Physical AI Flagship

[`sim-to-real-control-systems-public`](https://github.com/camirian/sim-to-real-control-systems-public) is the primary Physical AI proof surface.

It combines:

- NVIDIA Isaac Sim and ROS 2;
- a Franka closed-loop control scenario;
- seeded sensor disturbance injection;
- causal DSP filtering;
- tracking, settling, overshoot, and attenuation metrics;
- deterministic evidence packets;
- and a campaign-level filtered-versus-unfiltered comparison.

The current completion target is deliberately narrow: close the robot-command loop, run at least 20 filtered and 20 unfiltered seeded trials, preserve failures and raw evidence, generate the comparison table, and publish a concise limitations-aware demonstration.

The work does **not** claim real-world transfer, robot safety certification, production readiness, or regulatory approval.

### Open Verifier

Open Verifier is a private local research harness for verifiable open-model inference: deterministic scorers, task-class routing, council-plus-verification experiments, model evaluation, and carefully bounded fine-tuning.

It remains private while it completes a public-release gate covering:

- removal of private endpoints and machine-specific state;
- calibrated claims and reproducibility artifacts;
- model, dataset, and code provenance;
- security and contribution policies;
- clean-clone verification;
- and an explicit open-source license decision.

The narrower thesis is:

> On tasks with a credible verifier, generation and independent checking can be composed into a more reliable system. On open-ended tasks without a trustworthy oracle, the boundary must remain explicit.

### Public Contribution

I am prioritizing useful contributions to existing evaluation, observability, robotics, and simulation communities over creating more standalone repositories.

Relevant ecosystems include Inspect Evals, Hugging Face Lighteval, OpenTelemetry GenAI semantic conventions, ROS 2, NVIDIA Isaac, OpenUSD, LeRobot, and local-model runtimes.

I value:

- reproducible experiments over broad claims;
- raw evidence and negative results over polished demos alone;
- small upstream improvements over another platform architecture;
- and honest boundaries over artificial certainty.

---

## Public Projects

| Repository | What it demonstrates |
| --- | --- |
| [`sim-to-real-control-systems-public`](https://github.com/camirian/sim-to-real-control-systems-public) | Closed-loop Physical AI evaluation with Isaac Sim, ROS 2, seeded disturbances, DSP filtering, deterministic metrics, and evidence packets. |
| [`fieldheld-recorder`](https://github.com/camirian/fieldheld-recorder) | A stdlib-only CLI that turns coding-agent-style runs and public GitHub PR metadata into reviewable evidence bundles. The doer does not attest to its own success; verification is independent and fail-closed. |
| [`articulated-robot-manipulation-public`](https://github.com/camirian/articulated-robot-manipulation-public) | Franka Panda manipulation in Isaac Sim using Lula IK, PhysX, ROS 2, MoveIt 2, and a bounded perception example. |
| [`agentic-systems-verifier-case-study`](https://github.com/camirian/agentic-systems-verifier-case-study) | A sanitized systems-engineering case study connecting requirements, source context, verification records, and human review. |
| [`robotics-ontology-public`](https://github.com/camirian/robotics-ontology-public) | Executable domain vocabulary and architecture examples for robotics and cyber-physical systems. |
| [`distributed-robotics-infrastructure-public`](https://github.com/camirian/distributed-robotics-infrastructure-public) | A reference architecture for simulation, edge inference, robotics data, and deployment boundaries. |
| [`repo-preflight-drift-scanner`](https://github.com/camirian/repo-preflight-drift-scanner) | A bounded repository preflight tool for release hygiene and public-surface drift detection. |

These repositories are technical evidence and learning artifacts, not claims of customer adoption, certification, production safety, commercial operation, or validated real-world deployment.

---

## Demonstrations

| Demonstration | Watch |
| --- | --- |
| Articulated robot manipulation in Isaac Sim | [YouTube](https://www.youtube.com/watch?v=tvgWZHi6GRg) |
| Franka robot control with Python | [YouTube](https://www.youtube.com/watch?v=E2jNcWM_f08) |
| Sim-to-real control systems with ROS 2 and OmniGraph | [YouTube](https://www.youtube.com/watch?v=MfsuIWZ5_eg) |
| Fieldheld Recorder — reviewable evidence for autonomous coding-style work | [YouTube](https://www.youtube.com/watch?v=8C4pagZC91g) |
| Agentic Systems Verifier — requirements-to-verification workflow | [YouTube](https://www.youtube.com/watch?v=EoDpMjBUWmA) |

Future videos will emphasize real execution, benchmark design, measurable outcomes, failure analysis, limitations, and reproducibility rather than generic AI commentary.

---

## Technical Themes

- AI evaluation, executable verifiers, pass@k analysis, calibration, and held-out gates
- local open-weight models, quantization, routing, Ollama, llama.cpp, vLLM, and SGLang
- agent run evidence, review contracts, provenance, rollback boundaries, and unsupported-claim detection
- NVIDIA Isaac Sim, Isaac Lab, ROS 2, OmniGraph, Lula IK, PhysX, MoveIt 2, Jetson, and edge AI
- simulation campaigns, synthetic data, SIL/HIL thinking, sim-to-real validation boundaries, and robotics safety evidence
- MBSE, SysML-style traceability, requirements verification, digital twins, and change-impact reasoning
- Python, C++, Linux, Docker, GitHub Actions, and reproducible engineering workflows

---

## Fieldheld Status

[Fieldheld](https://fieldheld.com/) is a preserved personal research/project identity for evidence infrastructure. It is **not an active startup, product company, consulting service, customer operation, or sales program**.

Fieldheld Recorder remains public as a technical artifact. Private Fieldheld, Hermetic, Atlas, and related work are preserved but are not part of an active commercial program.

---

## Public Work Standard

For every result I publish, I aim to make clear:

1. what question was tested;
2. what code, data, models, simulation, and hardware were used;
3. what was actually observed;
4. what failed or remained uncertain;
5. how another person can reproduce it;
6. and what the evidence does **not** support.

GitHub is the source of truth for code and evidence. YouTube shows execution. X and Reddit are for technical conversation and learning from existing communities.
