# CAN Insight PRO — CAN Bus Decoder & Analyser

A browser-based tool for decoding and analysing heavy-duty vehicle CAN bus data using the **J1939 / FMS (Fleet Management System)** standard. No installation required — just open the HTML file in any modern browser.

> **Privacy Notice:** This tool processes CAN log files entirely in your browser. No data is uploaded to any server. All analysis is performed client-side using JavaScript.

## 🚀 Quick Start

1. Open **[can_insight_v2.html](can_insight_v2.html)** in a modern browser (Chrome, Firefox, Edge, Safari)
2. Click **LOAD LOG CSV** or drag-and-drop a CAN log file
3. Explore decoded data across four tabs: **Raw Data**, **Timeline**, **Tachograph**, **Manual Decode**

### Browser Requirements

| Browser | Minimum Version |
|---------|----------------|
| Chrome  | 90+            |
| Firefox | 88+            |
| Edge    | 90+            |
| Safari  | 14+            |

## 📊 Features

### CAN Insight PRO (`can_insight_v2.html`)
- **64+ J1939/FMS PGN definitions** with full SPN decoding
- **Real-time telemetry dashboard** — RPM, speed, fuel, brake, accelerator, PTO, gear
- **Interactive timeline chart** — multi-trace with zoom/scroll controls
- **Vehicle identification** — automatic VIN and make detection
- **Tachograph data** — RTD (Remote Tachograph Download) decoding
- **Manual decode** — enter any CAN ID & data payload to decode a single frame
- **Export** — PNG, wide PNG, and Excel export for timeline and data overview
- **FAQ & Help** — built-in guide on CAN decoding, changelog, and usage tips

### CAN Log Checker (`can_log_checker.html`)
- **Priority data validation** — pass/partial/fail assessment of key vehicle parameters
- **Timeline graph** — Engine RPM, Accelerator, Brake Pedal, PTO traces
- **3-tier PGN display** — fully decoded, hex-only, and unknown/proprietary
- Lightweight single-file tool for quick CAN log validation

### PGN Library (`pgn_library.js`)
- Standalone J1939/FMS decoder definitions
- 64 PGN groups covering engine, transmission, braking, fuel, electrical, and diagnostics
- Used internally by CAN Insight PRO and CAN Log Checker

## 📁 Repository Structure

```
├── can_insight_v2.html          # Main CAN decoder & analyser (open in browser)
├── can_log_checker.html         # Lightweight CAN log validation tool
├── pgn_library.js               # J1939/FMS PGN decoder definitions
├── can_master_kb.json           # CAN knowledge base
├── calculate_spn5464.py         # Interactive battery charge calculator (Python)
├── CHANGELOG.txt                # Version history
├── TUTORIAL_SUMMARY.txt         # Quick-start tutorial notes
├── LICENSE                      # Proprietary license terms
└── README.md                    # This file
```

## 🔧 How CAN Data is Decoded

CAN (Controller Area Network) uses 29-bit extended identifiers in J1939. Each message contains:

1. **CAN ID** → extract the **PGN (Parameter Group Number)** by right-shifting 8 bits and masking
2. **PGN** → look up the definition to find which **SPNs (Suspect Parameter Numbers)** are carried
3. **SPN** → extract bytes from the 8-byte data payload using offset, length, resolution, and offset values

### Example: Engine RPM (SPN 190)
```
CAN ID:    0CF00400
PGN:       F004 (EEC1 — Electronic Engine Controller 1)
Data:      00 00 00 88 13 00 00 00
SPN 190:   Bytes 3-4 → 0x1388 = 5000 → × 0.125 = 625 RPM
```

## 📖 Learning Resources

### Interactive Calculator
```bash
python3 calculate_spn5464.py
```

## ⚠️ Known Limitations

- Supports J1939 extended (29-bit) CAN IDs only; standard 11-bit frames are not decoded
- CSV files must have columns for CAN ID (or Identifier) and Data bytes
- Tested with IXXAT MiniMon and canAnalyser 3 Mini CSV exports
- No multi-frame (Transport Protocol) reassembly — each frame is decoded independently
- All processing is client-side; very large files (>100 MB) may be slow

## 📜 License

**© 2026 Nigel F. All rights reserved.**

This software is **free to use and share** for personal and commercial CAN log analysis. You may distribute unmodified copies to anyone who needs them.

You may **not** modify, reverse-engineer, or create derivative works from the source code. You may **not** extract or reuse the PGN/SPN library, decoding logic, or UI design in other projects.

See the [LICENSE](LICENSE) file for full terms.

## 🤝 Contributing

Contributions welcome! Please ensure CAN log test files do not contain personally identifiable information (vehicle registration numbers, VINs from real vehicles, etc.).

---

*Built with ❤️ by Nigel F — Powered by CAN INSIGHT PRO*
