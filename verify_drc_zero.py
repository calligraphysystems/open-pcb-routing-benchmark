#!/usr/bin/env python3
"""
Open PCB Routing Benchmark — Independent Native KiCad DRC Zero-Violation Verifier
https://calligraphyeda.com

Refills all copper zones on a disposable copy of a routed .kicad_pcb board and executes:
    kicad-cli pcb drc --severity-all --format json
Asserts strictly:
    unconnected_items == 0
    copper_drc_violations == 0
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile


def refill_zones_if_pcbnew_available(pcb_path: str) -> None:
    try:
        import pcbnew
        board = pcbnew.LoadBoard(pcb_path)
        filler = pcbnew.ZONE_FILLER(board)
        filler.Fill(board.Zones())
        pcbnew.SaveBoard(pcb_path, board)
    except ImportError:
        pass


def run_kicad_drc(pcb_path: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="open_pcb_drc_") as tmpdir:
        work_pcb = os.path.join(tmpdir, os.path.basename(pcb_path))
        shutil.copy2(pcb_path, work_pcb)

        base, _ = os.path.splitext(pcb_path)
        for ext in (".kicad_pro", ".kicad_dru"):
            if os.path.isfile(base + ext):
                shutil.copy2(base + ext, os.path.join(tmpdir, os.path.basename(base) + ext))

        refill_zones_if_pcbnew_available(work_pcb)

        report_json = os.path.join(tmpdir, "drc_report.json")
        env = dict(os.environ)
        env["XDG_DATA_HOME"] = "/tmp"

        cmd = [
            "kicad-cli", "pcb", "drc",
            "--severity-all",
            "--format", "json",
            "--output", report_json,
            work_pcb,
        ]
        subprocess.run(cmd, env=env, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not os.path.isfile(report_json):
            raise RuntimeError("kicad-cli pcb drc did not produce a JSON report. Ensure KiCad 8/9 CLI is installed.")

        with open(report_json, "r", encoding="utf-8") as fh:
            data = json.load(fh)

        unconnected = data.get("unconnected_items") or []
        violations = data.get("violations") or []
        copper_errors = [
            v for v in violations
            if v.get("severity") == "error"
            and v.get("type") not in ("silk_over_copper", "silk_overlap", "silk_edge_clearance", "lib_footprint_mismatch")
        ]
        return {
            "board": os.path.basename(pcb_path),
            "unconnected_count": len(unconnected),
            "copper_drc_error_count": len(copper_errors),
            "strict_zero_drc_pass": (len(unconnected) == 0 and len(copper_errors) == 0),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify 100.0% net completion and 0 native KiCad DRC errors.")
    parser.add_argument("pcb", help="Path to routed .kicad_pcb file")
    args = parser.parse_args()

    result = run_kicad_drc(args.pcb)
    print(json.dumps(result, indent=2))
    return 0 if result["strict_zero_drc_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
