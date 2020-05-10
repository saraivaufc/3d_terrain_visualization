import argparse
import os

import numpy as np
from osgeo import gdal
from mayavi import mlab
from tvtk.api import tvtk
from tvtk.common import configure_input_data, is_old_pipeline

def visualize_3d(texture_file, dem_file):
    dem_datasource = gdal.Open(dem_file)
    dem_data = dem_datasource.ReadAsArray()

    texture_image = tvtk.TIFFReader(file_name=texture_file)


    texture=tvtk.Texture()
    texture.interpolate=0
    texture.input_connection = texture_image.output_port

    transform = tvtk.Transform()
    transform.rotate_z(-90)

    texture.transform = transform


    fig = mlab.figure(size=(800, 800), bgcolor=(0.16, 0.28, 0.46))

    surface = mlab.surf(dem_data, color=(1,1,1), warp_scale=0.1)
    surface.actor.enable_texture = True
    surface.actor.tcoord_generator_mode = 'plane'
    surface.actor.actor.texture = texture
    surface.actor.texture.repeat = False

    mlab.view(azimuth=0, elevation=None, distance=2000, figure=fig)

    mlab.show()

parser = argparse.ArgumentParser("visualize_3d")
parser.add_argument("texture", nargs='?', help="Raster file in the 0-255 scale with 3-bands to use as a texture.", type=str)
parser.add_argument("dem", nargs='?', help="Raster file to use as the z axis of the visualization.", type=str)

args = parser.parse_args()

visualize_3d(args.texture, args.dem)
