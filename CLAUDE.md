# CLAUDE.md — InverseCSG Project

## What This Is

Modernized fork of [yijiangh/InverseCSG](https://github.com/yijiangh/InverseCSG) (SIGGRAPH Asia 2018). Converts 3D triangle meshes into CSG trees via program synthesis. Running on WSL Ubuntu.

See `PLAN.md` for the full implementation plan and task breakdown.

## Key Decisions

### Branch strategy (decided 2026-03-23)
- **`upstream-fixes`**: Clean fixes only (build fixes, bug fixes, dep upgrades). Used for PRs back to upstream. Branch from upstream's `master`.
- **`main`**: Our primary branch. Merges `upstream-fixes`, then adds extensions, eval tools, experiments.
- **Rule**: Upstream-worthy fixes go to `upstream-fixes` first, then merge forward into `main`. Never cherry-pick backwards from `main`.
- **Rationale**: Keeps `main` as the natural working branch (no constant switching), while `upstream-fixes` stays PR-ready. GitHub PRs work from any branch name.

### Fork source
- Primary upstream: `yijiangh/InverseCSG` (original authors)
- Reference fork: `jjjjulien/InverseCSG` (GCC 9 upgrade, eval scripts) — cherry-pick selectively, don't merge wholesale.

## Build & Run

```bash
# Install dependencies (once cloned)
python3 install.py -d build

# Run a single test
python3 run_tests.py build <model_name>

# Run full benchmark
python3 run_tests.py build
```

## Project Structure

C++ core in `cpp/`, Python pipeline scripts at root level, Sketch synthesizer in `sketch/`, benchmark models in `example/`, pre-computed solutions in `solution/`.
