# Santa Claus Algorithm — Web Demo (Flask)

Live demo: **https://mayrozen45.csariel.xyz/**

This repository contains the **web application** (Flask + JavaScript + HTML/CSS) for running and visualizing an implementation of the **Santa Claus / Max–Min Fair Allocation** algorithm.  
Users enter a valuation matrix (how much each player values each item), and the app computes an allocation that aims to **maximize the minimum total value** received by any player.

> 📌 **Note:** The algorithm implementation is maintained as part of the **`fairpyx`** Python library.  
> This repo is the **website + UI layer** that calls the algorithm.

---

## What is the Santa Claus Problem?

Given:
- `n` players (kids)
- `m` indivisible items (gifts)
- a valuation value `v[i][j] ≥ 0` describing how much player `i` values item `j`

Goal: allocate items so that the **least happy player is as happy as possible**, i.e. maximize:

$$
\max \ \min_i \sum_{j \in S_i} v_{i,j}
$$

---

## Algorithm Overview

This project follows the approach from the paper **“Santa Claus Meets Hypergraph Matchings”**:

1. **Choose a threshold `t`** and ask: “Can every player receive value ≥ `t`?”
2. Solve a **Configuration LP** (a relaxation that allows fractional assignments).
3. Convert the fractional solution into a structured form (conceptually: **fat / thin** items and minimal bundles).
4. Build a **bipartite hypergraph**:
   - Left side: players  
   - Right side: items  
   - Hyper-edges represent *valid bundles* for a player
5. Use a **local search** procedure to find a (near) **perfect hypergraph matching**, which corresponds to a valid allocation.

In practice, this produces an allocation that is guaranteed (theoretically) to be within a constant factor of the LP optimum under the restricted-assignment setting.

---

## Web App — How It Looks & Works

The website is designed to be simple and interactive:

1. **Home screen**: choose the number of players and gifts (with validation: players ≤ items).
2. **Valuation input**: fill a matrix where each row is a player and each column is an item.
3. **Run**: the server calls the Python algorithm and returns:
   - the final allocation (which items each player got)
   - summary/fairness information (e.g., the minimum achieved value)

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Algorithm:** implemented in Python as part of **`fairpyx`**

---

## Related Repositories

- **This repo (Web App):**  
  https://github.com/MayRozen/App-Research-Algorithms

- **Algorithm library (`fairpyx`) — my fork:**  
  https://github.com/MayRozen/fairpyx

- **Upstream `fairpyx` (official / main):**  
  https://github.com/ariel-research/fairpyx

---

## Installation (Algorithm Library)

You can install the `fairpyx` library via pip:

```bash
pip install fairpyx
