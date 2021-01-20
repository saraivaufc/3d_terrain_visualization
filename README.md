# 3D Terrain Visualization

![bigdata-docker](./docs/visualization.png)

### Requirements
* GDAL -- [Homepage](http://www.gdal.org)

### Install Gdal
```shell
$ sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
$ sudo apt-get update
$ sudo apt-get install libgdal-dev
$ sudo apt-get install python3-dev
$ sudo apt-get install gdal-bin python3-gdal
```

### Create and activate a virtual environment
```shell
$ virtualenv env -p python3
$ source env/bin/activate
```

### Install Numpy
```shell
(env) $ pip3 install numpy
```
### Install GDAL
```shell
(env) $ pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

### Install vtk
```shell
(env) $ pip3 install python-vtk
```

### Install Mayavi
```shell
(env) $ pip3 install mayavi PyQt5
```

### Execute
```shell
(env) $ python3 visualize_3d.py landsat_8.tif srtm.tif
```


<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
    <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" />
</a>
<br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
