# Grok model routing

Checked: 2026-09-27. Load only when selecting a Grok worker. The official catalog currently recommends `grok-4.7` for general text and coding; this reference does not preserve older alternatives or invent a cheaper successor. Confirm that the active host exposes this ID before selecting it. [Official model catalog](https://docs.x.ai/developers/models).

Use the same current model with task-appropriate effort:

| Task | Suggested starting effort |
| --- | --- |
| Clear extraction, simple tool use, mechanical changes | `low` |
| Scoped analysis, routine implementation, long-context synthesis | `medium` |
| Difficult debugging, consequential review, multi-step reasoning | `high` |
| Hard unresolved reasoning where latency is secondary | `xhigh` |

These task mappings are recommendations, not measured rankings. Grok 4.7 supports all four levels; its provider default is `high`, and reasoning cannot be disabled. The documented chat interface uses `reasoning_effort`; Responses uses `reasoning.effort`. A harness may expose different controls or only a subset: use its actual tool schema. [Official reasoning controls](https://docs.x.ai/developers/model-capabilities/text/reasoning).

Current-information tasks still require appropriate search tools; selecting Grok does not itself provide live facts. Provider-side multi-agent inference is not evidence that the local harness exposes independently assignable workers. Confirm native delegation separately, preserve explicit user choices, and report the effective model if observable. Refresh the catalog before relying on this dated guidance after a model change.
