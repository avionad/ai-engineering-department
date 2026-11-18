# Open-weight model selection: licence first

*v0.1.0, 2026-11-08. Sources: research B3 (`ai-dept-web-research-2026-11-08.md`), client FAQ Q10,
solution pattern P9. Model names, versions and dates below are a dated snapshot copied from the
research, most of it from secondary sources. **Never quote a row to a client without checking the
model card and licence file live on the day.** No benchmark figures are given here on purpose.*

## 1. The framework (in this order)

### Step 1. Licence

| Licence type | Examples per research | What it means for a client |
|---|---|---|
| Permissive (Apache-2.0, MIT) | Qwen family (Apache-2.0), DeepSeek (MIT), Gemma 4 (reported as the first Gemma under Apache-2.0, **[secondary]**, The Register per the research snapshot), gpt-oss (Apache-2.0, **[secondary]**, believed Apache-2.0 per research pending item 10) | Commercial use, modification and fine-tuning generally allowed; keep notices; still read the actual licence file on the model card |
| Custom community licence | Llama 4 Community Licence (not OSI-approved) | Per research B3: separate licence needed if the licensee's products exceeded 700m monthly active users; no rights to multimodal features for EU-domiciled individuals or companies with an EU principal place of business; "Built with Llama" attribution and a "Llama" name prefix on derivatives; acceptable use policy applies. The client's legal adviser reviews before use |
| Other custom licences | Kimi (Moonshot), GLM (Zhipu) main models; a GLM Flash variant reported MIT | Legal review required; facts `PENDING_VERIFICATION` |
| Earlier Gemma releases | Gemma before version 4 | Not Apache-2.0 per the research's "first Gemma under Apache 2.0" note (**[secondary]**, The Register); check the specific terms |

Licence questions to answer for every candidate: commercial use allowed; fine-tuned derivatives
allowed and on what terms; attribution and naming duties; user-count or revenue thresholds;
territorial limits; acceptable use policy; whether outputs may be used to train other models.

### Step 2. Client policy and origin

Government and critical-infrastructure clients may have procurement or security policy objections
to certain model origins (research B3). No Australian legal prohibition on self-hosting
Chinese-origin weights was found (`PENDING_VERIFICATION`). Ask the client; record the answer.
Commonwealth agencies and their suppliers also follow the DTA policy (register AU-17).

### Step 3. Task fit on the client's golden set

Shortlist two or three candidates, run them on the eval harness with the same prompts, compare per
failure bucket. Public leaderboards are a shortlisting aid only; they measure other tasks.

### Step 4. Size, hardware and hosting

Smallest model that clears the target, on hardware the platform decision allows. Research B4 lists
small open-weight models that suit a self-managed VPS (Gemma 4, Qwen3.6-27B, gpt-oss-20b) `[secondary]`,
noting that an **Australian** VPS is often a new procurement: verify your provider's data-centre
list live before assuming Australian hosting, as several popular VPS providers publish no
Australian location. Mixture-of-experts models have large total parameter counts but fewer active
parameters: memory still has to hold all the weights.

### Step 5. Currency check on the day

Open the model card and record: exact model ID and revision, licence file and date read, context
length, intended use and restrictions, recommended chat template. Paste the URL and date into the
decision record. If any field cannot be confirmed, write `PENDING_VERIFICATION` and keep the model
out of the client deliverable.

## 2. Research snapshot (2026-11-08, verify before use)

Copied from research B3; secondary sources marked as in the research.

| Family | Items reported by the research | Licence | Source status |
|---|---|---|---|
| Qwen (Alibaba) | Qwen3.5 (Feb 2026, MoE flagship; small 0.8B to 9B, Mar 2026); Qwen3.6-35B-A3B and Qwen3.6-27B dense (Apr 2026) | Apache-2.0 | **[secondary]** |
| DeepSeek | V4 preview (Apr 2026, Pro and Flash variants, 1M context); V4 Pro out of preview Aug 2026 | MIT | **[secondary]** |
| Gemma (Google) | Gemma 4 (Apr 2026): E2B, E4B, 26B MoE, 31B dense | Apache-2.0 | **[secondary]**, The Register (trade press, not the model card or licence file); `PENDING_VERIFICATION` |
| Llama (Meta) | Llama 4 Scout and Maverick (Apr 2025); a newer release reported Oct 2026 | Llama 4 Community Licence | Hugging Face model card for Llama 4, read by the research file and not re-read since (**[secondary]** as recorded here, primary if the card is opened on the day); newer release `PENDING_VERIFICATION` |
| gpt-oss (OpenAI) | gpt-oss-120b, gpt-oss-20b | Apache-2.0 (believed) | **[secondary]**, `PENDING_VERIFICATION` |
| Kimi (Moonshot), GLM (Zhipu) | Reported as top open-weight models on a public leaderboard, Oct 2026 | Custom licences | **[secondary]**, all `PENDING_VERIFICATION` |

The harvested wshobson model catalogue (last verified 2026-07-14) names size-class picks for
fine-tuning on specific hardware; it is older than the research snapshot and hardware-specific, so
use it only for its method (size class first, family second, dated catalogue with a refresh
checklist), not for its picks.

## 3. Refresh rule

This snapshot goes stale within a quarter. Refresh it when a client decision depends on it: check
each family's official model cards and licence files, update the table with URLs and dates, and
remove anything that cannot be confirmed. Log the refresh in the changelog of this skill.
