# Open-Source PCB Routing Torture Benchmark (`100.0%` Completion & `0` Native KiCad DRC)

[![Live Benchmark Gallery](https://img.shields.io/badge/Interactive_Gallery-calligraphyeda.com-00e5ff?style=for-the-badge)](https://calligraphyeda.com)
[![Verification Gate](https://img.shields.io/badge/kicad--cli_pcb_drc-0_Violations-00e676?style=for-the-badge)](verify_drc_zero.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## Why Partial Autorouting (`87%–97%`) Fails Hardware Engineers

Every hardware engineer who has tried traditional maze autorouters (`Freerouting`, legacy push-and-shove scripts, or LLM tool-wrappers) knows the trap:

- A router that reaches **`94%` net completion** with **`45` DRC clearance violations** has not solved your board — it has boxed in the hardest 6% of nets (`0.40 mm–0.50 mm` fine-pitch QFP/QFN pins, off-axis rotated connectors, and split return planes) so badly that ripping up and fixing the remaining airwires by hand takes longer than routing from scratch.
- **Our Benchmark Standard (`Strict 100.0% + 0 DRC`)**: A PCB routing engine only passes a board when native **`kicad-cli pcb drc --severity-all`** (after fresh copper zone refill via `pcbnew.ZONE_FILLER`) reports:
  - **`0` Unconnected Items (`100.0%` geometric net completion)**
  - **`0` Copper DRC Violations (clearances, track widths, annular rings, hole-to-hole, and rule-area keepouts)**
  - **`0.00000 mm` Footprint Coordinate Drift**

---

## Challenge: Try to Stump Our Router (`$0` 350-DPI Copper Proof)

Have an unrouted KiCad (`.kicad_pcb`), Altium (`.PcbDoc`), Eagle (`.brd`), or Specctra (`.dsn`) board that stalled Freerouting?

1. **Drop It into the Browser (`$0` Upfront)**: **[https://calligraphyeda.com](https://calligraphyeda.com)** (or click one of the **1-Click Sample Boards** at the top of the page).
2. **Inspect the 350-DPI Copper Proof & 3D WebGL View**: Zoom into every fine-pitch pad entry, differential pair, and ground return transition before paying a cent.
3. **Fail-Closed `0-DRC` Guarantee**: Our portal enforces a strict commercial gate — if a board does not achieve `100.0%` net completion and `0` native KiCad copper DRC errors, **it is never billed**.

---

## Visual Proof — High-Density Torture Boards Routed to `100.0%` & `0` DRC

### 1. `Karabas-Nano` — 738 Pads, 928 Connections on Just **2 Copper Layers** (`0` Unconnected, `0` DRC)

Routing 738 pads and 928 connections across only 2 copper layers (`F.Cu` and `B.Cu`) with zero internal plane layers requires global congestion balancing and tight multi-bus channel allocation without trapping inner QFP pins.

| 350-DPI Routed Copper Proof (`F.Cu` + `B.Cu`) | Raytraced 3D Verification |
| :---: | :---: |
| ![Karabas-Nano 2-Layer 738 Pads 0-DRC Copper Proof](assets/karabas_nano_2layer_738pads_0drc_copper.png) | ![Karabas-Nano 2-Layer 738 Pads 3D View](assets/karabas_nano_2layer_738pads_0drc_3d.png) |

### 2. `Decelerator-4030` — 908 Pads, High-Pin-Count Bus Escape (`0` Unconnected, `0` DRC)

| 350-DPI Routed Copper Proof | Raytraced 3D Verification |
| :---: | :---: |
| ![Decelerator-4030 908 Pads 0-DRC Copper Proof](assets/decelerator4030_908pads_0drc_copper.png) | ![Decelerator-4030 908 Pads 3D View](assets/decelerator4030_908pads_0drc_3d.png) |

### 3. `Teensy MCU Breakout` — Mixed-Pitch Signal Integrity & Ground Return Continuity (`0` Unconnected, `0` DRC)

| 350-DPI Routed Copper Proof | Raytraced 3D Verification |
| :---: | :---: |
| ![Teensy MCU Breakout 0-DRC Copper Proof](assets/teensy_mcu_breakout_0drc_copper.png) | ![Teensy MCU Breakout 3D View](assets/teensy_mcu_breakout_0drc_3d.png) |

---

## 13-Board Conquered Benchmark Ledger (`100.0%` Routed / `0` Native KiCad Copper DRC)

All 13 reference and torture boards below can be inspected interactively at **[https://calligraphyeda.com](https://calligraphyeda.com)**:

| # | Board Name | Copper Layers | Pads | Routed Nets / Connections | Unconnected Items | Native KiCad Copper DRC Errors |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | **Karabas-Nano (2-Layer Torture Config)** | `2L` | `738` | `928` connections | **`0` (`100.0%`)** | **`0`** |
| 2 | **Decelerator-4030 High-Pin-Count Accelerator** | `6L` | `940` | `284` nets | **`0` (`100.0%`)** | **`0`** |
| 3 | **Aleste LX Retro Z80/FPGA Motherboard** | `4L` | `1,829` | `236` nets | **`0` (`100.0%`)** | **`0`** |
| 4 | **i.MX8M Mini + LPDDR4 HDI System-on-Module** | `8L` | `1,813` | `520` nets | **`0` (`100.0%`)** | **`0`** |
| 5 | **LiteX M2SDR PCIe Gen2 / RF Transceiver** | `8L` | `1,420` | `412` nets | **`0` (`100.0%`)** | **`0`** |
| 6 | **Antmicro Jetson Nano/Xavier Baseboard** | `6L` | `1,180` | `365` nets | **`0` (`100.0%`)** | **`0`** |
| 7 | **STM32H743 Redundant IMU Flight Controller** | `6L` | `780` | `245` nets | **`0` (`100.0%`)** | **`0`** |
| 8 | **Karabas-Nano 4-Layer FPGA/Retro Computer** | `4L` | `652` | `198` nets | **`0` (`100.0%`)** | **`0`** |
| 9 | **DSP-ADAU1452 32-Bit SigmaDSP Audio Processor** | `4L` | `540` | `168` nets | **`0` (`100.0%`)** | **`0`** |
| 10 | **RP2040 + 3-Phase GaN FOC Motor Controller** | `4L` | `490` | `142` nets | **`0` (`100.0%`)** | **`0`** |
| 11 | **Teensy 4.1 Mixed-Signal Breakout Carrier** | `2L` | `445` | `134` nets | **`0` (`100.0%`)** | **`0`** |
| 12 | **ESP32-S3 IEEE 802.3af PoE Industrial Gateway** | `4L` | `410` | `128` nets | **`0` (`100.0%`)** | **`0`** |
| 13 | **RoyalBlue 54L Custom Mechanical Keyboard Matrix** | `4L` | `388` | `118` nets | **`0` (`100.0%`)** | **`0`** |

---

## Independent Verification Script (`verify_drc_zero.py`)

Never trust a screenshot without running `kicad-cli pcb drc --severity-all` yourself. Use [`verify_drc_zero.py`](verify_drc_zero.py) on any routed `.kicad_pcb` file to refill all copper zones on a temporary copy and verify `unconnected_count == 0` and `copper_drc_error_count == 0`:

```bash
python3 verify_drc_zero.py path/to/routed_board.kicad_pcb
```

---

## Related Open-Source Tools from Calligraphy Systems

- **[vibe-hardware-mcp](https://github.com/calligraphysystems/vibe-hardware-mcp)** — Model Context Protocol (MCP) configuration & CLI for wiring Claude Code, Cursor, and Windsurf to autonomous `0-DRC` PCB synthesis.
- **[calligraphy-kicad-plugin](https://github.com/calligraphysystems/calligraphy-kicad-plugin)** — Official 1-click KiCad Action Plugin (`PCM`) for pre-flight routing quotes and `$0` 350-DPI Copper Proof inspection.
- **Foundry Portal**: [https://calligraphyeda.com](https://calligraphyeda.com)
