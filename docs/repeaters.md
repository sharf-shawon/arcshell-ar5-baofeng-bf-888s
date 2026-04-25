---
layout: default
title: Repeater Guide
nav_order: 9
description: "How to use Ham radio repeaters with your BaoFeng BF-888S or Arcshell AR-5."
---

# 📡 Repeater Guide

A **repeater** is a special station that receives your signal and re-broadcasts it at much higher power from a tall tower or mountain top. This can extend your range from 2 miles to over 50 miles.

---

## How It Works

1.  **Input Frequency:** The frequency you transmit on (e.g., `442.500`).
2.  **Offset:** The difference between input and output (typically `+5.000` or `-5.000` MHz for UHF).
3.  **Output Frequency:** The frequency you listen on (e.g., `447.500`).
4.  **Tone (CTCSS):** A sub-audible "key" required to "open" the repeater.

---

## Finding Repeaters

Use [RepeaterBook.com](https://www.repeaterbook.com/) to find towers near you. Look for "70cm" or "UHF" repeaters, as those are compatible with your radio.

---

## Programming in CHIRP

| Field | Example Value |
| :--- | :--- |
| **Frequency** | `447.500` (The Output/Listen frequency) |
| **Duplex** | `-` (Minus offset) |
| **Offset** | `5.000` |
| **Tone Mode** | `Tone` |
| **Tone** | `100.0` |

---

## Repeater Etiquette

- **Listen First:** Ensure the repeater isn't already in use.
- **Identify:** You must state your callsign at the beginning and end of your conversation.
- **Be Brief:** Repeaters often have "time-out" timers that will cut you off if you talk for more than 3 minutes.
