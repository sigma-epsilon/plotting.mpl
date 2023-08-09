import unittest
import numpy as np

from sigmaepsilon.core.testing import SigmaEpsilonTestCase
from sigmaepsilon.mesh.grid import grid
from sigmaepsilon.mesh.utils.topology.tr import Q4_to_T3
from sigmaepsilon.mesh.trimesh import triangulate
from sigmaepsilon.mesh.recipes import circular_disk
from sigmaepsilon.plotting.mpl import triplot


class TestTriplot(SigmaEpsilonTestCase):

    def test_triplot(self):
        gridparams = {
            'size' : (1200, 600),
            'shape' : (30, 15),
            'eshape' : (2, 2),
            'origo' : (0, 0),
            'start' : 0
        }
        coordsQ4, topoQ4 = grid(**gridparams)
        points, triangles = Q4_to_T3(coordsQ4, topoQ4, path='grid')
        triobj = triangulate(points=points[:, :2], triangles=triangles)[-1]
        triplot(triobj)
        
        data = np.random.rand(len(triangles))   
        triplot(triobj, data=data)
        triplot(triobj, hinton=True, data=data)
        
        data = np.random.rand(len(points))
        triplot(triobj, data=data, cmap='bwr') 
        
    def circular_disk(self):
        n_angles = 60
        n_radii = 30
        min_radius = 5
        max_radius = 25
        disk = circular_disk(n_angles, n_radii, min_radius, max_radius)
        triobj = triangulate(points=disk.coords()[:, :2], triangles=disk.topology())[-1]
        triplot(triobj)
        
        
if __name__ == "__main__":
    unittest.main()
