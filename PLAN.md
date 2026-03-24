# InverseCSG — Implementation Plan

## Paper Summary

**InverseCSG** (Du et al., SIGGRAPH Asia 2018, MIT) takes a **3D triangle mesh** as input and reverse-engineers it into a **CSG tree** — a compact program of boolean operations (union, intersection, subtraction) on geometric primitives (spheres, cylinders, cuboids, tori). It frames this as a **program synthesis** problem.

## Pipeline (4 Stages)

| Stage | What it does | Key tools/methods |
|-------|-------------|-------------------|
| **1. Primitive Detection** | Detect surface primitives from mesh via RANSAC + graph-cut, build solid primitives | Efficient RANSAC, graph-cut optimization |
| **2. Sampling** | Sample points, classify inside/outside, reduce to one per canonical intersection term | Uniform sampling, inside/outside mesh queries |
| **3. Synthesis** | Find minimal CSG tree via SAT-based program synthesis (CEGIS) with divide-and-conquer for large inputs | Sketch synthesizer, HAC clustering |
| **4. Post-Processing** | Simplify tree, detect symmetries for re-parameterization | Rule-based simplification |

## Approach: Fork + Modernize on WSL Ubuntu

An official implementation exists at **[yijiangh/InverseCSG](https://github.com/yijiangh/InverseCSG)** — a complete C++/Python/OpenSCAD codebase with all 4 stages, vendored GCO, 50 benchmark models, and Sketch integration. It targets **Ubuntu 14.04/16.04** and was last updated Sept 2020.

A research fork at **[jjjjulien/InverseCSG](https://github.com/jjjjulien/InverseCSG)** (active through May 2025) adds evaluation scripts (Chamfer distance, normal consistency via Open3D), a mesh repair utility, expanded test cases, and a GCC 6→9 upgrade.

**Strategy**: **Fork** `yijiangh/InverseCSG` on GitHub to create our own repository. This project then focuses on **modernizing the fork**: updating dependencies to current versions, fixing bitrot and known bugs, verifying correctness on the benchmark suite, and documenting the process. Using WSL Ubuntu means the upstream code should build with minimal changes — the main work is upgrading outdated deps and fixing issues.

**Benefits of forking**:
- Clean separation between upstream code and our modernization commits
- Ability to submit fixes back as PRs to the original repo
- Proper git history tracking all changes we make
- Easy to pull in future upstream updates if any appear

## Platform

- **WSL Ubuntu** on Windows 11
- GCC 9+ (following jjjjulien's upgrade from GCC 6)
- Native Linux environment — no cross-platform porting needed

## Existing Codebase Structure (upstream)

```
yijiangh/InverseCSG/
├── cpp/                           # C++ core
│   ├── CMakeLists.txt
│   ├── src/
│   │   ├── ransac/                # Stage 1: RANSAC primitive detection
│   │   ├── primitive/             # Solid primitive types
│   │   ├── mesh/                  # Mesh I/O and operations
│   │   └── vsa/                   # Variational shape approximation
│   └── lib/
│       └── gco-v3.0/              # Vendored graph-cut library
├── sketch/                        # Sketch synthesis framework files
├── example/                       # 50 benchmark input models (.off meshes)
├── solution/                      # Pre-computed CSG solutions (.scad)
├── install.py                     # Automated installer (apt-get, CGAL, Eigen, Sketch)
├── main.py                        # Pipeline entry point
├── run_tests.py                   # Test runner
├── sketch_pipeline.py             # Stage 3: Sketch processing
├── point_cloud_seg.py             # Point cloud segmentation
├── primitive_to_sketch.py         # Primitive → Sketch conversion
├── surface_primitive_to_sketch.py # Surface primitive → Sketch
├── helper.py                      # Utility functions
└── transforms.py                  # Geometric transforms
```

## Potential Issues to Fix

| Component | Issue | Fix strategy |
|-----------|-------|-------------|
| **install.py** | Targets GCC 6, Ubuntu 14.04 packages | Update to GCC 9+ (per jjjjulien fork), modern Ubuntu packages |
| **CGAL 4.12** | Pinned to old version, may not compile with modern GCC | Upgrade to CGAL 5.x via apt or source, adapt any API changes |
| **Eigen 3.3.4** | Pinned to old version | Use system Eigen3 (`apt install libeigen3-dev`) |
| **Sketch synthesizer** | Built from source via Java/Maven, may have bitrot | Verify build with current Java/Maven versions |
| **Known bug** | AgglomerativeClustering crash with 1 sample (issue #1) | Guard `n_clusters` in divide-and-conquer logic |
| **Python** | May assume Python 3.7 specifics | Test with Python 3.10+ (current WSL Ubuntu default) |

## Branch Strategy

- **`upstream-fixes`** — Branched from upstream's `master`. Contains only clean, upstream-compatible changes: dependency upgrades, bug fixes, build fixes. This branch is used to create PRs back to `yijiangh/InverseCSG`. Keep it surgically clean.
- **`main`** — Our primary working branch. Merges `upstream-fixes` as a base, then adds everything else: extensions from jjjjulien fork, evaluation tools, new features, Claude Code artifacts, experiments. This is the default branch and where day-to-day work happens.

**Rule**: Make upstream-worthy fixes on `upstream-fixes` first, then merge into `main` — never cherry-pick backwards out of `main`.

## Cherry-picks from jjjjulien fork

**→ `upstream-fixes` branch** (fixes/upgrades):
- GCC 6 → 9 upgrade in `install.py`

**→ `main` branch** (new features, after merging `upstream-fixes`):
- `fix_mesh_watertight.py` — mesh repair utility (trimesh-based)
- `evaluator.py` — Chamfer distance, normal consistency metrics (Open3D-based)
- `batch_evaluation.py` — batch evaluation with Light Field Distance
- Expanded test cases for ABC dataset

## Implementation Tasks

### Task 1: Fork, clone, and WSL environment setup
Fork `yijiangh/InverseCSG` on GitHub. Clone the fork into this project directory. Set up WSL Ubuntu environment and install base system dependencies (`build-essential`, `cmake`, `git`, `python3`, `java`, `maven`). Audit the codebase to catalog all files, dependencies, and build steps.

### Task 2: Modernize dependencies and build
Apply GCC 9+ upgrade (from jjjjulien fork). Update `install.py` for modern Ubuntu: fix package names, upgrade CGAL to 5.x, use system Eigen3. Run `python3 install.py -d build` and fix any issues until C++ builds and Sketch compiles successfully. Commit each fix as a separate, well-documented commit.

### Task 3: Fix known bugs
Fix the AgglomerativeClustering crash (upstream issue #1) where `n_clusters` exceeds the number of samples. Add guard in the divide-and-conquer logic. Fix any other Python compatibility issues with modern Python 3.10+.

### Task 4: End-to-end verification on simple model
Run the full pipeline on a simple benchmark model (e.g., `one_cube`): `python3 run_tests.py build one_cube`. Verify output `.scad` matches the pre-computed solution. Debug and fix any runtime issues.

### Task 5: Cherry-pick evaluation tools (→ `main` branch)
Merge `upstream-fixes` into `main`. Bring in additions from jjjjulien fork: (a) `fix_mesh_watertight.py`, (b) evaluation scripts with Chamfer distance and normal consistency, (c) install additional Python deps (`trimesh`, `open3d`, `scipy`). These live on `main` alongside all other extensions.

### Task 6: Full benchmark run (on `upstream-fixes`)
Run the complete 50-model benchmark suite on `upstream-fixes` branch. Record success rate, runtime, and output quality. Document any models that fail and diagnose issues. This validates the modernized upstream before adding extensions.

## Dependency Graph

```
Task 1 (fork + WSL setup + clone)
  └── Task 2 (modernize deps + build) [upstream-fixes]
        └── Task 3 (fix bugs) [upstream-fixes]
              └── Task 4 (e2e verification) [upstream-fixes]
                    ├── Task 5 (merge upstream-fixes → main, add eval tools) [main]
                    └── Task 6 (full benchmark) [upstream-fixes]
```

## Dependencies (all installed via apt + pip in WSL Ubuntu)

| Dependency | Purpose | Installation |
|-----------|---------|-------------|
| **GCC 9+** | C++ compiler | `apt install gcc-9 g++-9` |
| **CMake** | Build system | `apt install cmake` |
| **CGAL** | Mesh processing, RANSAC | `apt install libcgal-dev` or source build |
| **Eigen3** | Linear algebra | `apt install libeigen3-dev` |
| **Java JDK 8+** | Sketch synthesizer runtime | `apt install default-jdk` |
| **Maven 3.x** | Builds Sketch from source | `apt install maven` |
| **GCO (gco-v3.0)** | Graph-cut optimization | Vendored in repo |
| **Python 3.8+** | Pipeline orchestration | `apt install python3` |
| **scikit-learn** | HAC clustering | `pip install scikit-learn` |
| **trimesh** | Mesh repair | `pip install trimesh` |
| **open3d** | Evaluation metrics | `pip install open3d` |
| **OpenSCAD** | CSG rendering (optional, for visualization) | `apt install openscad` |
