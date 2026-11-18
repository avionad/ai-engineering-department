# Observability stack: traces, evals, cost

*v0.1.0, 2026-11-08. Source: GitHub research area 7 (repo, licence, last push as at
2026-11-08). None of these tools was harvested; features are `PENDING_VERIFICATION` against their
live docs at deployment. Hosting follows the engagement's residency requirement (Australian region
or client infrastructure) and the data-handling agreement.*

## Default choice

| Tool | Licence (per research) | The practice use | Notes |
|---|---|---|---|
| **Langfuse** | Mixed: MIT core, `ee/` directories proprietary | **Default self-hosted tracing**, prompt management, eval scores, cost | Use the MIT core only; do not enable or harvest `ee/` features without a licence decision |
| **Opik** | Apache-2.0 | Permissive alternative with evals | Choose when the client or the practice wants no mixed-licence components |
| **Arize Phoenix** | **Elastic Licence 2.0, verified** 2026-11-08 from the repo LICENSE file, https://github.com/Arize-ai/phoenix/blob/main/LICENSE. The harvested Orchestra-Research how-to says "Apache 2.0"; the LICENSE file is the source of truth, so that how-to is wrong | **Client self-hosts only** | ELv2's limitation clause reads: "You may not provide the software to third parties as a hosted or managed service, where the service provides users with access to any substantial set of the features or functionality of the software." the practice's conservative reading is that hosting Phoenix for a client as part of a retainer would fall inside that clause, so **The practice does not host or resell Phoenix as a service**. A client self-hosting it for their own use is a normal permitted use. This is the practice's reading of the licence, not legal advice: if a client wants the practice to host it, their legal adviser decides first |
| **Platform-native logs** | n/a | Bedrock, Azure, Vertex logging and billing exports; n8n execution logs | Often enough for S band; usage export feeds `cost_trend.py` |
| OpenLLMetry / OpenLIT | Apache-2.0 | OpenTelemetry instrumentation feeding any backend | Vendor-neutral option for L and XL clients with an existing OTel stack |
| Helicone | Apache-2.0 | Proxy-style observability and cost | A proxy is a data flow: vendor due diligence applies |
| MLflow | Apache-2.0 | Tracing and evals in Databricks shops | Use what the client already runs |

Optimisation libraries (research area 7): DSPy (MIT) and GEPA (MIT, reflective prompt
optimisation, integrates with DSPy). TextGrad (MIT) is quiet since mid 2025: not a default.

## Minimum fields per trace (the practice standard)

Timestamp, system, workflow step, model ID and version, prompt version, input tokens, cached
input tokens, output tokens, cost (as reported by the platform), latency per stage, retrieval
document IDs and scores, tool calls with arguments and results, outcome (completed, escalated,
overridden, failed), reviewer and decision where a human approves, user role (not identity unless
the design requires it), masked input and output.

## Data handling

- Traces hold personal information unless masked: mask at source (Presidio AU recognisers) and
  set retention with the client (sign-off checklist item 10).
- The trace store sits in the agreed region; access is role-based and reviewed.
- the practice reads exports or read-only views; it does not need write access to production.
