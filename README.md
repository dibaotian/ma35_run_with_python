# ma35_run_with_python

#### OS 
#### Distributor ID: Ubuntu
#### Description:    Ubuntu 20.04.5 LTS
#### Release:        20.04
#### Codename:       focal
#### kernel 5.15.0-76-generic
#### ama sdk v1.1.2
#### ffmpeg version 5.1.2
#### python version >3.9


create a virtual environment
#>mkdir pyav
#>cd pyav
#>python3.9 -m venv .venv
#>source .venv/bin/activate

1 Downloay pyav source code

#>git clone https://github.com/PyAV-Org/PyAV.git

2 #>cd PyAV

3 Download the ama sdk ffmpeg source code

https://amd.github.io/ama-sdk/v1.1.2/using_ffmpeg.html

https://www.xilinx.com/content/dam/xilinx/guest-resources/2023/video/ma35d_sdk_v1.1.2_ffmpeg.zip

unzip the zip file to a folder , for example ama_ffmpeg

#>unzip ma35d_sdk_v1.1.2_ffmpeg.zip -d ama_ffmpeg

4 config pyav

- export PYAV_PYTHON=python3.9
- source scripts/activate.sh ama_ffmpeg
#>python setup.py build --ffmpeg-dir=ama_ffmpeg

5 install pyav
#>python setup.py install --ffmpeg-dir=ama_ffmpeg






4 #>cd ama_ffmpeg

5 configure

here the pyav does not support static libaray, Building ffmpeg with the flag --enable-shared, --extra-cflags='-fPIC'

#>./configure --extra-cflags='-fPIC'--disable-alsa --disable-libxcb --disable-libxcb-shm --disable-libxcb-xfixes --disable-libxcb-shape --disable-xlib --disable-libmfx --disable-vaapi --disable-vulkan --disable-static --enable-shared --prefix=$PWD --disable-stripping --enable-shared --enable-vpe --enable-libxrm --extra-libs="-L/opt/amd/ama/ma35/lib -lvpi -lroi_scale -llog_ama -lxrm -lxrm_interface -lhugetlbfs -lpthread -lstdc++ -lm -ldl -lrt  /opt/amd/ama/ma35/lib/libxrm.so.1.6.0" --extra-cflags="-I/usr/include -I$PWD -I/opt/amd/ama/ma35/include/xrm_interface/ -I/opt/amd/ama/ma35/include/xrm/ -DSUPPORT_OSAL" --extra-ldflags="-Wl,-rpath=$PWD/libavutil:$PWD/libavfilter:$PWD/libavcodec:$PWD/libavformat:$PWD/libavdevice:$PWD/libswscale:$PWD/libswresample:$PWD:/opt/amd/ama/ma35/lib/"

6 build and install ffmpeg

#>make && make install



8 build pyav
#>build

9 install 
#>pip install .

10 other 
#>sudo apt install python3.9-dev   //if you use python3.9


final got

Processing /home/xilinx/Documents/minx/pyav/PyAV

  Installing build dependencies ... done

  WARNING: Missing build requirements in pyproject.toml for file:///home/xilinx/Documents/minx/pyav/PyAV.

  WARNING: The project does not specify a build backend, and pip cannot fall back to setuptools without 'wheel'.

  Getting requirements to build wheel ... done

  Installing backend dependencies ... done

    Preparing wheel metadata ... done

Building wheels for collected packages: av

  Building wheel for av (PEP 517) ... done

  Created wheel for av: filename=av-13.0.0rc1-cp39-cp39-linux_x86_64.whl size=10299083 sha256=dc70b9be29c2e18e74070c22ed0bf85de69f8cae94c09b13ee4f6fef170bef52

  Stored in directory: /tmp/pip-ephem-wheel-cache-8gdskz3t/wheels/74/94/3e/bd4224ad071fc7aa42b176297800f679c75e80fc3672e13d41

Successfully built av

Installing collected packages: av

Successfully installed av-13.0.0rc1

