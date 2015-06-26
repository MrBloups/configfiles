 xcalib configuration
---------------------

Xcalib is a tool for calibrate your screen manually or from an icc profile.  

Installation:  

    sudo dnf install xcalib

Get the icc profile for your screen back:  

    wget http://www.notebookcheck.net/uploads/tx_nbc2/Lenovo_S300_glare_1366x768__LG_Display_LP133WH2_TLE1_.icc

Usage:  

    xcalib -clear ; xcalib ICCPROFILE
