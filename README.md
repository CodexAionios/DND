# Neuroscience for Ocular Health — Research Repo

This repository consolidates the full project for exploring how chronic blue‑enriched visual stimulation shapes the eye–brain system, including the working hypothesis that **blue light–driven gamma oscillations** can induce **activity‑dependent cortical contraction**, with downstream effects on **folding**, **ion demands (Na⁺/K⁺)**, **attention**, and **behavioral economics of craving** (e.g., sodium preference) under modern digital exposure.

The repo is organized to make it easy to reproduce experiments, collect data, analyze biomarkers (pupillometry/EEG/EMG), and publish preprints. It also hosts the **AVA+RSU protocol** for antideepfake visual acuity training with safe exposure budgets.

## Quickstart

1. Create a Python environment and install requirements:

   ```bash
   uv venv && source .venv/bin/activate  # or: python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run a dry test of RSU calculation and generate a toy report:

   ```bash
   python scripts/run_rsu_demo.py
   ```

3. Explore the docs in `docs/` and protocols in `docs/protocols/`.

## Core hypothesis (research kernel)

- Blue light (~460–480 nm) biases visual and arousal circuits toward sustained **gamma**.
- Sustained gamma increases energetic load and **Na⁺/K⁺-ATPase** activity, shifting ion homeostasis and autonomic tone.
- Prolonged regimes may correlate with **localized cortical thickening/folding** and measurable changes on MRI/DTI.
- Behavioral outputs manifest as short‑term attention gains, long‑term fatigue, narrowed focus, and potentially a **sodium‑seeking** dietary bias via dopaminergic reinforcement.
- Clinical and public‑health interfaces include **digital eye strain**, **blink suppression**, **tear‑film instability**, **myopia risk**, and **sleep/circadian** disruption.

## Folder map

```
docs/              — protocols, specifications, ethics, reviews (incl. DND 2008–2024)
src/               — Python packages: rsu/ (metric) and avarsu/ (training)
experiments/       — YAML configs for runs
scripts/           — entrypoints for data collection and analysis
data/              — raw/ processed/ external/ (git‑ignored by default)
notebooks/         — exploratory analysis (placeholders)
reports/           — paper‑ready figures and tables
tests/             — unit tests for metrics/pipelines
.github/workflows/ — CI: lint, tests
```

## Citing

If this work informs your research, please cite using the `CITATION.cff` metadata or the preprints in `docs/specs` once published.
