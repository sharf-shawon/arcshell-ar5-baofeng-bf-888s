---
layout: default
title: Step-by-Step Guide
parent: Programming
nav_order: 2
description: "Walkthrough for programming Arcshell AR-5 and BaoFeng BF-888S radios with custom frequencies."
---

# 📝 Step-by-Step Programming Guide

Follow these steps to safely program your radio.

---

## 1. Backup Factory Settings (CRITICAL)

Before you change anything, save the original settings. If you make a mistake, you can always revert to this file.

1.  Connect your radio and click **Radio > Download from Radio**.
2.  Once the download completes, click **File > Save As**.
3.  Name it `My-Radio-Original-Backup.img` and store it in a safe place.

---

## 2. Enter Your Channels

You will see a spreadsheet-like view. Here is what each column means:

| Column | What to enter |
| :--- | :--- |
| **Frequency** | The RX frequency (e.g., `446.000`). |
| **Name** | A label for the channel (max 6 characters). |
| **Tone Mode** | Use `Tone` for simple privacy codes or `TSQL` for repeaters. |
| **Tone** | The CTCSS tone frequency (e.g., `100.0`). |
| **Duplex** | Use `Off` for simplex (direct) or `+` / `-` for repeaters. |
| **Power** | `High` (5W) for range, `Low` (0.5W) for battery saving. |

---

## 3. Recommended Starter Channels

If you have your Ham license, try these:

| Ch | Frequency | Name | Use Case |
| :--- | :--- | :--- | :--- |
| 1 | 446.000 | CALL | National 70cm Calling Frequency |
| 2 | 446.500 | CHAT | Simplex Chat |
| 3 | (Local) | RPT 1 | Your nearest local repeater |

---

## 4. Upload to Radio

Once you have entered your desired channels:
1.  Click **Radio > Upload to Radio**.
2.  Verify the COM port and model.
3.  Click **OK**.
4.  **Wait** for the red light on the radio to stop flashing. The radio will reboot.

---

## 5. Test

Disconnect the cable and test your channels. Try talking to a friend or listening to a local repeater to confirm your settings are correct.
