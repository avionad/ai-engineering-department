# Tool card: hosting a custom model on Amazon SageMaker

*Adapted 2026-11-08 from huggingface/skills `skills/hf-cloud-sagemaker-deployment-planner/SKILL.md`,
`hf-cloud-sagemaker-iam-preflight/SKILL.md` and `hf-cloud-sagemaker-production-defaults/SKILL.md`
(Apache-2.0, commit 25910b3d0ba31a2ba102f901cdc9e008c278a69c). The scripts those skills reference were
not harvested; this card carries the method only. Instance types named in the source are omitted:
check regional availability and quota in the client's account.*

## Pathway choice (from the planner)

| Pathway | Fits | Avoid when |
|---|---|---|
| Real-time endpoint | Steady traffic, interactive latency; the default for LLMs | Very sparse or spiky traffic (idle cost) |
| Real-time, scale to zero | Sparse or scheduled traffic, dev/test | Any interactive SLA: the first request after idle is slow and requests during wake-up fail |
| Serverless inference | Spiky, small models | Most LLMs exceed its memory limits |
| Async inference | Long inference or large payloads, queue-friendly | Interactive synchronous calls |
| Batch transform | Offline scoring of a dataset (eval runs, bulk classification) | Anything online |
| Bedrock Custom Model Import | Wants the Bedrock API, supported base family, weights only | Custom inference logic, unsupported architectures |

Ask only what is needed (what model, roughly how often it is called), recommend one pathway, and
confirm before creating anything that costs money.

## Preflight (from the IAM and planner skills)

1. **Region first**: an Australian region approved for the data class (`ai-deployment-platforms`).
2. **Quota**: GPU endpoint quotas are per instance type per region and often zero by default; check
   before recommending, request increases early (hours to days).
3. **Execution role**: reuse an existing valid role before creating one; validate its trust policy;
   scope permissions to the model bucket, container pulls and logs; never attach a full-access
   managed policy. SSO users often cannot create roles: ask the client's admin with the exact
   actions needed.

## Production defaults (from the source)

- Autoscaling, CloudWatch alarms and tagging on by default; an endpoint without them is a demo.
- Alarms need a notification target or nobody hears them.
- "InService is not success": smoke-test with real requests before declaring done.
- VPC configuration and KMS keys are not defaulted by the source: **our security baseline requires
  both** for confidential and personal data (`ai-deployment-platforms/references/security-baseline.md`).
- Data capture writes requests and responses to S3: off by default; if enabled, the bucket holds
  client data and must meet the same residency, encryption and access rules.
