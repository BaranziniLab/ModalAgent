---
name: modal-compute
description: "Moved: use gpu-compute-optimization instead. This skill no longer holds instructions."
---

# modal-compute has moved

This skill was bundled with ModalAgent. Its content now lives in `gpu-compute-optimization`. Install `gpu-compute-optimization` from BAAM in Biorouter and use it instead.

ModalAgent was retired on 2026-11-22 and no longer calls any service. Why: Modal ships its own command line, which the Developer extension runs with the secret guard in place, so a separate wrapper is not needed. Use instead: Use the modal command line through the Developer extension, with the gpu-compute-optimization skill.
