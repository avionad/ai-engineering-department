# Model customisation go / no-go: {project}

*Template v0.1.0 (ai-model-customisation), 2026-11-08. Save as
`{client}/created/docs/strategy/customisation-go-no-go-{project}-{YYYY-MM-DD}.md`. A "no-go" is a
normal, good outcome: it saves the client the cost of training they do not need. Model names,
versions and licences carry a model-card URL and date read, or `PENDING_VERIFICATION`.*

## 1. Summary (60 seconds, for the owner)

- Decision: GO (fine-tune / distil) | NO-GO (stay with prompting / RAG) | NOT YET (gate not met)
- Why, in one paragraph in plain English:
- What it costs to run and maintain (drivers, not prices):
- What happens next:

## 2. Context

| Item | Value |
|---|---|
| Use case and process | |
| Risk tier (`ai-compliance-risk`) and date | |
| Size band, industry pack | |
| Failure in one sentence (facts / behaviour / format / verifiable skill / cost-latency) | |
| Volume (requests per day or month, client's figures) | |
| Target agreed with client owner (metric, threshold, who, date) | |

## 3. Off-ramps checked

| Off-ramp | Tried? | Result | Evidence |
|---|---|---|---|
| Better prompt on a capable hosted model in the approved region | | | baseline file |
| Retrieval / tools (`ai-rag-engineering`) | | | baseline file |
| Cost levers (caching, batch, smaller hosted model, routing) | | | |

## 4. Eval-first gate (all must be true for GO)

- [ ] At least 100 traces open-coded; failure buckets: ____
- [ ] Goldens versioned and signed off by ____
- [ ] One grader per bucket, deterministic first; judge calibrated or N/A
- [ ] Drift suite frozen (harness and version): ____
- [ ] Baselines: hosted+prompt ____ ; hosted+RAG ____ ; untuned base model ____
- [ ] Baselines miss the agreed target by: ____

## 5. Proposed approach (GO only)

| Item | Value |
|---|---|
| Method and the data shape that drove it | |
| Base model, revision, model-card URL, date read | |
| Licence, licence file read on (date), obligations, legal review needed? | |
| Client origin policy checked (yes/no, who) | |
| Size class and memory feasibility basis | |
| Training environment and region (from platform decision record) | |
| Hosting option and serving stack | |
| Export format; merged or adapter-only; base revision pinned | |

## 6. Data and privacy

- [ ] Data classes in the training set: ____
- [ ] PIA reference: ____ ; APP 3 / APP 6 outcome: ____
- [ ] Consent or permitted secondary use basis recorded (for the legal adviser)
- [ ] Redaction applied and tested (recall on sample): ____
- [ ] Golden IDs excluded; de-duplication done
- [ ] Dataset card complete (all fields incl. DDD privacy and approval fields)
- [ ] Teacher-model output-use terms checked (distillation only): ____
- [ ] Storage of weights: location, encryption, access, retention date

## 7. Promotion criteria (agreed before training)

- Golden target per bucket: ____
- Drift budget: <= 1 pt noise; 2-5 pt rerun with seeds; > 5 pt hard fail
- Paired comparison vs base and vs hosted+prompt: must win
- Canary share and rollback trigger: ____
- Client owner approves the comparison report before go-live

## 8. Operations

- Monitoring signals and owner:
- Retraining triggers:
- Rollback checkpoint retained until:
- Exit / fallback to hosted+prompt documented: yes / no

## 9. Effort drivers (to ai-proposal-pricing, bucket slugs only)

| Driver | Bucket | Notes |
|---|---|---|
| | `governance-compliance` | eval harness, PIA input, model card |
| | `model-customisation` | data prep, licence review, training, export, hosting |
| | `run-ongoing` | monitoring, retraining |

## 10. Sign-off

| Role | Name | Date | Decision |
|---|---|---|---|
| DDD (ai-architect / owner) | | | |
| ai-compliance-officer review | | | |
| Client accountable owner | | | |
