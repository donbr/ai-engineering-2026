# Mermaid.js Syntax Scout Report

## KEY SYNTAX RULES

1. **Preamble Required**: Every diagram must start with a valid type declaration (e.g., `flowchart TD`, `graph LR`, `sequenceDiagram`)
2. **Direction Codes**: TB (top-bottom), BT (bottom-top), LR (left-right), RL (right-left)
3. **Node Shapes**: Use specific delimiters - `[]` square, `()` rounded, `([])` stadium, `[[]]` subroutine, `[()]` database, `{}` diamond, `{{}}` hexagon
4. **Edge Syntax**: `-->` arrow, `---` line, `-.->` dotted, `==>` thick, `--text-->` labeled
5. **Comments**: Use `%%` for inline comments
6. **Subgraphs**: Declare with `subgraph name` and close with `end`

## COMMON PITFALLS

| Issue | Cause | Solution |
|-------|-------|----------|
| Silent render failure | Special characters in node text | Wrap text in quotes: `id1["Text with (parens)"]` |
| Quote errors | Unescaped quotes in labels | Use entity codes: `#quot;` for `"` |
| Subgraph direction ignored | External links to internal nodes | Link to subgraph itself, not internal nodes |
| Complex graph syntax error | Too many nodes/edges | Validate with `mermaid.parse()` before render |
| LLM-generated errors | Invalid classDef or arrow syntax | Always test in [Mermaid Live Editor](https://mermaid.live) |
| Version mismatch | Features differ between v9/v10/v11 | Check target renderer's Mermaid version |

## BEST PRACTICES

1. **Define nodes first**: List all nodes with labels at the top, then define connections using IDs only
2. **Use classDef for styling**: `classDef green fill:#9f6,stroke:#333` then `class nodeA green`
3. **One concept per diagram**: Follow the "illustrate only one idea per diagram" principle
4. **Minimize edges**: Remove non-essential connections; redraw if flow is unclear
5. **Use subgraph direction**: Set `direction TB` inside subgraphs for independent layout control
6. **Document with comments**: Use `%%` to explain complex sections for team collaboration
7. **Test incrementally**: Build diagrams piece by piece, validating each addition

## COMPLEXITY GUIDELINES

| Metric | Threshold | Action |
|--------|-----------|--------|
| Nodes | >50 | Split into sub-diagrams |
| Edges/Connections | >100 | Performance degrades (O(n^2)); must split |
| Graph density | >0.3 | Too interconnected; simplify or split |
| Parallel branches | >8 | Exceeds working memory (Miller's Law); group or split |
| Cyclomatic complexity | >15 | Too many decision paths; decompose |

**When to Split:**
- Diagram illustrates more than one main concept
- LR diagrams have >10 nodes (text becomes unreadable)
- TB diagrams require excessive scrolling
- Rendering takes >2 seconds

**Alternative for Complex Layouts:** Consider ELK (Eclipse Layout Kernel) layout for advanced positioning when standard algorithms produce overlapping nodes.

---

*Sources: [Mermaid Official Docs](https://mermaid.js.org/intro/syntax-reference.html), [Mermaid Chart Blog - O(n^2) Complexity](https://docs.mermaidchart.com/blog/posts/flow-charts-are-on2-complex-so-dont-go-over-100-connections), [Mermaid-Sonar Complexity Analyzer](https://entropicdrift.com/blog/mermaid-sonar-complexity-analyzer/), [MkDocs-Mermaid2 Troubleshooting](https://mkdocs-mermaid2.readthedocs.io/en/latest/troubleshooting/)*
