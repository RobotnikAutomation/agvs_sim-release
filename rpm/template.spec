Name:           ros-kinetic-agvs-sim
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS agvs_sim package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/agvs_sim
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-agvs-control
Requires:       ros-kinetic-agvs-gazebo
Requires:       ros-kinetic-agvs-robot-control
Requires:       ros-kinetic-agvs-sim-bringup
BuildRequires:  ros-kinetic-catkin

%description
agvs Gazebo simulation packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Aug 19 2016 Roberto Guzmán <rguzman@robotnik.es> - 0.1.3-0
- Autogenerated by Bloom

* Wed Jul 20 2016 Roberto Guzmán <rguzman@robotnik.es> - 0.1.2-0
- Autogenerated by Bloom

