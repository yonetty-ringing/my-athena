usage: configure.py [-h]
                    [--prob {beam,binary_gravity,blast,chem_G14Sod,chem_H2,chem_onecell_sixray,chem_pdr_moving,chem_Pn_grid,chem_turb,chem_uniform,chem_uniform_sixray,collapse,cpaw,cr_diffusion,cr_diffusion_mg,default_pgen,disk,dmr,eos_test,fft,field_loop,field_loop_poles,from_array,gr_blast,gr_bondi,gr_geodesic_infall,gr_linear_wave,gr_mhd_inflow,gr_shock_tube,gr_torus,hb3,hgb,jeans,jet,jgg,kh,linear_wave,lw_implode,magnoh,mignone_advection,noh,orszag_tang,poisson,quirk,rad_linearwave,read_vtk,resist,rotor,rt,scalar_diff,shk_cloud,shock_tube,shu_osher,slotted_cylinder,ssheet,strat,thermal_multigroup,thermal_relaxation,thermal_relaxation_amr,turb,twoibw,visc}]
                    [--coord {cartesian,cylindrical,spherical_polar,minkowski,schwarzschild,kerr-schild,gr_user}]
                    [--eos {adiabatic,isothermal,general/eos_table,general/hydrogen,general/ideal}]
                    [--flux {default,hlle,hllc,lhllc,hlld,lhlld,roe,llf}]
                    [--nghost NGHOST] [--nscalars NSCALARS]
                    [--nspecies NSPECIES] [-b] [-sts] [-s] [-g] [-t] [-debug]
                    [-coverage] [-float] [-mpi] [-omp] [--grav {none,fft,mg}]
                    [-fft] [--fftw_path FFTW_PATH]
                    [--chemistry {gow17,H2,kida,G14Sod}]
                    [--kida_rates {H2,gow17,nitrogen,nitrogen_gas_Sipila}]
                    [--chem_radiation {const,six_ray}]
                    [--chem_ode_solver {cvode,forward_euler}]
                    [--cvode_path CVODE_PATH] [-hdf5] [-h5double]
                    [--hdf5_path HDF5_PATH] [-nr_radiation]
                    [-implicit_radiation] [-cr] [-crdiff]
                    [--cxx {g++,g++-simd,icpx,icpx-old,icpc,icpc-debug,icpc-phi,cray,clang++,clang++-simd,clang++-apple,aocc}]
                    [--ccmd CCMD] [--mpiccmd MPICCMD] [--gcovcmd GCOVCMD]
                    [--cflag CFLAG] [--include INCLUDE] [--lib_path LIB_PATH]
                    [--lib LIB]

Prepare custom Makefile and defs.hpp for compiling Athena++ solver

options:
  -h, --help            show this help message and exit
  --prob {beam,binary_gravity,blast,chem_G14Sod,chem_H2,chem_onecell_sixray,chem_pdr_moving,chem_Pn_grid,chem_turb,chem_uniform,chem_uniform_sixray,collapse,cpaw,cr_diffusion,cr_diffusion_mg,default_pgen,disk,dmr,eos_test,fft,field_loop,field_loop_poles,from_array,gr_blast,gr_bondi,gr_geodesic_infall,gr_linear_wave,gr_mhd_inflow,gr_shock_tube,gr_torus,hb3,hgb,jeans,jet,jgg,kh,linear_wave,lw_implode,magnoh,mignone_advection,noh,orszag_tang,poisson,quirk,rad_linearwave,read_vtk,resist,rotor,rt,scalar_diff,shk_cloud,shock_tube,shu_osher,slotted_cylinder,ssheet,strat,thermal_multigroup,thermal_relaxation,thermal_relaxation_amr,turb,twoibw,visc}
                        select problem generator
  --coord {cartesian,cylindrical,spherical_polar,minkowski,schwarzschild,kerr-schild,gr_user}
                        select coordinate system
  --eos {adiabatic,isothermal,general/eos_table,general/hydrogen,general/ideal}
                        select equation of state
  --flux {default,hlle,hllc,lhllc,hlld,lhlld,roe,llf}
                        select Riemann solver
  --nghost NGHOST       set number of ghost zones
  --nscalars NSCALARS   set number of passive scalars
  --nspecies NSPECIES   set number of chemical species
  -b                    enable magnetic field
  -sts                  enable super-time-stepping
  -s                    enable special relativity
  -g                    enable general relativity
  -t                    enable interface frame transformations for GR
  -debug                enable debug flags; override other compiler options
  -coverage             enable compiler-dependent code coverage flag
  -float                enable single precision
  -mpi                  enable parallelization with MPI
  -omp                  enable parallelization with OpenMP
  --grav {none,fft,mg}  select self-gravity solver
  -fft                  enable FFT
  --fftw_path FFTW_PATH
                        path to FFTW libraries
  --chemistry {gow17,H2,kida,G14Sod}
                        select chemical network
  --kida_rates {H2,gow17,nitrogen,nitrogen_gas_Sipila}
                        select special rates for kida network
  --chem_radiation {const,six_ray}
                        enable and select radiative transfer method for
                        chemistry
  --chem_ode_solver {cvode,forward_euler}
                        ode solver for chemistry
  --cvode_path CVODE_PATH
                        path to CVODE libraries
  -hdf5                 enable HDF5 Output
  -h5double             enable double precision HDF5 output
  --hdf5_path HDF5_PATH
                        path to HDF5 libraries
  -nr_radiation         enable non-relativistic radiative transfer
  -implicit_radiation   enable radiative transfer
  -cr                   enable cosmic ray transport
  -crdiff               enable implicit cosmic ray diffusion
  --cxx {g++,g++-simd,icpx,icpx-old,icpc,icpc-debug,icpc-phi,cray,clang++,clang++-simd,clang++-apple,aocc}
                        select C++ compiler and default set of flags (works w/
                        or w/o -mpi)
  --ccmd CCMD           override for command to use to call (non-MPI) C++
                        compiler
  --mpiccmd MPICCMD     override for command to use to call MPI C++ compiler
  --gcovcmd GCOVCMD     override for command to use to call Gcov utility in
                        Makefile
  --cflag CFLAG         additional string of flags to append to
                        compiler/linker calls
  --include INCLUDE     extra path for included header files (-I<path>); can
                        be specified multiple times
  --lib_path LIB_PATH   extra path for linked library files (-L<path>); can be
                        specified multiple times
  --lib LIB             name of library to link against (-l<lib>); can be
                        specified multiple times

Full documentation of options available at
https://github.com/PrincetonUniversity/athena-public-version/wiki/Configuring