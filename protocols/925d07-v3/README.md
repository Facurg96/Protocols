# PCR Prep

### Author
[Opentrons](https://opentrons.com/)

## Categories
* PCR
	* PCR Prep

## Description

This protocol performs a custom PCR prep from 4 source 96-well RNA plate to a single 384-well destination plate. The transfer scheme is shown below.

---

### Labware
* [Opentrons 20ul tips](https://shop.opentrons.com/collections/opentrons-tips)
* Corning 96 Well Plate 360 ul Flat
* Custom 384 Well Plate 100 ul
* Generic PCR Strips in [96-well aluminum block](https://shop.opentrons.com/collections/hardware-modules/products/aluminum-block-set)

### Pipettes
* [P20 Multi Channel Pipette](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)

### Modules
* [Temperature Module GEN2](https://shop.opentrons.com/collections/hardware-modules/products/tempdeck)

---

### Deck Setup
![deck layout](https://opentrons-protocol-library-website.s3.amazonaws.com/custom-README-images/925d07/deck.png)

---

### Process
1. Input your protocol parameters above.
2. Download your protocol and unzip if needed.
3. Upload your custom labware to the [OT App](https://opentrons.com/ot-app) by navigating to `More` > `Custom Labware` > `Add Labware`, and selecting your labware files (.json extensions) if needed.
4. Upload your protocol file (.py extension) to the [OT App](https://opentrons.com/ot-app) in the `Protocol` tab.
5. Set up your deck according to the deck map.
6. Calibrate your labware, tiprack and pipette using the OT App. For calibration tips, check out our [support articles](https://support.opentrons.com/en/collections/1559720-guide-for-getting-started-with-the-ot-2).
7. Hit 'Run'.

### Additional Notes
If you have any questions about this protocol, please contact the Protocol Development Team by filling out the [Troubleshooting Survey](https://protocol-troubleshooting.paperform.co/).

###### Internal
9250d7
