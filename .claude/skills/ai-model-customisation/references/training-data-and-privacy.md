# Training data preparation and privacy

*v0.1.0, 2026-11-08. Privacy rows from `../../_shared/regulatory-register.md` (AU-6, AU-12, EU-1,
EU-3) and research B3; dataset mechanics adapted from wshobson/agents `dataset-curation` and
`trace-to-training-data` (MIT). This file identifies considerations for the client's legal adviser;
it is not legal advice (conventions s4). Every client-facing use carries the standard disclaimer.*

## 1. Privacy first: the questions before any data moves

| # | Question | Source / rule |
|---|---|---|
| 1 | Does the training, eval or golden data contain personal information? Sensitive information (health, biometric, criminal record, TFN)? | APPs (AU-6) |
| 2 | Was it collected for a purpose that covers training a model? If not, is a secondary use permitted (APP 6), or is consent needed? | Using existing customer data to train or fine-tune triggers APP 3 and APP 6 limits (solution pattern P9, OAIC developing-and-training guidance AU-12) |
| 3 | Has a privacy impact assessment been done? | AU-12 expects one (voluntary guidance on binding law) |
| 4 | Is any of it scraped or third-party data? | AU-12: scraped public data is not automatically fair to use; check source terms |
| 5 | Will the tuned model be placed on the EU market or used there? | Training-data provenance and copyright exposure sit with the deployer under EU GPAI rules for fine-tuned models placed on the EU market (research B3); GDPR lawful basis for training (EU-3). Route to `ai-compliance-risk` |
| 6 | Will model outputs feed decisions that significantly affect people? | APP 1.7 ADM check (AU-8, from 10 Dec 2026), run by `ai-compliance-risk` |
| 7 | Does the client have an AI or data policy restricting training on certain data classes? | Client's own policy (ground truth 1) |

Outcome options: proceed with the data as is; proceed after de-identification or redaction; proceed
with a narrower dataset; obtain consent; or do not train. Record the outcome and who decided it.

## 2. Data handling rules

- **Location.** Training data, goldens, checkpoints and logs stay inside the environment approved
  for the data class (`ai-deployment-platforms/references/data-class-matrix.md`). Hosted training
  services and notebooks (including Hugging Face Jobs, which the harvested trainer skill uses) are
  treated as offshore until their processing region is verified (`PENDING_VERIFICATION`). No
  personal information goes to an unverified service.
- **Memorisation.** A tuned model can reproduce training data. The adapter and any merged model are
  classified at the highest data class present in the training set, access-controlled and stored
  like the source data. Never pushed to a public model hub; private repositories only inside the
  approved environment.
- **Redaction.** Scan every row for secrets and PII and redact before it ships; if sensitive fields
  remain after redaction, drop the row (fail closed). Presidio with the AU recognisers is the
  default tool (`ai-rag-engineering/references/pii-redaction-presidio.md`).
- **Minimisation.** Train on the fields the task needs; strip identifiers that do not change the
  output.
- **Retention.** Datasets and checkpoints have an owner and a deletion date in the model card.
  Rejected checkpoints are deleted, not archived indefinitely, unless the client asks to keep them.
- **Credentials** for data pulls live in Doppler, read-only, scoped to the source.

## 3. Building the dataset (for engineers)

Adapted from wshobson `dataset-curation` and `trace-to-training-data`:

| Method | Row shape | Floor |
|---|---|---|
| SFT, single turn | `prompt` / `completion` (or instruction / response) | About 1,000 rows recommended floor; quality over quantity above it |
| SFT, multi-turn | `messages` list (chat format) | As above |
| DPO / ORPO | `prompt`, `chosen`, `rejected` | Per method |
| KTO | `prompt`, `completion`, `label` | Per method |
| GRPO / verifiable rewards | `prompt` plus verifier metadata | Per method; inspect the reward function against 50-100 sampled outputs before training |

Silent-failure checks before any run:

1. Apply the target model's chat template before packing, never after.
2. Train on assistant turns only (loss masked over system and user turns).
3. Use the same chat template at training, evaluation and inference: a mismatch degrades quality
   without any error.
4. If packing sequences, decode and read 5 to 10 packed sequences by hand before the full run.
5. Golden IDs excluded from training by ID; de-duplicate against existing training data, not just
   within the new batch.
6. Synthetic data: keep at least 25% real (non-generated) rows; expect filtering to reject most
   generated rows, so plan volume accordingly.

## 4. Dataset card (required before any run)

| Field | Content |
|---|---|
| Provenance | Every source (client system, date range, synthetic method, teacher model and its terms check) |
| Counts | Total rows and rows per split |
| Synthetic / real ratio | Measured, checked against the 25% real floor |
| De-duplication method | Exact, semantic, or both |
| Chat template | Exact identifier, matched at eval and inference |
| Packing | On or off, max sequence length, manual inspection done |
| Privacy (House addition) | PIA reference, APP 3/6 outcome, redaction applied and its test result, data class, storage location, retention and deletion date, owner |
| Approval (House addition) | Client data owner sign-off and date |

## 5. Model card (for the tuned model, owned with ai-governance-program)

Base model and licence (with the licence file checked on the day), method and hyperparameters,
dataset card link, eval results versus baselines with dates, known limitations and failure buckets,
intended and out-of-scope uses, data class, hosting location, owner, retraining cadence, retirement
plan. Entered in the client's AI register.
