import subprocess
import sys
from pathlib import Path
from generate_cpe_pack import PROBLEMS

ROOT = Path(__file__).resolve().parent

def main():
    passed = 0
    total = 0
    for problem in PROBLEMS:
        script = ROOT / "solutions" / problem["file"]
        for sample_in, expected in problem.get("tests", []):
            total += 1
            result = subprocess.run(
                [sys.executable, str(script)],
                input=sample_in,
                text=True,
                capture_output=True,
                timeout=5,
            )
            if result.returncode != 0:
                print(f"FAIL {problem['no']:02d} {problem['uva']} runtime error")
                print(result.stderr)
                return 1
            if result.stdout != expected:
                print(f"FAIL {problem['no']:02d} {problem['uva']}")
                print("Expected:")
                print(repr(expected))
                print("Got:")
                print(repr(result.stdout))
                return 1
            passed += 1
    print(f"All {passed}/{total} sample checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
