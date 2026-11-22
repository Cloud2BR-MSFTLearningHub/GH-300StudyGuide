"""Validate question completeness and the advertised domain-weighted bank."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    foundation = (ROOT / "docs/practice-questions.md").read_text(encoding="utf-8")
    if re.findall(r"^### (\d+)\.", foundation, re.MULTILINE) != [
        str(number) for number in range(1, 49)
    ]:
        raise ValueError("Foundation questions must have unique sequential IDs 1-48")

    mock = (ROOT / "docs/mock-exam.md").read_text(encoding="utf-8")
    questions = re.split(r"^### M(\d{2})\.", mock, flags=re.MULTILINE)
    if questions[1::2] != [f"{number:02}" for number in range(1, 41)]:
        raise ValueError("Mock questions must have unique sequential IDs M01-M40")

    for number, text in zip(questions[1::2], questions[2::2]):
        stem = text.split("<details", 1)[0]
        if re.findall(r"^- ([A-D])\.", stem, re.MULTILINE) != list("ABCD"):
            raise ValueError(f"M{number}: requires exactly four ordered options")
        if text.count('<details markdown="1">') != 1 or text.count("</details>") != 1:
            raise ValueError(f"M{number}: requires one collapsible rationale")
        answer = re.search(r"\*\*Answer: ([A-D](?:, [A-D])*)\.\*\*", text)
        if not answer:
            raise ValueError(f"M{number}: missing explicit answer key")
        selected = answer.group(1).split(", ")
        required = 2 if "Select two" in stem else 1
        if len(selected) != required or len(set(selected)) != required:
            raise ValueError(f"M{number}: selection count and answer key disagree")
        rationale = text.split(answer.group(0), 1)[1].split("</details>", 1)[0]
        if not rationale.strip() or not re.search(r"\[[^]]+\]\([^)]+\)", rationale):
            raise ValueError(f"M{number}: needs explanatory rationale and remediation link")
        for distractor in set("ABCD") - set(selected):
            if not re.search(rf"\b{distractor}\b", rationale):
                raise ValueError(f"M{number}: rationale must address distractor {distractor}")

    domains = [
        ("Responsible use", 7, 15, 20),
        ("Features", 11, 25, 30),
        ("Data and architecture", 6, 10, 15),
        ("Prompt engineering and context", 6, 10, 15),
        ("Developer productivity", 5, 10, 15),
        ("Privacy, exclusions, and safeguards", 5, 10, 15),
    ]
    for title, expected, lower, upper in domains:
        section = mock.split(f"## {title}\n", 1)[1].split("\n## ", 1)[0]
        count = len(re.findall(r"^### M\d{2}\.", section, re.MULTILINE))
        if count != expected or not lower <= count / 40 * 100 <= upper:
            raise ValueError(f"{title}: allocation does not match the documented weights")

    print("Verified 48 foundation + 40 complete mock questions; six domain allocations match official ranges.")


if __name__ == "__main__":
    main()
