# Weighted GH-300 mock exam

!!! important "Original practice, not real exam content"
    These 40 questions were written for this guide. They are not Microsoft/GitHub questions, exam dumps, or a prediction of your score. The six-domain distribution fits the published exam weight ranges, but neither difficulty nor scoring is calibrated to the actual exam.

Answer without notes or opening rationales. Record your confidence and flag
guesses. A suggested **practice** limit is 60 minutes, not the actual exam's
time allowance. Read the current [official exam information](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/).

## Scorecard

| Domain | Questions | Count | Practice allocation | My correct answers |
| --- | --- | ---: | ---: | --- |
| Responsible use | M01-M07 | 7 | 17.5% | ___ / 7 |
| Features | M08-M18 | 11 | 27.5% | ___ / 11 |
| Data/architecture | M19-M24 | 6 | 15% | ___ / 6 |
| Prompt/context | M25-M30 | 6 | 15% | ___ / 6 |
| Productivity | M31-M35 | 5 | 12.5% | ___ / 5 |
| Privacy/safeguards | M36-M40 | 5 | 12.5% | ___ / 5 |
| Total | M01-M40 | 40 | 100% | ___ / 40 |

Unless stated otherwise, select **one** answer. For **Select two** questions,
award one practice point only when both correct options and no extra options
are selected. No partial credit in this guide; actual exam scoring may differ.
Your simple percentage is not the exam's scaled score or a pass guarantee.

## Responsible use

### M01. Tests agree with an invented API

Copilot generates an integration and mocks the same method in every test.
The suite passes, but the method is missing from the installed dependency.
What is the strongest next action?

- A. Increase coverage using more mocks of the same method.
- B. Verify the real dependency contract and test the actual integration boundary.
- C. Accept the integration because the suite is internally consistent.
- D. Change the dependency version until a similarly named method is found.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Passing mocks can reproduce an invented contract; authoritative
API checks and a real boundary test can disprove it.
A expands the same false premise. C mistakes test consistency for correctness.
D changes compatibility without establishing the required behavior.
Review [validation](responsible-ai.md#validation-workflow).
</details>

### M02. Unequal input handling

A generated form accepts identifiers written in one alphabet but rejects
valid identifiers in other supported scripts. Which response best addresses
the responsible-AI concern?

- A. Document the restriction without checking the agreed requirements.
- B. Add a disclaimer that AI generated the validation.
- C. Disable input validation for every field.
- D. Review inclusiveness/fairness, define valid inputs, and test representative supported cases.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Review impact against requirements and test the intended supported
inputs. A leaves the unexplained exclusion in place. B does not repair impact.
C removes unrelated safeguards rather than fixing the validation.
Review [responsible principles](responsible-ai.md#responsible-ai-principles).
</details>

### M03. Ownership of a production change

A team accepts an agent-generated patch after its normal review. A defect
later affects customers. Which accountability statement is correct?

- A. The approving and operating team remains responsible for the change.
- B. Responsibility moves entirely to the AI service because it authored the patch.
- C. The reviewer is responsible only for manually written lines.
- D. Passing CI transfers responsibility to the test framework.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** AI assistance does not transfer engineering accountability.
B and C carve out an unsupported exception for generated code.
D confuses a validation mechanism with an accountable decision-maker.
Review [responsible use](responsible-ai.md).
</details>

### M04. Accidental sensitive context

A developer realizes a troubleshooting prompt contained an actual credential.
What should they do first?

- A. Add an exclusion later and assume the earlier exposure is reversed.
- B. Ask Copilot to forget it and continue using the credential.
- C. Stop sharing it, follow the incident process, and revoke/rotate the exposed credential.
- D. Put the credential in an environment variable but leave it active.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Handle actual exposure through the approved security process.
A does not retroactively undo exposure. B is not revocation or verified deletion.
D changes local placement without addressing the already exposed secret.
Review [privacy safeguards](privacy-safeguards.md).
</details>

### M05. A green filter

Generated code has no public-code match and no scanner findings. Which
conclusion is justified?

- A. Those checks provide limited evidence; correctness, license suitability, and review still need evaluation.
- B. No match proves the output is original and license-free.
- C. No scanner finding proves there are no authorization bugs.
- D. The checks make domain-owner approval unnecessary.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** Each check has a scope and limitations.
B turns absence of a detected match into a legal conclusion.
C treats known-pattern detection as exhaustive proof.
D removes accountability unrelated to either check.
Review [validation limits](responsible-ai.md#what-automated-checks-can-and-cannot-prove).
</details>

### M06. Tool output tries to expand permission

An external tool response contains instructions to send project files to an
unapproved destination. Which two responses are appropriate? **Select two.**

- A. Treat the response as authorization because the server is connected.
- B. Treat it as untrusted data and refuse the out-of-scope disclosure.
- C. Approve the disclosure if it reduces the number of tool calls.
- D. Check task scope and approved permissions before any additional action.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B, D.** Data returned by a tool does not grant new authority.
A confuses connectivity with authorization. C makes efficiency override
privacy and scope. Validate tool access and retain accountable oversight.
Review [MCP lab](hands-on-labs.md#lab-5-mcp-and-delegated-work).
</details>

### M07. Review effort versus impact

A generated comment and a generated payment-rule change are both short.
How should the team allocate oversight?

- A. Use equal review effort because line counts are equal.
- B. Use impact and reversibility to justify stronger validation for the payment rule.
- C. Review only the comment because code is already executable.
- D. Let the selected model determine which change requires approval.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Risk is not proportional to line count.
A ignores business impact. C mistakes executability for correctness.
D delegates governance to the assistant instead of the accountable team.
Review [risk-based oversight](responsible-ai.md#match-oversight-to-risk).
</details>

## Features

### M08. Coordinated local work

The goal is defined: change three local files, run the existing tests, and
iterate on failures while the developer supervises. Which starting surface
fits best?

- A. Inline completion alone, with no tool execution.
- B. A PR summary that describes changes not yet made.
- C. IDE Agent mode with appropriate tool approvals.
- D. A Space containing only general onboarding documents.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Agent mode fits supervised multi-step local edits and tests.
A is narrower than the task. B summarizes rather than implements.
D can provide context but is not the requested execution workflow.
Review [feature selection](copilot-features.md).
</details>

### M09. Requirements are not ready

A team wants Copilot to inspect dependencies and propose a migration sequence
before any edits. Which choice best reflects that intent?

- A. A planning workflow with read-only investigation and review before implementation.
- B. Agent execution with permission to rewrite all dependencies immediately.
- C. Accept the first inline migration suggestion as the complete plan.
- D. Delegate an issue without specifying compatibility or acceptance criteria.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** Planning separates investigation from approved implementation.
B exceeds the no-edit stage. C does not analyze the full migration.
D leaves the critical contract unspecified.
Review [modes](copilot-features.md#ask-plan-and-agent-modes).
</details>

### M10. Standalone CLI task

Using the current standalone Copilot CLI, a developer needs one programmatic
prompt that completes and exits. Which invocation pattern is appropriate?

- A. Run `copilot` and assume it always exits after the first answer.
- B. Put a task into a repository instruction and assume that starts a CLI session.
- C. Use an IDE slash command directly as a shell executable.
- D. Use `copilot -p "PROMPT"` with only the required approved tool permissions.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** `-p` selects programmatic usage; permissions remain a separate
decision. A selects interactive usage. B supplies context, not invocation.
C confuses client-specific chat commands with shell commands.
Source: [Copilot CLI](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli).
</details>

### M11. Repeatable task versus persistent convention

A team wants developers to invoke a reusable "review boundary cases" task
when needed, without applying its full task text to every chat. What best fits?

- A. An organization policy that enables a feature.
- B. A supported prompt file invoked for that task.
- C. A public-code matching filter.
- D. An audit event describing a past policy change.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** A prompt file packages a reusable task.
A governs availability. C filters certain matches. D records activity.
None of those substitutes for the requested reusable prompt.
Review [customization distinctions](copilot-features.md#distinctions-worth-practicing).
</details>

### M12. MCP access design

An approved MCP server will provide one reference lookup. Which two design
choices support least privilege? **Select two.**

- A. Inspect the tool/schema and provide only the access required for the lookup.
- B. Give every server a write-capable token for future convenience.
- C. Treat returned content as data requiring validation, not new authority.
- D. Assume MCP itself guarantees all responses are correct and safe.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A, C.** MCP enables integration; it does not eliminate authorization
or output validation. B expands permissions unnecessarily.
D treats a protocol as a correctness and safety guarantee.
Review [MCP in Part 2](learning-path-part-2.md#3-introduction-to-mcp-server).
</details>

### M13. A stale Space

A shared Space answers deployment questions using an obsolete runbook.
What is the best corrective action?

- A. Increase the answer length without changing the sources.
- B. Grant broader repository access to every Space user.
- C. Declare the latest conversation more authoritative than the runbook without review.
- D. Update/remove the obsolete source and retest representative questions.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Curated context must remain accurate and relevant.
A does not change grounding. B expands access without repairing the source.
C changes authority by assertion instead of maintaining the shared context.
Review [Spaces](learning-path-part-1.md#4-introduction-to-copilot-spaces).
</details>

### M14. A historical application-building objective

The published exam objectives still name Spark, but the learner is checking
product availability in November 2026. Which statement is accurate?

- A. Spark provided natural-language app building, but its new-app experience was retired; use currently supported Copilot environments for practice.
- B. Public-code matching policy, which implements full-stack applications.
- C. A PR summary, which creates and secures an application automatically.
- D. Audit logs, which generate the interface and service code.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** Distinguish historical purpose, objective wording, and current
availability. B is a safeguard, C is a description, and D is evidence of
activity rather than an application builder. Current practice should not
depend on creating a new Spark app.
Source: [official Spark retirement notice](https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com/).
</details>

### M15. Summary versus review

A PR summary accurately describes a patch. A required human approval is still
missing. What should the team conclude?

- A. The summary satisfies branch approval requirements automatically.
- B. The description aids understanding but does not replace required review and approval.
- C. A summary proves all changed paths were tested.
- D. A generated summary permits bypassing branch rules for generated code.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Summaries explain; branch/review controls govern approval.
A and D invent an exemption. C infers execution evidence from prose.
Review [review workflow](learning-path-part-2.md#4-level-up-code-reviews-and-pull-requests).
</details>

### M16. Feature unavailable under policy

A user has an assigned seat, but the organization disables a Copilot feature.
Which action can legitimately change availability?

- A. Add a prompt saying the organization has enabled the feature.
- B. Use a repository instruction to override the administrative setting.
- C. Start a new chat and assume the restriction disappears.
- D. Have an authorized administrator review the effective feature policy.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Authorization and effective policy control availability.
A and B are model instructions, not policy changes. C is not a governance
operation. Verify user, scope, plan, and surface before escalating.
Review [administration](copilot-features.md#cli-and-administration).
</details>

### M17. Seat management and change investigation

An administrator needs to automate seat assignment and separately investigate
who changed a Copilot setting. Which two resources best match those needs?
**Select two.**

- A. PR summaries as the sole source of policy-change attribution.
- B. The Copilot REST administration endpoints for supported seat operations.
- C. Applicable organization/enterprise audit log events for actor/action/scope.
- D. A repository prompt file as the seat-assignment API.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B, C.** Management operations and audit evidence solve different
problems. A describes source changes, not authoritative administrative events.
D is reusable prompt context, not an administration endpoint.
Review [administrative controls](copilot-features.md#cli-and-administration)
and [Copilot REST](https://docs.github.com/en/rest/copilot).
</details>

### M18. Delegation with useful context

A parent agent has a large task and a self-contained documentation lookup.
When is a subagent most appropriate?

- A. When every trivial lookup should be delegated regardless of overhead.
- B. When it needs unrestricted permissions unavailable to the parent.
- C. When a bounded independent task benefits from separate context and a clear result.
- D. When the parent should skip checking how the result affects the task.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Separate context helps bounded specialized work.
A wastes overhead. B does not create authority. D abandons integration and
accountability. Delegation is a workflow choice, not an approval bypass.
Review [agents and customization](copilot-features.md#ide-context-and-customization).
</details>

## Data and architecture

### M19. Wrong framework in the response

Copilot proposes a framework absent from the project. The response lacks
references to the actual dependency manifest. What should you investigate first?

- A. Whether the manifest needs to be replaced to match the suggestion.
- B. Whether relevant authoritative project context reached the prompt.
- C. Whether all output can be made correct by using a larger model alone.
- D. Whether public-code filtering guarantees framework selection.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Check grounding before altering the project.
A lets an unsupported premise redefine requirements. C overlooks missing
context. D attributes task understanding to an unrelated safeguard.
Review [prompt inputs](data-architecture.md#prompt-inputs).
</details>

### M20. "Everything is always sent"

A colleague claims every Copilot interaction uploads every accessible
repository file unchanged. Which description is more accurate?

- A. Only the prompt text can ever influence a response.
- B. The exact same file set is included across every client and mode.
- C. Context is selected and assembled within limits, according to feature, permissions, and policy.
- D. Open files always outrank explicit user context in every client.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Context sources and construction vary.
A ignores code/history/tools. B and D invent universal rules.
Do not confuse potential context sources with proof of a particular request's
contents. Review [context assembly](data-architecture.md#context-is-assembled-not-copied-blindly).
</details>

### M21. Retention generalization

A team reads a retention statement for one cloud environment and applies it
to every Copilot client, plan, and mode. What is the best correction?

- A. Retention is independent of feature or contract.
- B. Closing a chat proves all service-side data has been deleted.
- C. A repository exclusion sets the retention period for all conversations.
- D. Check the current terms for the exact plan, feature, model, and execution environment.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Data handling is context-specific and changes over time.
A ignores documented differences. B is an unsupported deletion inference.
C confuses context selection with service retention.
Review [data and architecture](data-architecture.md)
and [current GitHub cloud environments](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github).
</details>

### M22. Nondeterministic suggestions

The same task produces different suggestions across two sessions with
different histories. What is the most defensible explanation?

- A. Probabilistic generation and different effective context can change the result.
- B. One result must have bypassed all content policies.
- C. Repeating a prompt guarantees byte-identical output on every model.
- D. Different wording proves one session trained a new model on the repository.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** Model/context variation can change output without establishing
policy violations or new training. B and D infer events without evidence.
C incorrectly treats generation as universally deterministic.
Review [suggestion lifecycle](data-architecture.md#suggestion-lifecycle).
</details>

### M23. Lifecycle diagnosis

A suggestion uses the wrong interface and includes a public-code reference.
Which two checks address different lifecycle stages? **Select two.**

- A. Check supplied context/current interface definitions to diagnose grounding.
- B. Assume the reference proves the interface is valid for this project.
- C. Remove all context so post-processing cannot affect output.
- D. Inspect matching source/license and applicable safeguards before accepting it.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A, D.** Context/API grounding and matching-code suitability are distinct
checks. B converts similarity into correctness. C removes useful evidence
and does not establish safe processing.
Review [lifecycle](data-architecture.md#suggestion-lifecycle)
and [public-code ownership](privacy-safeguards.md#ownership-and-public-code).
</details>

### M24. Finite conversation context

A long conversation begins missing an earlier compatibility constraint.
What response best restores useful context?

- A. Assume earlier history is permanent and keep adding unrelated examples.
- B. Restate the critical constraint, attach authoritative files, and use a focused thread if needed.
- C. Rely on model selection alone to recover any omitted information.
- D. Remove the acceptance criteria so the model has fewer constraints.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Explicit current grounding helps when history becomes diluted.
A assumes guaranteed retention of every relevant turn. C ignores selection
limits. D removes the very contract the response should satisfy.
Review [context assembly](data-architecture.md#context-is-assembled-not-copied-blindly).
</details>

## Prompt engineering and context

### M25. A measurable prompt

You want a behavior-preserving refactor of one function with no new package.
Which prompt best states a verifiable contract?

- A. Name the function/tests, preserve public outputs/errors, forbid new dependencies, and require focused tests.
- B. Ask for "cleaner code" and let Copilot choose whether callers should change.
- C. Specify only a preferred coding style and assume behavior will be preserved.
- D. Request a complete rewrite without attaching the current contract.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** It supplies scope, authoritative context, constraints, and
observable acceptance checks. B leaves behavior open. C covers presentation
but not compatibility. D discards the evidence needed to preserve behavior.
Review [prompt pattern](prompt-engineering.md#practical-prompt-pattern).
</details>

### M26. Examples clarify a format

An output format has several nuanced cases that are hard to describe in prose.
Which approach most directly clarifies the desired pattern?

- A. Ask the same vague question repeatedly without inspecting results.
- B. Include unrelated repository files to fill the context window.
- C. Remove all examples so the model cannot be biased toward a format.
- D. Provide a small set of representative input/output examples plus constraints.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Few-shot examples can make the pattern concrete.
A is repetition without refinement. B adds noise. C rejects useful task
evidence. Examples still need review and should not contain sensitive data.
Review [prompting approaches](prompt-engineering.md#prompting-approaches).
</details>

### M27. A stale conversational premise

A chat previously discussed a different framework. Copilot keeps using that
framework for a new task. What is the best next action?

- A. Rewrite the current application to fit the stale answer.
- B. Correct the premise explicitly and start a focused conversation with the current files if needed.
- C. Add more unrelated history to make the conversation longer.
- D. Remove the dependency manifest from context.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Repair the context rather than the application.
A makes the assistant's mistake authoritative. C adds noise.
D removes evidence that could resolve the wrong assumption.
Review [weak-response diagnosis](prompt-engineering.md#diagnose-a-weak-response).
</details>

### M28. Better test-generation context

Which two additions most improve a prompt asking for tests of a shipping rule?
**Select two.**

- A. Only the name of the test file, without behavior requirements.
- B. Boundary input/output examples from the independently specified business rule.
- C. A direction to make tests pass by changing any expected value.
- D. The existing framework and a constraint not to change production behavior.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B, D.** Independent behavior examples and repository constraints
support useful tests. A lacks a contract. C rewards green tests even when
the assertions or implementation are wrong.
Review [testing prompt](productivity.md#a-stronger-test-prompt)
and [Lab 3](hands-on-labs.md#lab-3-tests-that-detect-a-regression).
</details>

### M29. Role without demonstrations

A prompt asks Copilot to act as a test reviewer and lists constraints, but
contains no example input/output pair. How should it be classified?

- A. Few-shot, because the role implies multiple hidden examples.
- B. One-shot, because there is one role.
- C. Fine-tuning, because the prompt changes model weights.
- D. Zero-shot with role/task instructions.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Shot count concerns demonstrations, not role count.
A and B miscount examples. C confuses inference-time context with training.
A role can guide emphasis without providing a concrete demonstration.
Review [prompting approaches](prompt-engineering.md#prompting-approaches).
</details>

### M30. Refinement from a failure

A generated implementation mishandles exactly the threshold value.
What is the most effective follow-up?

- A. Provide the failing input, expected result, relevant code, and focused regression test; constrain the repair.
- B. Ask it to make the suite green by deleting the failing test.
- C. Repeat the original broad prompt without new evidence.
- D. Add several unrelated features while it edits the threshold.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** A concrete counterexample and constrained repair narrow the
feedback loop. B removes useful evidence. C does not address the identified
gap. D expands scope and regression risk.
Review [prompt refinement](prompt-engineering.md#diagnose-a-weak-response).
</details>

## Developer productivity

### M31. Modernizing legacy code

Copilot proposes a broad legacy rewrite that changes errors and response
shapes. Existing behavior is still supported. What should come first?

- A. Merge first, then write tests for the new behavior.
- B. Remove compatibility checks to simplify modernization.
- C. Establish characterization/contract tests and scope the change to preserve intended behavior.
- D. Treat the generated documentation as proof of compatibility.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** A baseline exposes unintended behavior changes.
A tests only after the regression. B removes the contract. D is prose, not
execution evidence. Review [SDLC and modernization](productivity.md).
</details>

### M32. Measuring useful impact

A Copilot pilot generated twice as many lines of code but required substantial
review and rework. Which measurement best evaluates productivity?

- A. Generated line count alone.
- B. End-to-end completion/lead time, review/rework, defects, and quality against a defined baseline.
- C. The number of suggestions displayed without considering outcomes.
- D. Model response speed while ignoring integration time.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Measure the workflow and quality, not drafting volume alone.
A/C reward activity regardless of value. D omits downstream cost.
Review [impact measurement](productivity.md#measure-actual-impact).
</details>

### M33. Evidence that a test matters

Which two actions help establish that generated tests detect the intended
behavior? **Select two.**

- A. Compare assertions to an independent requirement and cover meaningful boundaries.
- B. Use line coverage as the sole proof of semantic correctness.
- C. Introduce a controlled wrong implementation in a disposable copy and verify a relevant test fails.
- D. Compute expected values by copying the same algorithm from production code.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A, C.** Independent oracles and falsification reveal useful behavior
coverage. B can count executed lines with weak assertions.
D can reproduce the implementation's mistake in the expected value.
Review [testing workflow](productivity.md#testing-workflow).
</details>

### M34. Sample data for boundary tests

A team needs test data for formatting and validation. Which source best
reduces unnecessary privacy risk?

- A. Synthetic schema-valid data plus deliberate invalid/boundary cases, reviewed for realism.
- B. Production customer exports, because realistic data always outweighs privacy concerns.
- C. Real credentials embedded as fixtures to prove authentication works.
- D. A public screenshot of a customer's private account.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: A.** Synthetic data can exercise the schema and boundaries without
unnecessary disclosure. B ignores minimization. C introduces secret handling
risks. D is not a safe or appropriate data source.
Review [productivity use cases](productivity.md).
</details>

### M35. A proposed optimization

Copilot says a new algorithm is faster and safer. What evidence should the
developer seek before accepting it?

- A. The confidence of the explanation alone.
- B. More generated lines than the previous implementation.
- C. Behavior-preserving tests, representative profiling/benchmarks, and verification of security assumptions.
- D. A benchmark that excludes the workload where the original problem occurs.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Test correctness and measure performance under relevant inputs;
verify security claims independently. A/B are not outcome evidence.
D can conceal the regression or fail to measure the intended improvement.
Review [security and performance](productivity.md#security-and-performance).
</details>

## Privacy, exclusions, and safeguards

### M36. Supported exclusion is not isolation

Current documentation lists exclusion support for the team's Copilot CLI.
An administrator concludes no possible tool can ever read an excluded file.
What is the best correction?

- A. Supported exclusions make OS permissions irrelevant.
- B. Exclusions are tool/context guardrails, not a filesystem boundary; indirect and third-party access need separate controls.
- C. Every CLI mode universally lacks exclusions, regardless of current documentation.
- D. A matching-code filter is sufficient to protect the file.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Current support does not guarantee prevention of every file
access path. A overstates protection. C repeats outdated universal guidance.
D addresses public-code similarity, not local file authorization.
Source: [current content-exclusion support and limits](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion).
</details>

### M37. Policy applies to the wrong population

An organization exclusion works for one user but not another. Before
reinstalling the IDE, what should be checked?

- A. Only whether both users typed the same prompt.
- B. Whether the generated output has the same number of lines.
- C. Whether the repository has enough stars.
- D. The signed-in identity, seat assignment, policy scope, plan/client support, and matching paths.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: D.** Effective applicability can differ by user and scope.
A is insufficient to establish policy application. B/C are irrelevant.
Investigate the configuration before assuming installation corruption.
Review [exclusion troubleshooting](privacy-safeguards.md#troubleshooting-checklist).
</details>

### M38. Unknown license on a match

A public-code reference shows a matching repository but no identified license.
Which two actions are appropriate? **Select two.**

- A. Treat unknown as permission for unrestricted reuse.
- B. Inspect the original source/repository and applicable license information.
- C. Follow the project's legal/licensing review process before accepting uncertain reuse.
- D. Assume public visibility proves the code is public domain.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B, C.** Public availability and license suitability are different.
A/D infer rights that have not been established.
A detected license is useful context, not automatic project approval either.
Review [ownership and public code](privacy-safeguards.md#ownership-and-public-code).
</details>

### M39. Matching-code filter scope

An administrator blocks suggestions matching public code. What should the
team still do with suggestions that remain?

- A. Assume all remaining code is original, secure, and license-compatible.
- B. Remove human review because the filter handles correctness.
- C. Validate behavior/security and assess licensing suitability; understand the filter's limited scope.
- D. Treat the filter as an access-control system for private files.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: C.** Matching controls reduce a specific category of risk.
A overstates what no detected match proves. B drops engineering review.
D confuses similarity filtering with authorization/exclusions.
Review [safeguards](privacy-safeguards.md#ownership-and-public-code).
</details>

### M40. A newly saved exclusion

An already-open supported IDE still offers suggestions immediately after a
valid exclusion change. What is the best next troubleshooting step?

- A. Assume the setting has failed permanently and disable all safeguards.
- B. Confirm effective scope/patterns, then follow documented propagation and client refresh steps.
- C. Copy the excluded content into a different file to test a workaround.
- D. Change production access policies without checking which user/client is affected.

<details markdown="1"><summary>Answer and rationale</summary>

**Answer: B.** Check applicability and known refresh behavior before escalating.
A abandons protections without evidence. C works around the intended
boundary. D expands the incident before identifying the cause.
Review [exclusion troubleshooting](privacy-safeguards.md#troubleshooting-checklist).
</details>

## Debrief before another attempt

Calculate each domain percentage, distinguish confident answers from guesses,
and write the rule behind every missed or uncertain choice.
Revisit the linked chapter and its official references, then complete an
[appropriate lab](hands-on-labs.md).
Use the [readiness plan](exam-preparation.md) and
[official practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/practice/assessment?assessment-type=practice)
for independent feedback. Do not map this practice score to the official
scaled score.
