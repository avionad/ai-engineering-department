# Vendored provenance: ai-deployment-platforms

*v0.1.0, 2026-11-08. Harvested files this skill read or adapted, with repo, licence and pinned commit
(SHAs from `ai-kb/vendor/_harvest-manifest-2026-11-08.json`). Department-wide list:
`../../_shared/VENDORED.md`. This skill is mostly built from the research files and DDD's own method;
harvested material supplied specific platform patterns.*

| Used in (this skill) | Harvested file (upstream, under `ai-kb/vendor/`) | Repo | Licence | Commit SHA | How used |
|---|---|---|---|---|---|
| `references/security-baseline.md` B1, B4, B6; `references/platforms.md` s2 | `ai-kb/vendor/Azure-Samples__azure-search-openai-demo/docs/productionizing.md`, `.../docs/login_and_acl.md`, `.../docs/evaluation.md` | Azure-Samples/azure-search-openai-demo | MIT | 558ffd397eddcfe4da5c85ebc285796b367eb9b2 | Network isolation, authentication, API Management in front, on-behalf-of identity, logging query for throttling. Paraphrased; Microsoft Learn URLs from these docs listed in `verify-live.md` |
| `references/security-baseline.md` B1, B4, B5, B6; `references/platforms.md` s1 | `ai-kb/vendor/huggingface__skills/skills/hf-cloud-sagemaker-iam-preflight/SKILL.md`, `.../hf-cloud-sagemaker-production-defaults/SKILL.md`, `.../hf-cloud-sagemaker-deployment-planner/SKILL.md` | huggingface/skills | Apache-2.0 | 25910b3d0ba31a2ba102f901cdc9e008c278a69c | Least-privilege execution role, quota preflight, alarms and autoscaling defaults, Bedrock Custom Model Import fit, and the gap that VPC and KMS are not defaulted (we require them). Summarised and modified; licence at `ai-kb/vendor/huggingface__skills/LICENSE` |
| `references/security-baseline.md` s3 | `ai-kb/vendor/Orchestra-Research__AI-Research-SKILLs/12-inference-serving/vllm/SKILL.md`, `.../llama-cpp/SKILL.md` | Orchestra-Research/AI-Research-SKILLs | MIT | 773a52944ba4747a18bd4ae9ade53fff041adcbc | Observation that examples bind to all interfaces and use `trust-remote-code`; our hardening rules respond to it |

## Non-harvested sources

| Source | Used for |
|---|---|
| Research `ai-dept-web-research-2026-11-08.md` B2, B4, B5, B6 | All platform residency and assurance facts, sovereignty caveat, hybrid recommendation, cost levers, agent controls, every URL in `verify-live.md` except the Microsoft Learn links from the harvested sample |
| Research `ai-dept-github-research-2026-11-08.md` area 4, 5, gap 7 | Reference repos with licences and archive status (AVM landing zone module, Foundry baseline, AI hub gateway, AWS samples, LiteLLM, archived repos) |
| `../../_shared/regulatory-register.md` AU-6, AU-11, AU-13, AU-15, AU-17, AU-19, AU-23 | Obligations cited with their recorded status |
| `../../_shared/client-faq.md` Q1-Q3, Q12, Q17 | Client-ready wording referenced |
