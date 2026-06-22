# Contributing

Thanks for helping grow pentagi-knowledge!

## Adding a new framework / source

1. Create a top-level folder named after the source (e.g. `owasp/`, `atlas/`).
   For MITRE frameworks, nest under `mitre/<framework>/<domain>/`.
2. Inside each domain folder, ship:
   - the knowledge documents (one Markdown file per item),
   - an `INDEX.md` mapping every item,
   - a `manifest.json` (source, version, counts, generated_at, generator).
3. Keep the document format consistent: YAML frontmatter (`id/name/type/tags/url`) +
   structured body so semantic search stays precise.
4. Add a generator under `tools/` when the source has machine-readable data; prefer
   official structured data over scraping.

## Knowledge document conventions

- One file per atomic item (tactic, technique, sub-technique, rule, …).
- Filename: `<ID>__<slug>.md`.
- Always include a `Source:` link to the authoritative page.
- Paraphrase where possible; attribute verbatim third-party text in `NOTICE`.

## Legal

Only contribute content you have the right to redistribute, with proper attribution.
This project is for defensive understanding and authorised testing only.
