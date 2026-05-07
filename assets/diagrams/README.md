# Report diagrams

PlantUML source files for report figures.

Render PNG files with:

```powershell
plantuml -tpng assets/diagrams/*.puml
```

Render SVG files with:

```powershell
plantuml -tsvg assets/diagrams/*.puml
```

The LaTeX report can keep using TikZ while the PlantUML CLI is unavailable.
When rendered images are available, replace the matching TikZ figure with
`\includegraphics{assets/diagrams/<name>.png}` or SVG/PDF-compatible output.
