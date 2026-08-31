# GH-300 practice questions

> **Important:** These are original study questions, not Microsoft or GitHub exam questions. Use the [official GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300) and practice assessment as the final authority.

Answer before opening each rationale, explain why the distractors fail, and revisit the linked documentation for weak areas.

| Domain | Questions |
| --- | ---: |
| Responsible use | 1-3 |
| Copilot features | 4-6 |
| Data and architecture | 7-9 |
| Prompt engineering | 10-12 |
| Developer productivity | 13-15 |
| Privacy and safeguards | 16-18 |
| Learning path Part 1 | 19-36 |
| Learning path Part 2 | 37-48 |

## Responsible use

### 1. Plausible output

Copilot generates code that compiles. What should the developer do next?

- A. Merge it because compilation proves correctness.
- B. Review, test, and scan it against the requirements.
- C. Remove all existing tests.
- D. Treat it as official documentation.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Compilation checks only part of correctness. Human review, tests, and appropriate security checks remain necessary.
</details>

### 2. Sensitive context

A debugging prompt would include customer records. What is the best first action?

- A. Include every record for more context.
- B. Minimize or sanitize the data and follow organizational policy.
- C. Put the records in a code comment.
- D. Disable tests.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Data minimization reduces privacy risk. Sensitive data must be handled under applicable policy.
</details>

### 3. Accountability

Who is responsible for an accepted Copilot-generated production change?

- A. Nobody, because AI wrote it.
- B. Only the model provider.
- C. The people and organization approving and operating it.
- D. The compiler.

<details markdown="1"><summary>Answer and rationale</summary>

**C.** Copilot assists; it does not transfer engineering accountability.
</details>

## Copilot features

### 4. Choosing a surface

A task requires coordinated edits and test runs across several local files. Which surface fits best?

- A. Inline completion only
- B. Agent mode
- C. A repository star
- D. GitHub Pages

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Agent mode is designed for multi-step local work with edits and tools.
</details>

### 5. Delegated task

A developer assigns a repository issue to Copilot coding agent. How should the result normally arrive?

- A. As an unreviewed direct push to the default branch
- B. As a pull request from an isolated environment
- C. As an email attachment
- D. As a local stash

<details markdown="1"><summary>Answer and rationale</summary>

**B.** The coding agent works independently and proposes changes through a pull request for review.
</details>

### 6. Organization investigation

An administrator needs to investigate Copilot policy activity. What should they use?

- A. Audit log events
- B. Markdown headings
- C. Git tags
- D. Repository topics

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Audit logs provide administrative activity records; organization and enterprise settings control policies.
</details>

## Data and architecture

### 7. Context source

Which item can directly improve a chat response about a selected function?

- A. The active selection and relevant file
- B. An unrelated archived repository
- C. A repository star count
- D. The monitor resolution

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Relevant selected code gives the model direct context for the request.
</details>

### 8. Variable output

Why might an identical prompt produce a different answer later?

- A. Model generation is probabilistic and context or service behavior can change.
- B. Copilot always returns one stored answer.
- C. Git commits prohibit repeated output.
- D. Markdown randomizes code.

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Model, context, settings, and service updates can all affect probabilistic generation.
</details>

### 9. Exclusion boundary

What does a supported content exclusion primarily affect?

- A. Whether configured content enters Copilot context
- B. Repository read permissions
- C. Git commit signatures
- D. Network firewall rules

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Exclusion controls supported Copilot context. It is not an access-control system.
</details>

## Prompt engineering

### 10. Few-shot prompt

When is few-shot prompting especially useful?

- A. When several examples clarify a nuanced output pattern
- B. When no task has been defined
- C. When repository permissions are missing
- D. When deleting all context

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Multiple examples can demonstrate structure or distinctions that prose alone does not convey efficiently.
</details>

### 11. Context quality

A prompt includes many unrelated files and stale chat turns. What is the best improvement?

- A. Add more unrelated text.
- B. Start a focused interaction with only relevant context and constraints.
- C. Remove the goal.
- D. Omit acceptance criteria.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Relevant, noncontradictory context improves signal and preserves the context window.
</details>

### 12. Acceptance criteria

Which acceptance criterion is most useful?

- A. Make it better.
- B. Reject malformed email input and keep the existing response schema.
- C. Write some code.
- D. Use AI.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** It states observable behavior and a compatibility constraint that can be tested.
</details>

## Developer productivity

### 13. Legacy refactor

What should precede a broad behavior-preserving refactor?

- A. Delete existing tests.
- B. Establish characterization and regression coverage.
- C. Change every dependency simultaneously.
- D. Skip review.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Behavior coverage detects unintended changes and supports incremental modernization.
</details>

### 14. Generated test

A generated test passes immediately. Why must its assertions still be reviewed?

- A. It may assert the implementation's mistake or never exercise the intended path.
- B. Passing tests are always invalid.
- C. Copilot cannot produce test syntax.
- D. Assertions affect repository permissions.

<details markdown="1"><summary>Answer and rationale</summary>

**A.** A passing test proves little if it tests the wrong behavior or fails to reach the target code.
</details>

### 15. Security suggestion

Copilot identifies a possible injection risk. What is the right response?

- A. Treat the statement as a completed security certification.
- B. Verify it with code analysis, tests, documentation, and human review.
- C. Publish the vulnerable input.
- D. Disable authentication.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** AI output is a lead to investigate, not proof that a vulnerability exists or is fixed.
</details>

## Privacy and safeguards

### 16. Protecting a secret

A credential was committed to an excluded path. What should the team do?

- A. Assume the exclusion secures it.
- B. Remove and rotate the credential, then use proper secret management.
- C. Add it to another prompt.
- D. Make the repository public.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Content exclusion is not secret protection or repository access control.
</details>

### 17. Public-code match

Copilot provides a reference for a suggestion matching public code. What should be reviewed?

- A. Source, repository, license, and project suitability
- B. Only indentation
- C. Only the file name
- D. Nothing; a reference guarantees permission

<details markdown="1"><summary>Answer and rationale</summary>

**A.** A reference supports investigation but does not replace licensing, security, and quality review.
</details>

### 18. Exclusion troubleshooting

An excluded file seems to influence a feature. What should be confirmed first?

- A. Whether that specific feature supports content exclusions
- B. Whether the repository has stars
- C. Whether a release exists
- D. Whether Markdown tables render

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Support differs across Copilot surfaces; then check scope, patterns, propagation, account, and client state. Review [content exclusion](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion).
</details>

## Learning path Part 1 review

### 19. Responsible AI mitigation

A generated function passes its happy-path test but processes financial eligibility. What is the most responsible next step?

- A. Deploy because the test passed.
- B. Validate edge cases, fairness, security, and business rules with accountable reviewers.
- C. Hide that AI was used.
- D. Ask for a longer function.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** High-impact logic needs evidence across correctness, fairness, security, and domain requirements. One passing example is insufficient.
</details>

### 20. Transparency

Which action best supports transparency when a team uses generated code?

- A. Make the model the code owner.
- B. Preserve review context and explain relevant AI limitations to stakeholders.
- C. Remove the test results.
- D. Assume users understand the model.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Transparency makes AI involvement, evidence, and limitations understandable without transferring accountability to the model.
</details>

### 21. Copilot setup troubleshooting

Copilot works for one organization member but not another in the same IDE. What should be checked first?

- A. Monitor size
- B. Signed-in account, assigned seat, policy, extension state, and network access
- C. Repository star count
- D. Commit message length

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Availability depends on identity, entitlement, policy, client configuration, and connectivity.
</details>

### 22. Inline suggestion trigger

Which context is most likely to produce a useful inline function body?

- A. A descriptive function name, types, nearby code, and a focused comment
- B. An unrelated chat from yesterday
- C. An empty file with no language mode
- D. A repository topic

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Local code structure and an explicit description give completion models relevant intent and constraints.
</details>

### 23. Prompt decomposition

A request to “build the entire inventory system” produces inconsistent output. What should the developer do?

- A. Repeat the identical prompt indefinitely.
- B. Split the goal into architecture, data model, API, UI, and test milestones with acceptance criteria.
- C. Remove all constraints.
- D. Add unrelated files.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Smaller, independently verifiable tasks reduce ambiguity and make feedback actionable.
</details>

### 24. Role prompting

What does telling Copilot to act as a security reviewer accomplish?

- A. It grants security permissions.
- B. It guides the response's focus but does not enforce policy or prove security.
- C. It replaces code scanning.
- D. It makes output deterministic.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** A role is prompt context. Authorization, enforcement, and validation come from separate controls.
</details>

### 25. Designing a Space

A team creates a Copilot Space for on-call support. Which source set is strongest?

- A. Every file the organization owns
- B. Current runbooks, service architecture, escalation policy, and recent resolved incidents
- C. Unreviewed personal notes only
- D. Empty instructions and no sources

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Focused, authoritative, current sources support grounded answers for the Space's purpose.
</details>

### 26. Space governance

What should happen when a runbook in a shared Space becomes obsolete?

- A. Leave it because more context is always better.
- B. Update or remove it and retest representative questions.
- C. Duplicate it several times.
- D. Make the Space public.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Stale sources degrade grounding. Curated context requires maintenance and validation.
</details>

### 27. Advanced feature workflow

Before asking Copilot to update an unfamiliar web API, what should the developer do?

- A. Ask it to rewrite every file.
- B. Inspect project conventions, dependencies, tests, and the request flow.
- C. Delete the test project.
- D. Upgrade every package.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Understanding the local system establishes constraints and the smallest safe change surface.
</details>

### 28. Refining from evidence

An agent-generated API change fails one focused test. What is the best follow-up context?

- A. The exact failure, expected behavior, and relevant implementation
- B. “Try harder”
- C. An unrelated repository
- D. No error output

<details markdown="1"><summary>Answer and rationale</summary>

**A.** A concrete failure is grounding evidence that helps distinguish an implementation defect from a wrong assumption.
</details>

### 29. Choosing an environment

A developer wants a conversational terminal session that can inspect Git history and create a pull request. Which tool fits?

- A. Copilot CLI
- B. GitHub Pages
- C. Repository Insights
- D. Markdown preview

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Copilot CLI supports terminal-native project, Git, and GitHub tasks in interactive sessions.
</details>

### 30. Terminal permissions

Why is `--allow-all-tools` risky in a Copilot CLI automation?

- A. It disables output formatting.
- B. It permits commands and file operations without individual approval.
- C. It prevents network access.
- D. It changes the repository license.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Broad automatic approval can expose all permissions available to the user; narrow allowlists and sandboxing reduce risk.
</details>

### 31. Policy versus instruction

Which item enforces whether organization members may use a Copilot feature?

- A. A prompt file
- B. Organization or enterprise policy
- C. A code comment
- D. A README heading

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Instructions guide responses; administrative policies control feature availability.
</details>

### 32. Exclusion propagation

An administrator saves a valid exclusion, but an already-open IDE still offers suggestions. What is a reasonable next check?

- A. Reload the client and account for propagation time.
- B. Delete the repository immediately.
- C. Add the secret to the prompt.
- D. Disable source control.

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Exclusions can take time to propagate; supported clients provide refresh or restart procedures.
</details>

### 33. Measuring productivity

Which metric best tests whether Copilot improved the whole delivery workflow?

- A. Number of generated lines only
- B. Lead time, review effort, rework, defects, and developer satisfaction against a baseline
- C. Number of prompts only
- D. Suggestion acceptance alone

<details markdown="1"><summary>Answer and rationale</summary>

**B.** End-to-end measures detect whether faster drafting created downstream review or quality costs.
</details>

### 34. SDLC boundary

During requirements analysis, what is an appropriate Copilot role?

- A. Make the final stakeholder decision.
- B. Turn confirmed stories into prototype structures and candidate APIs.
- C. Approve production deployment.
- D. Replace domain experts.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Copilot can accelerate artifacts, while stakeholders retain ownership of intent and acceptance criteria.
</details>

### 35. Planning tests

A method has complex boundaries, but the team is not ready for file changes. Which mode should they start with?

- A. Ask mode to enumerate cases, then Plan or Agent as needed
- B. Autopilot with unrestricted tools
- C. Inline completion in an empty file
- D. Cloud deployment

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Ask mode supports analysis without mutation and can establish a reviewed test strategy first.
</details>

### 36. Proving a generated test

What is a strong way to show that a generated regression test is meaningful?

- A. Confirm it passes only after the fix.
- B. Observe it fail for the targeted defect and pass after the fix.
- C. Count its lines.
- D. Remove its assertions.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** The fail-then-pass evidence demonstrates that the test detects the behavior it claims to protect.
</details>

## Learning path Part 2 review

### 37. Agent mode acceptance criteria

Which prompt gives agent mode the strongest basis for a multi-file change?

- A. “Improve the app.”
- B. “Add pagination to the orders endpoint, preserve its response schema, add boundary tests, and run the API test project.”
- C. “Write lots of code.”
- D. “Use your best judgment with no constraints.”

<details markdown="1"><summary>Answer and rationale</summary>

**B.** It defines scope, compatibility constraints, evidence, and a validation command while leaving implementation details discoverable.
</details>

### 38. Agent mode oversight

An IDE agent requests permission to run a database reset script while implementing a UI label. What should the developer do?

- A. Approve because agents require every tool.
- B. Deny it and ask why the unrelated destructive action is necessary.
- C. Disable source control.
- D. Give the agent production credentials.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Tool approval is a security boundary. The command is disproportionate to the stated goal and should be challenged.
</details>

### 39. Cloud delegation

A developer wants to delegate a bounded backlog issue and review a pull request later. Which feature is designed for this?

- A. Inline suggestions
- B. Copilot Cloud Agent
- C. Markdown preview
- D. Ask mode

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Cloud Agent works asynchronously in a GitHub-hosted environment and can create a branch, commits, and pull request.
</details>

### 40. Agent-created workflow

Why might a workflow added by Cloud Agent show an **Approve and run workflows** button?

- A. Markdown cannot render automatically.
- B. Workflows from agent-created pull requests are held by default so a reviewer can inspect potentially privileged automation.
- C. Copilot cannot write YAML.
- D. The pull request has no branch.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Workflow code can access credentials or perform sensitive actions, so deliberate human approval is an important safeguard.
</details>

### 41. MCP tool selection

An MCP server exposes 40 tools, but a task only needs read access to two issue queries. What is the safest configuration?

- A. Enable every tool permanently.
- B. Enable only the two required read tools for the task.
- C. Store an administrator token in the repository.
- D. Turn off tool confirmations globally.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Least privilege limits both accidental actions and the impact of malicious or misleading context.
</details>

### 42. MCP configuration scope

Where should a team place reviewed MCP configuration that should travel with one repository in Visual Studio Code?

- A. `.vscode/mcp.json`
- B. A public issue comment containing credentials
- C. The compiled application binary
- D. A commit message

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Repository-level MCP configuration belongs in `.vscode/mcp.json`; secrets still require supported secure authentication.
</details>

### 43. Copilot review status

Copilot finds no issues in a required-review pull request. What review state does it submit?

- A. Approve
- B. Request changes
- C. Comment
- D. Merge

<details markdown="1"><summary>Answer and rationale</summary>

**C.** Copilot always leaves a Comment review and does not satisfy required human approvals or block a merge.
</details>

### 44. Re-review after changes

An author pushes a substantial fix after Copilot reviewed the pull request. Automatic review of new pushes is disabled. What is required?

- A. Nothing; the old review covers future commits.
- B. Explicitly request Copilot review again.
- C. Close the repository.
- D. Delete all previous comments.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** A review applies to the observed changes. Without automatic review of new pushes, another request is needed.
</details>

### 45. JavaScript validation

Copilot generates a click handler that compiles but never runs in the browser. Which check is most useful first?

- A. Verify the DOM selector, script loading, event binding, and browser console.
- B. Add more Markdown.
- C. Rename the repository.
- D. Increase the prompt length without evidence.

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Runtime DOM behavior depends on page structure and loading order, which static syntax success does not prove.
</details>

### 46. JavaScript security

A generated portfolio feature inserts user text with `innerHTML`. What should the developer examine?

- A. Cross-site scripting risk and safer text or sanitization APIs
- B. Repository color theme
- C. Commit count
- D. File extension length

<details markdown="1"><summary>Answer and rationale</summary>

**A.** Untrusted HTML insertion can create an injection vulnerability even when the feature appears to work.
</details>

### 47. Python API validation

A generated Python endpoint returns the right data for one request. Which evidence is still important?

- A. Invalid-input tests, status codes, schema serialization, exception handling, and dependency behavior
- B. Number of blank lines
- C. Repository stars
- D. Prompt token count alone

<details markdown="1"><summary>Answer and rationale</summary>

**A.** One successful request does not establish the API contract across failures, boundaries, and framework behavior.
</details>

### 48. Python project conventions

Copilot suggests a library that conflicts with the project's dependency and async patterns. What is the best response?

- A. Accept it because generated code is current by definition.
- B. Constrain the prompt to the existing stack and verify the dependency API in current documentation.
- C. Remove the lock file.
- D. Skip tests.

<details markdown="1"><summary>Answer and rationale</summary>

**B.** Repository conventions and authoritative dependency documentation are stronger evidence than an unconstrained suggestion.
</details>

## Continue preparing

When you can explain every answer and reject each distractor, use the official [GitHub Copilot practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/practice/assessment?assessment-type=practice) to check readiness.