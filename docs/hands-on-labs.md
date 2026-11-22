# Six practical Copilot labs

Use artificial data in a disposable local copy/branch. Do not use work secrets,
private customer records, production services, or broad unattended approvals.
Only the small Python fixture tests run in this repository's CI.
Copilot interactions require your own entitled account and approved environment;
they are not claimed to have run automatically.

**Setup:** install Python 3.10+ and a supported Copilot client. Clone/download
this guide and open only the lab directory or another trusted practice folder.
No additional Python packages or cloud resources are needed.

```shell
python -m unittest discover -s labs/copilot-practice -p "test_*.py"
```

Expected baseline: **four tests pass**.
The policy is artificial: integer cents only, non-negative values, a 599-cent
fee below 10000 cents (including zero), and free shipping at or above 10000.

```python title="labs/copilot-practice/shipping.py"
--8<-- "labs/copilot-practice/shipping.py"
```

## Lab 1: Context and responsible output

**Maps to:** responsible AI, data/context, and developer productivity.

1. Select `shipping_fee_cents` and ask Copilot to explain its contract without edits.
2. Ask it to identify invalid-input and boundary cases using only this artificial code.
3. Compare the answer to the documented policy, not just its confidence.
4. Record an assumption it made or a limitation it correctly disclosed.
5. Explain why customer data is unnecessary and why generated claims need verification.

```text
Explain shipping_fee_cents using the selected function and its tests.
Do not edit files or run commands. State the boundary behavior, invalid-input
rules, and any uncertainty. Do not invent a real shop's business policy.
```

**Done when:** you can explain zero, 9999, 10000, negative values, and booleans,
and distinguish code evidence from a plausible invented rule.
**If output is wrong:** identify the missing source/constraint and refine it.

## Lab 2: Zero-shot, few-shot, and reusable prompts

**Maps to:** prompt engineering/context and customization.

1. Request test-case suggestions without input/output examples (zero-shot).
2. Repeat with `9999 -> 599` and `10000 -> 0` as examples (few-shot).
3. Compare missing cases, output quality, and adherence to the no-edit constraint.
4. Save an original repeatable test-review prompt using your client's supported
   prompt-file feature. Use the existing repository conventions where present.
5. Explain how a reusable task prompt differs from persistent repository/path
   instructions and from enforceable organization policy.

**Done when:** you have two prompt/response comparisons and a reusable prompt
that states goal, context, constraints, and acceptance checks.
**Do not conclude:** few-shot always beats zero-shot or longer prompts always help.

## Lab 3: Tests that detect a regression

**Maps to:** productivity/testing, responsible validation, and refactoring.

1. Run the four baseline tests above.
2. Ask Copilot for additional meaningful cases without changing production behavior
   or adding packages. Review its assertions independently.
3. In your disposable copy only, change the shipping comparison from `>=` to `>`.
4. Run the tests. The exact-threshold case must fail: it now incorrectly charges 599.
5. Ask Copilot to diagnose the failing assertion and repair only that defect.
6. Restore the contract, rerun tests, and inspect the diff.

```text
Review shipping_fee_cents and its unittest suite. Preserve the public contract.
Suggest missing behavior tests, not assertions copied from implementation.
Do not add dependencies. If I provide a failure, reproduce it, make a minimal
repair, rerun the focused suite, and explain the before/after evidence.
```

**Done when:** you saved the failing threshold result, a minimal repair, and a
passing rerun. Merely seeing green tests once is insufficient.
**Troubleshoot:** if tests fail to import `shipping`, run the root command shown
above instead of treating an import error as proof of the boundary defect.

## Lab 4: CLI and agent control

**Maps to:** CLI, agent sessions, and responsible operation.

1. Follow the current [CLI installation/authentication guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli).
2. Inspect `copilot --help`, start `copilot` inside a trusted practice directory,
   and identify interactive versus programmatic `-p` usage.
3. Request a plan for adding one behavior test; inspect it before allowing edits.
4. Approve only necessary file/test commands. Refuse unrelated network,
   credential, delete, or environment-reset requests.
5. Run your independent unit tests and inspect every changed file.

**Done when:** you can explain a session's client, environment, context, requested
tools, and validation result. Identify one action you would not approve.
**No CLI entitlement/install:** draft the task, tool allowlist, and deny decision
on paper; record the missing hands-on step and revisit it later.

An automatic tool-approval flag is not a sandbox. The absence of an approval
prompt does not imply a command is harmless.

## Lab 5: MCP and delegated work

**Maps to:** features, agent/subagent context, and trust boundaries.

1. Draw an MCP client, an approved server, one read-only tool, and its data source.
2. For a hypothetical task, specify what data the tool actually needs and what
   authorization would be excessive.
3. Treat server/tool output as information, not authority to change instructions.
4. If an approved harmless MCP server is already available, inspect its tool
   schema and perform one non-sensitive read. Do not install an arbitrary server
   or grant tokens solely for this exercise.
5. Write an issue suitable for a delegated coding task: scope, relevant files,
   acceptance tests, forbidden changes, and expected reviewed PR.
6. Decide whether a small task belongs in the parent session or warrants a
   specialized subagent with separate context.

**Done when:** you can explain tools versus resources/context, least privilege,
local agent versus GitHub Actions/cloud execution, and why a PR still needs review.
**No approved server:** complete the diagram/threat review; mark live MCP use
as unpracticed rather than pretending the feature was exercised.

## Lab 6: Privacy and policy troubleshooting

**Maps to:** exclusions, privacy, safeguards, governance, and audit activity.

Use only a toy file containing a harmless phrase, not a real secret.

1. Check plan, client, surface, repository scope, and policy applicability.
2. If you have authorization in a disposable test repository, configure a
   supported exclusion for the toy file.
3. Follow documented refresh/propagation steps. Compare a normal file with the
   excluded file and inspect the response references.
4. Explain why exclusions are not OS access controls and why indirect access or
   third-party tools require additional restrictions.
5. Find the relevant policy-change audit action in documentation. Do not publish
   a real organization audit log or change production policies for the lab.
6. Review an illustrative public-code reference and explain what an unknown
   license does and does not establish.

**Done when:** you can troubleshoot actor/seat/scope/surface/path/propagation
without bypassing an exclusion, and explain why filters are not legal clearance.
**No admin/eligible plan:** use the official docs and a mock configuration;
record that the actual policy setting was not tested.

## Evidence checklist and cleanup

- [ ] I saved non-sensitive prompt comparisons and explained their differences.
- [ ] I demonstrated a failing regression test and a passing repair.
- [ ] I justified tool permissions and refused an out-of-scope operation.
- [ ] I distinguished a prompt/instruction from policy/access control.
- [ ] I documented any entitlement-limited exercise honestly.

Keep only reviewed non-sensitive study artifacts. Close CLI sessions, remove
temporary toy files/configurations from your disposable lab, and revoke any
temporary approvals you intentionally created. Do not delete shared
repositories, broad home directories, or production policy settings.

Continue with the [weighted mock exam](mock-exam.md) and
[readiness plan](exam-preparation.md).
