# GH-300 objective coverage map

**Official exam-objective date:** August 7, 2026. **Sources checked:** November 22, 2026.

Use this map to find evidence of mastery, not just pages you have read.
The [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)
is authoritative; related topics can also appear.
Objective descriptions below are original paraphrases.

!!! note "Count the substantive domains, not a duplicated label"
    The official skills-at-a-glance list repeats the features label. Its detailed objectives describe six domains. Do not allocate a second 25-30% block to that repeated line.

## Coverage and practical evidence

| Domain and official weight | Skill to demonstrate | Study material | Practice evidence |
| --- | --- | --- | --- |
| Responsible use: 15-20% | Recognize uncertainty, bias, overreliance, and potential harms | [Responsible AI](responsible-ai.md) | Explain M01-M07 without opening the answers |
| Responsible use | Choose mitigations and human accountability proportionate to risk | [Validation workflow](responsible-ai.md#validation-workflow) | [Lab 1](hands-on-labs.md#lab-1-context-and-responsible-output) and [Lab 3](hands-on-labs.md#lab-3-tests-that-detect-a-regression) |
| Features: 25-30% | Set up an IDE; select completion, chat, or agent work | [Features](copilot-features.md) | Select a surface and justify tool permissions in M08-M10 |
| Features | Install/authenticate CLI; interactive sessions versus programmatic tasks | [CLI and administration](copilot-features.md#cli-and-administration) | [Lab 4](hands-on-labs.md#lab-4-cli-and-agent-control) |
| Features | Generate/review scripts and file changes in CLI | [Features](copilot-features.md) | Show scoped tools, a reviewed diff, and a test result |
| Features | Distinguish edits/agents, sessions, delegation, and MCP | [Part 2](learning-path-part-2.md) | [Lab 5](hands-on-labs.md#lab-5-mcp-and-delegated-work) |
| Features | Distinguish Spaces, historical Spark, PR summaries, code review, and instructions | [Capability distinctions](copilot-features.md#distinctions-worth-practicing) | Explain M11-M15 and M18, including Spark's retirement |
| Features | Govern feature access and code-review policy across surfaces | [Features](copilot-features.md) | Explain the policy/instruction distinction in M16 |
| Features | Investigate audit activity and manage seats via REST | [Features](copilot-features.md) | Map an actor/action/scope; explain M17 |
| Data/architecture: 10-15% | Describe prompt inputs, context selection, flow, and processing | [Data and architecture](data-architecture.md) | Draw the lifecycle from memory; M19-M21 |
| Data/architecture | Explain probabilistic output, finite context, and lifecycle failures | [Lifecycle](data-architecture.md#suggestion-lifecycle) | Diagnose M22-M24 without assuming universal retention |
| Prompting/context: 10-15% | Specify task, context, constraints, and examples | [Prompt engineering](prompt-engineering.md) | [Lab 2](hands-on-labs.md#lab-2-zero-shot-few-shot-and-reusable-prompts); M25-M27 |
| Prompting/context | Refine from evidence and manage chat-history relevance | [Diagnose a weak response](prompt-engineering.md#diagnose-a-weak-response) | Explain M28-M30 and compare two saved prompt attempts |
| Productivity: 10-15% | Generate/refactor/document/modernize without changing intended behavior | [Productivity](productivity.md) | Baseline tests plus one scoped improvement; M31-M32 |
| Productivity | Use synthetic data; test edge cases/assertions and integration boundaries | [Testing workflow](productivity.md#testing-workflow) | [Lab 3](hands-on-labs.md#lab-3-tests-that-detect-a-regression); M33-M34 |
| Productivity | Verify security/performance suggestions and measure real impact | [Productivity](productivity.md) | Explain M35; propose a baseline and an outcome metric |
| Privacy/safeguards: 10-15% | Apply exclusion/editor/privacy settings at the correct scope | [Privacy](privacy-safeguards.md) | [Lab 6](hands-on-labs.md#lab-6-privacy-and-policy-troubleshooting); M36-M37 |
| Privacy/safeguards | Evaluate public-code references, ownership, and safeguard limits | [Ownership and public code](privacy-safeguards.md#ownership-and-public-code) | M38-M39; explain why a missing license is not permission |
| Privacy/safeguards | Diagnose exclusion/suggestion problems without bypassing protections | [Troubleshooting](privacy-safeguards.md#troubleshooting-checklist) | M40 and a sanitized troubleshooting record |

Question identifiers refer to the [40-question mock exam](mock-exam.md).
The existing [48 practice questions](practice-questions.md) remain useful for
initial review and the Microsoft Learn paths.

## What to refresh immediately before the exam

| Stable reasoning | Product detail to verify, not memorize blindly |
| --- | --- |
| Humans retain responsibility for accepted changes | Client modes, feature names, and preview status |
| Instructions are not authorization boundaries | Plan entitlements, organization policies, and billing |
| Meaningful tests can disprove a wrong implementation | Current CLI flags and installation prerequisites |
| Exclusions complement access control | Supported surfaces, indirect-access limitations, and propagation |
| Model output needs grounding and validation | Data terms for the exact plan, model, feature, and environment |

The newer cloud experience and exclusion support differ from some older training
screenshots. Read scenario qualifiers carefully and consult current
[content-exclusion documentation](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion).
Do not invent exam questions or try to obtain recalled exam content to resolve
differences between product versions.
