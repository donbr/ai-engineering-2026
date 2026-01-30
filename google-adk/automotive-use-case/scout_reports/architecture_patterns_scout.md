# Architecture Diagram Patterns Scout Report

## DIAGRAM VIEW TYPES

### Conceptual View
- **Purpose**: High-level system overview for executives and stakeholders
- **Focus**: System purpose, key components, and business alignment
- **When to use**: Early planning, stakeholder communication, business cases
- **Characteristics**: No implementation details, shows relationships not flows

### Logical View
- **Purpose**: Describes how the solution works functionally
- **Focus**: Application connectivity, data flows, component sequences
- **When to use**: Solution architecture, development guidance, troubleshooting
- **Characteristics**: Shows "how" without code references; basis for physical design

### Physical View
- **Purpose**: Detailed infrastructure and deployment specifics
- **Focus**: Servers, VMs, containers, networks, zones, connectivity
- **When to use**: Implementation, operations, capacity planning
- **Characteristics**: Technology-specific, deployment-ready details

**Best Practice**: Layer progressively - context diagram leads to container diagram, which leads to component diagrams for critical use cases (C4 Model approach).

## EVOLUTION DIAGRAMS

### Before/After Comparison Patterns
- **Evolution Graphs**: Nodes represent complete architectural states; edges show possible transitions
- **Forward Design**: Diagrams before coding help visualize target state
- **Backward Design**: Diagrams after coding document actual implementation

### Showing System Changes
- Use side-by-side comparison for clear before/after visualization
- Highlight changed components with color or annotation
- Document rationale for architectural decisions using ADRs (Architecture Decision Records)
- Consider "Diagram as Code" tools for version-controlled evolution tracking

### Key Principle
Capture actual architecture before migration; maintain accuracy afterward to prevent drift and technical debt accumulation.

## CLOUD/EDGE PATTERNS

### Edge Hybrid Architecture
- **Visual Convention**: Edge components at network perimeter, cloud services centrally
- **Communication Patterns**:
  - Unidirectional: Use gated ingress pattern
  - Bidirectional: Use gated egress + gated ingress pattern

### Common Hybrid Patterns
| Pattern | Use Case |
|---------|----------|
| Tiered Hybrid | Application tiers distributed across clouds |
| Partitioned Multi-Cloud | Different functions on different clouds |
| Edge Hybrid | Local processing for time-critical, cloud for other workloads |
| Meshed | All systems can communicate across environments |

### Visual Conventions
- Use layered architecture: edge devices, edge gateways, cloud services, orchestration
- Show API gateways as integration points
- Distinguish synchronous (solid lines) vs asynchronous (dashed lines) communication
- Include legends for line/border semantics

## FILE ORGANIZATION

### Single File
- **When**: Simple systems, overview documents, quick reference
- **Pros**: Single source of truth, easy to share
- **Cons**: Becomes unwieldy at scale, harder to maintain

### Multiple Files
- **When**: Complex systems, team collaboration, evolving documentation
- **Pros**: Single responsibility per file, easier comprehension, parallel editing
- **Cons**: Requires clear naming conventions and navigation structure

### Decision Criteria
| Factor | Single File | Multiple Files |
|--------|-------------|----------------|
| System complexity | Low | High |
| Team size | Small | Large |
| Update frequency | Rare | Frequent |
| Audience diversity | Uniform | Varied |

### Recommended Structure
```
docs/architecture/
  00_context.md          # System context (C4 Level 1)
  01_containers.md       # Container diagram (C4 Level 2)
  02_components/         # Component diagrams by domain
  03_deployment.md       # Physical/deployment view
  decisions/             # Architecture Decision Records
```

---

**Sources**: [vFunction Architecture Guide](https://vfunction.com/blog/architecture-diagram-guide/), [C4 Model](https://c4model.com/), [Google Cloud Hybrid Patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices), [Microsoft Azure Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/), [bool.dev Documentation Best Practices](https://bool.dev/blog/detail/architecture-documentation-best-practice)
