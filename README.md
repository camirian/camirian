# Caaren Amirian

**Systems + verification engineer working on verifiable AI and Physical AI.**

I build evaluation and evidence workflows that make AI-agent and cyber-physical behavior independently inspectable: reproducible experiments, explicit verification contracts, failure analysis, provenance, robotics simulation, and requirements-to-evidence systems.

> **I verify AI systems — from coding agents to robots in simulation.**

## Flagship proof — Physical AI evaluation

### [Sim-to-Real Control Systems](https://github.com/camirian/sim-to-real-control-systems-public)

▶ **[Watch the 3:44 case study](https://www.youtube.com/watch?v=f5oMNBi78a8)** — the two runtime defects, the frozen campaign, and the 0/40 result.

A closed-loop Isaac Sim + ROS 2 Franka experiment with seeded sensor noise and causal filtering.

The current public campaign was preregistered: **20 seeds × 2 conditions = 40 scheduled runs**, frozen before the first run. All 40 then executed validly — with preserved raw evidence, reproducible paired analysis, and explicit claim boundaries.

- on the three headline paired metrics — tracking RMS, disturbance attenuation, and true articulation-position RMS — filtering won in **20/20 paired seeds**;
- **0/40 runs passed the full certification gauntlet**;
- the acceptance thresholds were **not relaxed after seeing the result**;
- simulation only — no physical-hardware, safety, certification, production-readiness, or real-world-transfer claim.

**Pinned case study:** [`M4_CASE_STUDY.md` @ `24bf738`](https://github.com/camirian/sim-to-real-control-systems-public/blob/24bf7388e806e9f49f3bee93f754b2b4c00953ff/docs/M4_CASE_STUDY.md) — the fixed evidence-backed record for these campaign claims.

That distinction is intentional: execution success and metric improvement are evidence, not permission to overclaim.

## Verifiable AI & agent evidence

- [Fieldheld Recorder](https://github.com/camirian/fieldheld-recorder) — independent evidence for AI-assisted software changes.
- [Agentic Systems Verifier — Case Study](https://github.com/camirian/agentic-systems-verifier-case-study) — sanitized verification case study.
- [Repo Preflight Drift Scanner](https://github.com/camirian/repo-preflight-drift-scanner) — small verification tooling for repository drift/preflight checks.

I am also working privately on fail-closed AI evaluation, verifier disagreement, quarantine, provenance, and AI-scaffolding experiments. Public artifacts will be released only after their evidence, privacy, and claim-review gates are satisfied rather than exposing private working history prematurely.

## Physical AI & robotics support

- [Articulated Robot Manipulation](https://github.com/camirian/articulated-robot-manipulation-public) — Franka Panda manipulation and robotics integration in Isaac Sim.
- [Robotics Ontology](https://github.com/camirian/robotics-ontology-public) — robotics terminology, interfaces, and systems/MBSE-style traceability examples.
- [Distributed Robotics Infrastructure](https://github.com/camirian/distributed-robotics-infrastructure-public) — supporting edge/host/cloud robotics architecture reference.

## What I care about

I am most interested in the engineering layer between **promising AI capability** and **trustworthy system use**:

- AI evaluation and verification;
- agent evidence and reproducibility;
- Physical AI / robotics simulation and sim-to-real evaluation;
- AI scaffolding, harnesses, tools, and evaluation loops;
- systems architecture, MBSE, traceability, and technical decision-making;
- failure modes, explicit uncertainty, and honest non-claims.

My public repositories are personal, clean-room work. They contain no employer, customer, classified, export-controlled, proprietary, or private operational material, and no employer endorsement is implied.

[YouTube](https://www.youtube.com/@CaarenAmirian) · [X](https://x.com/CaarenAmirian) · [LinkedIn](https://www.linkedin.com/in/caaren-amirian) · [Reddit](https://www.reddit.com/user/CaarenAmirian/)
