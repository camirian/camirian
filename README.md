# Caaren Amirian | MBSE & Systems Architecture | Pioneering AI for Digital Transformation

<p align="left">
  <a href="https://www.linkedin.com/in/caaren-amirian/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://www.youtube.com/@CaarenAmirian" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/></a>
</p>

An award-winning systems architect and applied AI innovator with over 9 years of experience designing the future of complex, safety-critical systems. I specialize in the synthesis of formal Model-Based Systems Engineering (MBSE) and the hands-on development of generative AI solutions. I am driven by the challenge of applying my deep background in systems-of-systems architecture and functional safety to solve the next generation of complex engineering problems.

---

### 🏗️ Systems Architecture & Physical AI

My work integrates formal systems modeling with agentic AI to bridge the gap between digital simulation and physical reality.

```mermaid
graph TD
    subgraph "Digital Twin / Simulation"
      Isaac["NVIDIA Isaac Sim"]
      USD["OpenUSD Assets"]
      Isaac -->|Sensors & Physics| ROS2
    end

    subgraph "Physical Intelligence / Agentic Layer"
      LLM["Multimodal LLM (Gemini/LlaVA)"]
      RAG["RAG Knowledge Base"]
      Planner["Agentic Planner"]
      LLM <--> RAG
      Planner <--> LLM
    end

    subgraph "Robot Control / Execution"
      ROS2["ROS 2 Humble Middleware"]
      Nav["Nav2 & MoveIt"]
      Hardware["Jetson Orin / Physical Robot"]
      ROS2 <--> Nav
      Nav --> Hardware
    end

    Planner -->|High-Level Commands| ROS2
    ROS2 -->|State Feedback| Planner
