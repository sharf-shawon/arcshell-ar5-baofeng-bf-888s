---
layout: default
title: Compatibility
nav_order: 10
description: "Radio compatibility guide for Arcshell AR-5, BaoFeng BF-888S, and other walkie-talkie brands."
---

# 🤝 Radio Compatibility

Will your Arcshell talk to your friend's Motorola? The answer is **Yes**, but they must be programmed to the same frequency and tone.

---

## 🟢 Compatible Radios

These radios can all communicate with each other if programmed correctly:
- **Other BF-888S Clones:** Pxton PX-888S, Retevis H-777, etc.
- **Consumer FRS/GMRS Radios:** Motorola Talkabout, Midland, Cobra, Onn.
- **Ham Radios:** Any UHF-capable handheld like the BaoFeng UV-5R.

---

## 🔴 Incompatible Radios

Your radio will **NOT** work with:
- **Digital Radios (DMR/P25):** Your radio is analog only.
- **CB Radios:** These use a completely different frequency band (27 MHz).
- **VHF Marine Radios:** These use the 156 MHz band (though some clones are dual-band, the AR-5/BF-888S are typically UHF only).

---

## Matching Privacy Codes

If your friend's radio says they are on "Channel 1, Code 12", you must find the frequency for Channel 1 (462.5625 MHz) and the CTCSS frequency for Code 12 (100.0 Hz) and program those into your radio via CHIRP.

[See our Frequency Charts for common codes →]({{ site.baseurl }}/frequencies/frs-gmrs-chart/)
