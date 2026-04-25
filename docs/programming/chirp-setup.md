---
layout: default
title: CHIRP Setup
parent: Programming
nav_order: 1
description: "Installing CHIRP software and setting up USB programming cable drivers for BaoFeng radios."
---

# 🛠️ CHIRP Setup

CHIRP is the free, open-source industry standard for programming handheld radios. It works on Windows, macOS, and Linux.

---

## 1. Download CHIRP
Always download CHIRP from the official website to ensure you have the latest version (CHIRP-next).

- **Official Download:** [chirpmyradio.com](https://chirpmyradio.com/projects/chirp/wiki/Download)

---

## 2. Install Drivers
This is the most common hurdle. Most cheap programming cables use "clone" chips that require specific drivers.

- **Windows 10/11:** Usually handles drivers automatically. If you see a yellow triangle in Device Manager, try the [Prolific](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225) or [CH340](http://www.wch-ic.com/downloads/CH341SER_EXE.html) drivers.
- **macOS:** May require manual driver installation and permission in "Security & Privacy".
- **Linux:** Most drivers are built-in, but you may need to add your user to the `dialout` group:
  `sudo usermod -aG dialout $USER` (Log out and back in after running).

---

## 3. Connect the Hardware
1.  **Turn the radio OFF.**
2.  Plug the USB cable into your computer.
3.  Plug the 2-pin connector into the radio. **Push hard** until it clicks; it needs a very snug connection.
4.  **Turn the radio ON** and rotate the volume to about 50-70%.

---

## 4. Verify the Connection
In CHIRP, go to **Radio > Download from Radio**. 
- **Port:** Select the one that says "USB" or "COM3/4".
- **Vendor:** Select `Baofeng`.
- **Model:** Select `BF-888S` (This works for Arcshell AR-5 and Pxton PX-888S as well).

If you see a progress bar, you are connected! If not, check our [Troubleshooting]({{ site.baseurl }}/troubleshooting/) page.
