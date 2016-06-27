"""User provided customizations.

Here one changes the default arguments for compiling _gpaw.so (serial)
and gpaw-python (parallel).

Here are all the lists that can be modified:
    
* libraries
* library_dirs
* include_dirs
* extra_link_args
* extra_compile_args
* runtime_library_dirs
* extra_objects
* define_macros
* mpi_libraries
* mpi_library_dirs
* mpi_include_dirs
* mpi_runtime_library_dirs
* mpi_define_macros

To override use the form:
    
    libraries = ['somelib', 'otherlib']

To append use the form

    libraries += ['somelib', 'otherlib']
"""

# compiler = 'gcc'
# mpicompiler = 'mpicc'  # use None if you don't want to build a gpaw-python
# mpilinker = 'mpicc'
# platform_id = ''
#hdf5 = False
compiler = './icc.py'
mpicompiler = './icc.py'
mpilinker = 'MPICH_CC=gcc mpicc'

scalapack = True

library_dirs = ['/apps/python/2.7.8/lib/python2.7/site-packages/numpy/core/lib','/apps/intel/parallel_studio_2015/composer_xe_2015.0.090/mkl/lib/intel64'] #, '/apps/fftw3/intel/avx/3.3.4/lib']
libraries = [ 'mkl_intel_lp64' ,'mkl_sequential' ,'mkl_core',
             'mkl_lapack95_lp64','mkl_blas95_lp64',
             'mkl_scalapack_lp64', 
             'mkl_blacs_openmpi_lp64',
             'pthread'
             ]
include_dirs+=['/apps/openmpi/intel-2015/1.8.4/include']
library_dirs+=['/apps/openmpi/intel-2015/1.8.4/lib64']
include_dirs += ['/apps/python/2.7.8/lib/python2.7/site-packages/numpy/core/include']
libraries += ['xc']
library_dirs+=['/home/r/kls49/lib/lib']
include_dirs+=['/home/r/kls49/lib/include']
# Use ScaLAPACK:
# Warning! At least scalapack 2.0.1 is required!
# See https://trac.fysik.dtu.dk/projects/gpaw/ticket/230
define_macros += [('GPAW_NO_UNDERSCORE_CBLACS', '1')]
define_macros += [('GPAW_NO_UNDERSCORE_CSCALAPACK', '1')]
define_macros += [("GPAW_ASYNC",1)]
define_macros += [("GPAW_MPI2",1)]
