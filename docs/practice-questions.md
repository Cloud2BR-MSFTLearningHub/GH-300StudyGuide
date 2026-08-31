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

## Continue preparing

When you can explain every answer and reject each distractor, use the official [GitHub Copilot practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/practice/assessment?assessment-type=practice) to check readiness.