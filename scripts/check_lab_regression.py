"""Prove the threshold test fails on a controlled mutation, without editing the lab."""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run_boundary_test(directory):
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            "-m",
            "unittest",
            "test_shipping.ShippingTests.test_free_shipping_boundary_and_above",
        ],
        cwd=directory,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode, result.stdout + result.stderr


def main():
    source = Path(__file__).resolve().parents[1] / "labs/copilot-practice"
    with tempfile.TemporaryDirectory(prefix="gh300-regression-") as temporary:
        directory = Path(temporary)
        for name in ("shipping.py", "test_shipping.py"):
            shutil.copy2(source / name, directory / name)
        code_path = directory / "shipping.py"
        original = code_path.read_text(encoding="utf-8")
        if original.count("subtotal_cents >= 10000") != 1:
            raise ValueError("Expected one exact-threshold comparison to exercise")
        status, output = run_boundary_test(directory)
        if status != 0:
            raise RuntimeError(f"Baseline boundary test failed:\n{output}")
        code_path.write_text(
            original.replace("subtotal_cents >= 10000", "subtotal_cents > 10000"),
            encoding="utf-8",
        )
        status, output = run_boundary_test(directory)
        if status != 1 or "(subtotal=10000)" not in output or "599 != 0" not in output:
            raise RuntimeError(f"Mutation did not fail on the expected threshold assertion:\n{output}")
        print("Controlled mutation correctly failed at subtotal=10000 (599 != 0).")
        code_path.write_text(original, encoding="utf-8")
        status, output = run_boundary_test(directory)
        if status != 0:
            raise RuntimeError(f"Restored boundary test failed:\n{output}")
    print("Restored test passed; temporary copy removed; repository lab unchanged.")


if __name__ == "__main__":
    main()
