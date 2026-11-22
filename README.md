# ModalAgent

Retired. This extension no longer calls Modal and only reports that it is retired. Remove it.

Current version: **0.2.0**

> **Retired.** ModalAgent was retired on 2026-11-22 and no longer calls any service. Why: Modal ships its own command line, which the Developer extension runs with the secret guard in place, so a separate wrapper is not needed. Use instead: Use the modal command line through the Developer extension, with the gpu-compute-optimization skill.

This is the final release of a retired Biorouter extension. It replaces every
earlier tool with one, `modal_status`, which shows the notice above. It holds no
credentials, reads no setting and calls no service. Remove the extension in
Biorouter once you no longer need the notice.

## Tools

- `modal_status`: shows why ModalAgent was retired and what to use instead. It calls no service.

## Bundled skills

Every skill an earlier release bundled is kept, and each now says where its content
moved. An update never deletes a file an earlier version installed, so keeping the
paths is what replaces the old instructions.

## Develop and release

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python scripts/build_brxt.py
```

Do not edit `src/modalagent/_kit/` or `tests/kit_testing/`: they are vendored from the BRXT
adapter kit in the Biorouter repository (`scripts/brxt-adapter-kit/`).

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
