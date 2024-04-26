xilinx@X570-AORUS-PRO:~/Documents/minx/ma35_run_with_python$ sudo dpkg -l amd-ama*
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name              Version          Architecture Description
+++-=================-================-============-=================================
hi  amd-ama-core      1.1.2-2403291822 amd64        Supernova
hi  amd-ama-driver    1.1.2-2403291822 amd64        Supernova
hi  amd-ama-ffmpeg    1.1.2-2403291822 amd64        Supernova
hi  amd-ama-gstreamer 1.1.2-2403291822 amd64        Supernova
hi  amd-ama-xma       1.1.2-2403291822 amd64        Supernova

sudo apt remove amd-ama-ffmpeg -y
sudo apt remove amd-ama-gstreamer -y
sudo apt remove amd-ama-xma -y
sudo apt remove amd-ama-core -y

/lib/modules/5.15.0-76-generic/updates/dkms/ama_transcoder.ko

sudo apt-mark unhold amd-ama-driver amd-ama-core amd-ama-xma amd-ama-ffmpeg amd-ama-gstreamer