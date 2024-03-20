# Arcshel AR-5 Radios Documentation Repository

Welcome to the Arcshel AR-5 Radios Documentation Repository! 📻

## Table of Contents

- [Introduction](#introduction)
- [User's Manual](#users-manual)
- [Default Channel Frequencies](#default-channel-frequencies)
- [FRS Channel Frequencies](#frs-channel-frequencies)
- [DIY Programming Cable](#diy-programming-cable)
- [Programming Software](#programming-software)
- [How to Contribute](#how-to-contribute)
- [Feedback and Suggestions](#feedback-and-suggestions)

## Introduction

This repository serves as a comprehensive resource for beginners and enthusiasts who have purchased Arcshel AR-5 radios. Whether you're seeking detailed information or guidance on usage, this repository aims to simplify the learning process by gathering valuable insights, tips, and resources in one place.

Feel free to contribute any valuable information you have to make this repository more helpful for others.

## User's Manual

If you've misplaced your user's manual, you can find a copy on [Manuals.Plus](https://manuals.plus/arcshell/ar-5-rechargeable-long-range-two-way-radio-manual.pdf).

## Default Channel Frequencies

Here are the default channel configurations for Arcshel AR-5 radios:

| Loc | Frequency | Tone  | Mode | ToneSql | DTCS | Code |
|-----|-----------|-------|------|---------|------|------|
| 1   | 462.125   | TSQL  |      | 69.3    |      |      |
| 2   | 462.225   |       |      |         |      |      |
| 3   | 462.325   |       |      |         |      |      |
| 4   | 462.425   | TSQL  |      | 103.5   |      |      |
| 5   | 462.525   | TSQL  |      | 114.8   |      |      |
| 6   | 462.625   | TSQL  |      | 127.3   |      |      |
| 7   | 462.725   | TSQL  |      | 136.5   |      |      |
| 8   | 462.825   | TSQL  |      | 162.2   |      |      |
| 9   | 462.925   | DTCS  |      |         | 25   |      |
| 10  | 463.025   | DTCS  |      |         | 51   |      |
| 11  | 463.125   | DTCS  |      |         | 125  |      |
| 12  | 463.225   | DTCS  |      |         | 155  |      |
| 13  | 463.525   | DTCS  |      |         | 465  |      |
| 14  | 450.225   | DTCS  |      |         | 23   |      |
| 15  | 460.325   |       |      |         |      |      |
| 16  | 469.95    | TSQL  |      | 203.5   |      |      |


## FRS Channel Frequencies 

Here are the FRS channel frequencies:

| FRS Channel | Frequency | FRS Power | FRS Bandwidth | GMRS Power | GMRS Bandwidth | Notes/Usage                       |
|-------------|-----------|-----------|---------------|------------|----------------|-----------------------------------|
| 01          | 462.5625  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 02          | 462.5875  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 03          | 462.6125  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 04          | 462.6375  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 05          | 462.6625  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 06          | 462.6875  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 07          | 462.7125  | 2 W       | 12.5 kHz      | 5 W        | 20 kHz         | (1)                               |
| 08          | 467.5625  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 09          | 467.5875  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 10          | 467.6125  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 11          | 467.6375  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 12          | 467.6625  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 13          | 467.6875  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 14          | 467.7125  | 0.5 W     | 12.5 kHz      | 0.5 W      | 12.5 kHz       | (1)                               |
| 15          | 462.5500  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 16          | 462.5750  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 17          | 462.6000  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 18          | 462.6250  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 19          | 462.6500  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 20          | 462.6750  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 21          | 462.7000  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
| 22          | 462.7250  | 2 W       | 12.5 kHz      | 50 W       | 20 kHz         | (1) (2)                           |
|             | 467.5500  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.5750  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.6000  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.6250  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.6500  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.6750  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.7000  |           |               | 50 W       | 20 kHz         | (3)                               |
|             | 467.7250  |           |               | 50 W       | 20 kHz         | (3)                               |

**Notes**

(1) Shared FRS and GMRS simplex.
(2) GMRS repeater output.
(3) GMRS repeater input only.

*[Credits](https://wiki.radioreference.com/index.php/FRS/GMRS_combined_channel_chart)*

For suggested and unofficial channel usages, see the [Family Radio Service and General Mobile Radio Service wiki articles](https://wiki.radioreference.com/index.php/FRS/GMRS_combined_channel_chart).

## DIY Programming Cable

To program your Arcshel AR-5 radios, you'll need a programming cable like this one:

![Baofeng USB Programming Cable](Baofeng-USB-Programming-Cable.webp)

You can either purchase one or create your own using a USB to Serial FTDI converter. Here's a diagram for the DIY programming cable:

![DIY Programming Cable Diagram](cp2102-radio-programmer.jpg)

*Credits: Diagram sourced from [Miklor.com](https://www.miklor.com/COM/UV_Technical.php)*

## Programming Software

Once you have a programming cable, you may download [CHIRP](https://chirpmyradio.com/projects/chirp/wiki/Download) to program your radio. For guidance on using CHIRP, refer to this [YouTube video](https://www.youtube.com/watch?v=XQ_JzivmjyI) from NotaRubicon Productions.

## How to Contribute

Contributions to this documentation repository are highly encouraged! Whether you're a seasoned expert or a fellow beginner, your input is invaluable in enhancing the quality and comprehensiveness of this resource. Please feel free to submit a pull request with any insights, tips, or additional resources.

## Feedback and Suggestions

Your feedback is essential in improving this documentation repository. If you have any suggestions or encounter any issues, please don't hesitate to open an issue or reach out to the repository maintainer.

Let's work together to make the Arcshel AR-5 Radios Documentation Repository a valuable resource for everyone!
