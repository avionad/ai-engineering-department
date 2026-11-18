# Architecture views and Mermaid conventions

*v0.1.0, 2026-11-08. DDD conventions. The four views follow the common context, container,
data-flow and sequence split used in software architecture practice; nothing harvested is
copied. Mermaid renders in Markdown, Google Docs exports and the DDD report renderer
(conventions s7).*

## 1. Mermaid conventions

| Convention | Rule |
|---|---|
| Diagram type | `flowchart LR` for context, container and data flow; `sequenceDiagram` for interactions; `flowchart TD` for decision logic |
| Node labels | Plain words a client understands; technical names on a second line. Any label with punctuation goes in double quotes, and never nest brackets inside a shape: `M["Model endpoint<br/>(Bedrock, Sydney)"]` |
| Regions | Every external service and data store is labelled with its region or "region PENDING_VERIFICATION" |
| Shapes | `[(...)]` data stores; `[...]` services and steps; `{...}` decisions; `([...])` people or external actors |
| Trust boundaries | `subgraph` per boundary with an ID and a quoted title: `subgraph CT ["Client tenancy, Australia East"]` |
| Personal data | Edges carrying personal information labelled `PI:` plus the kinds (`PI: name, phone`); sensitive information `SI:` |
| Writes | Edges that write to a system of record labelled `write` and, if approval-gated, `write (approved)` |
| Size | One idea per diagram; split when a diagram passes about 15 nodes |
| No styling | No colours or classes: they do not survive every renderer and add nothing to meaning |

## 2. Context view

Who and what surrounds the system.

```mermaid
flowchart LR
  U([Accounts staff]) --> S[Invoice capture service]
  V([Suppliers]) -->|email with PDF| S
  S -->|write approved| E[("ERP<br/>(client tenancy, region)")]
  S --> M["Model endpoint<br/>(provider, region)"]
  S --> A[Approval screen]
  U --> A
```

## 3. Container view

The deployable parts and how they communicate.

```mermaid
flowchart LR
  subgraph DV ["DDD-managed VPS, Australia"]
    W["Workflow engine<br/>(n8n)"]
    Q[(Error queue)]
    L[(Run log)]
  end
  subgraph PR ["Provider, Australian region"]
    M[Model endpoint]
  end
  subgraph CT ["Client tenancy"]
    MB[Shared mailbox]
    E[(ERP)]
  end
  MB -->|IMAP/API| W
  W -->|HTTPS| M
  W -->|API write approved| E
  W --> Q
  W --> L
```

## 4. Data flow with trust boundaries and personal-data paths

The view the compliance officer and the client's privacy officer read. Show every boundary
crossing and every place personal data rests, including logs, caches, backups and the vendor's
own retention.

```mermaid
flowchart LR
  subgraph CD ["Customer devices"]
    C([Customer])
  end
  subgraph CT ["Client tenancy, Australia"]
    F[Web form]
    CRM[(CRM)]
  end
  subgraph DM ["DDD-managed, Australia"]
    W[Workflow]
    LG[("Logs, retention per design<br/>PI redacted")]
  end
  subgraph MP ["Model provider, region PENDING_VERIFICATION"]
    M["Model API<br/>retention per contract"]
  end
  C -->|PI: name, email, enquiry| F
  F -->|PI| W
  W -->|PI: enquiry text only| M
  M -->|classification| W
  W -->|write: PI| CRM
  W -->|redacted| LG
```

Checklist for this view:
- Every edge crossing a subgraph is a boundary crossing: what protects it (TLS, private link,
  allow-listed IP, signed webhook)?
- Every store holding PI: region, retention, who can read it, encryption.
- Minimisation: does each hop receive only the fields it needs?
- Untrusted input entry points marked (they feed the threat model: LLM01:2026, ASI01).

## 5. Sequence view

For the key interaction, and always for the approval path of anything that acts.

```mermaid
sequenceDiagram
  participant W as Workflow
  participant M as Model
  participant A as Approver
  participant E as ERP
  W->>M: Extract fields (schema)
  M-->>W: Fields + confidence
  W->>W: Validation rules
  alt Passes
    W->>A: Approval request (raw document + fields)
    A-->>W: Approve
    W->>E: Create draft bill (idempotency key)
  else Fails
    W->>W: Error queue + alert
  end
```

## 6. Which views a design needs

| Risk tier / size | Views required |
|---|---|
| Tier 1, S | Context + data flow (can be one diagram) |
| Tier 2 or M | Context, data flow, sequence for the main interaction |
| Tier 3 or L/XL | All four, plus a sequence for every approval path and the kill switch |
