# CLI Log Analyzer

A lightweight, high-performance Command Line Interface (CLI) tool written in Python to stream, filter, and analyze system log files. 

This tool is designed to help software engineers efficiently sift through massive production logs by streaming files line-by-line (maintaining a $O(1)$ memory footprint) rather than loading entire files into RAM.

---

## 🚀 Features

* **Memory Efficient:** Streams files line-by-line, making it safe to open multi-gigabyte log files without crashing your system.
* **Multi-Filter System:** Filter logs dynamically by specific keywords, specific dates, or both simultaneously (using logical `AND` matching).
* **Case-Insensitive Search:** Built-in substring matching handles mixed-case searches smoothly while preserving original log formatting in the output.
* **Automatic Metrics:** Scans the entire file to provide a total count of `[ERROR]` and `[WARNING]` logs, regardless of the active filters applied.
* **Robust CLI Parsing:** Uses Python's native `argparse` library to handle arguments cleanly and generate automatic help screens.
* **Graceful Error Handling:** Catches standard file-system exceptions to prevent ugly stack traces and provide human-readable errors.

---

## 🛠️ Tech Stack & Concepts Used

* **Language:** Python 3
* **Libraries:** `argparse`, `sys`
* **Architectural Patterns:** Modular procedural design (separation of configuration and execution logic), file streaming, conditional flag verification.

---

