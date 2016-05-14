INSTALL H.264 DRIVERS FOR FIREFOX
=================================

Enable CISCO repo for openh264

    # dnf config-manager --set-enabled fedora-cisco-openh264

Install rpms

    # dnf install mozilla-openh264 gstreamer1-plugin-openh264

Finally install ffmpeg-libs from rpmfusion.

NOTA: Think to enable plugin in Firefox Plugin Page.
