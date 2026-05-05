# F_holoindex Roadmap

## Vision

F_holoindex is not a library — it is a **FoundUp** whose purpose is to serve as the **pAVS Federation Brain**.

Every FoundUp publishes patterns. Every FoundUp queries the federation. When 012 has an idea, 0102 queries F_holoindex first: "Does this already exist?"

## Architecture

```
012 has idea
│
▼
0102 ───────────► F_holoindex (Federation)
│                    │
│                    ▼
│              Pattern DAEs (WRE)
│              - All FoundUp patterns indexed
│              - Cross-repo relationships
│              - Solution templates
│                    │
│◄───────────────────┘
│         "gotjunk has 80% of this"
│         "extend science-swarm module X"
│         "greenfield approved"
▼
012 decides
```

## Phases

| Phase | Status | Description |
|-------|--------|-------------|
| P0: Package Extraction | ✅ DONE | Standalone pip-installable core |
| P1: Federation Architecture | 🔜 NEXT | Cross-FoundUp index, publish/query protocol |
| P2: Pattern DAEs | 📋 PLANNED | WRE learning across all FoundUps |
| P3: FoundUp Integrations | 📋 PLANNED | gotjunk, autopost, science-swarm, GeozeAI |
| P4: Anti-Vibecode Gate | 📋 PLANNED | Mandatory query before greenfield builds |

## How FoundUps Connect

Each FoundUp:
1. Indexes itself locally (own patterns)
2. Publishes patterns to F_holoindex federation
3. Queries federation before building new

## Internal / External Concatenation

| Internal (Foundups-Agent) | External (F_holoindex) |
|---|---|
| `holo_index/` = PoC, dev, TurboQuant experiments | Production federation brain |
| Publishes TO federation | IS the federation |
| Consumer | Provider |
| Keep iterating here | Stable core, federation features |

**Bridge:** Internal publishes its 20K symbol index to F_holoindex. Other FoundUps do the same. Federation grows.

## Plan Moving Forward

- **Now:** ROADMAP.md added ✅
- **P1:** Design federation publish/query protocol (MCP? API? Shared ChromaDB?)
- **P2:** Pattern DAEs spec — what do they learn, how do they store?
- **P3:** First consumer (gotjunk) publishes + queries
- **P4:** Anti-vibecode gate wired into 0102 workflow

## Related WSPs

- WSP 84: Code Reuse
- WSP 97: Truth Boundaries
- WSP 103: pAVS MCP Tools
- WSP 104: FoundUp Independence
