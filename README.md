# Study Guide: GitHub Copilot (GH-300)

!!! note
	This independent study guide contains original study notes and diagrams, not official exam questions. It follows the [GH-300 Microsoft Learn study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300). Use the [GitHub Copilot certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/) for current exam details, the practice assessment, and scheduling information.

<details markdown="1">
<summary><b>List of official references</b> (Click to expand)</summary>

- [GH-300 study guide and skills measured](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)
- [GitHub Copilot certification](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/)
- [GitHub Copilot Fundamentals Part 1](https://learn.microsoft.com/en-us/training/paths/copilot/)
- [GitHub Copilot Fundamentals Part 2](https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)

</details>

## Start here: prepare with evidence

1. Follow the [14-day study and readiness plan](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/exam-preparation/).
2. Use the [objective coverage map](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/objective-map/) to identify gaps across all six domains.
3. Read the existing chapters and Microsoft Learn summaries, then complete [six practical labs](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/hands-on-labs/).
4. Answer **88 original questions**: the [48-question foundation bank](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/practice-questions/) and [40-question weighted mock exam](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/mock-exam/).
5. Track mistakes by domain and verify readiness with the official practice assessment. A practice percentage is not the official scaled score or a pass guarantee.

**Sources checked: November 22, 2026.** The guide distinguishes the published
August 7, 2026 exam objectives from changing product behavior. In particular,
current supported CLI/IDE agent exclusions are guardrails, not filesystem
isolation. Spark remains named in those objectives, but its github.com creation
experience was retired; do not plan a new Spark hands-on exercise.

## Content

- [Use GitHub Copilot responsibly](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/responsible-ai/)
- [Use GitHub Copilot features](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/copilot-features/)
- [Understand data and architecture](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/data-architecture/)
- [Apply prompt engineering and context crafting](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/prompt-engineering/)
- [Improve developer productivity](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/productivity/)
- [Configure privacy, exclusions, and safeguards](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/privacy-safeguards/)
- [Summarize GitHub Copilot Fundamentals Part 1](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/learning-path-part-1/)
- [Summarize GitHub Copilot Fundamentals Part 2](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/learning-path-part-2/)
- [Practice with 48 original scenario questions](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/practice-questions/)

## Skills measured

| Official domain | Weight |
| --- | ---: |
| Use GitHub Copilot responsibly | 15-20% |
| Use GitHub Copilot features | 25-30% |
| Understand GitHub Copilot data and architecture | 10-15% |
| Apply prompt engineering and context crafting | 10-15% |
| Improve developer productivity with GitHub Copilot | 10-15% |
| Configure privacy, content exclusions, and safeguards | 10-15% |

## Microsoft Learn study map

The two official paths contain 15 modules and approximately 519 minutes of instruction. The local Part 1 and Part 2 summaries follow every module in order, highlight product boundaries and governance details, and point back to the official exercises. Use the six exam-domain chapters for focused revision, then complete the Microsoft Learn content and hands-on exercises.

| Study goal | Guide summary | Official Microsoft Learn resource |
| --- | --- | --- |
| Core concepts, prompting, governance, SDLC, and tests | [Part 1 summary](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/learning-path-part-1/) | [GitHub Copilot Fundamentals Part 1](https://learn.microsoft.com/en-us/training/paths/copilot/) |
| Agents, MCP, reviews, JavaScript, and Python | [Part 2 summary](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/learning-path-part-2/) | [GitHub Copilot Fundamentals Part 2](https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/) |
| Practice responsible operation | [Responsible AI chapter](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/responsible-ai/) | [Responsible AI with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/) |
| Apply Copilot across the SDLC | [Productivity chapter](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/productivity/) | [Developer use cases for AI with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/) |
| Generate and review tests | [Testing workflow](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/productivity/#testing-workflow) | [Develop unit tests using GitHub Copilot tools](https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/) |
| Check exam readiness | [Weighted mock exam](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/mock-exam/) and [readiness plan](https://cloud2br-msftlearninghub.github.io/GH-300StudyGuide/exam-preparation/) | [Official GitHub Copilot practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/practice/assessment?assessment-type=practice) |

!!! tip
	The current English exam skills measured as of August 7, 2026 are reflected here. Review the current [skills measured](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300) before scheduling the exam.

## Local validation

The Python lab uses only the standard library. Documentation and learning
materials are validated on pull requests; validated main changes deploy Pages.

```shell
python -m unittest discover -s labs/copilot-practice -p "test_*.py"
python scripts/validate_study_material.py
python -m pip install -r requirements.txt
mkdocs build --strict
python scripts/check_site.py
```

CI also proves the threshold test detects a controlled regression in an isolated
temporary copy; it never leaves a broken implementation in the lab.

<figure class="product-visual certification-badge">
	<a href="https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/"><img src="assets/images/github-copilot-certification.svg" alt="Official GitHub Copilot certification badge from Microsoft Learn" /></a>
	<figcaption>Image source: <a href="https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/">Microsoft Learn, GitHub Copilot certification</a>.</figcaption>
</figure>
