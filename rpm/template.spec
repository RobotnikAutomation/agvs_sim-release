Name:           ros-kinetic-agvs-gazebo
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS agvs_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/agvs_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-agvs-description
Requires:       ros-kinetic-agvs-pad
Requires:       ros-kinetic-agvs-robot-control
Requires:       ros-kinetic-effort-controllers
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-joint-state-controller
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-velocity-controllers
BuildRequires:  ros-kinetic-catkin

%description
The agvs_gazebo package. Launch files and worlds to run Gazebo.

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
* Wed Jul 20 2016 Roberto Guzmán <rguzman@robotnik.es> - 0.1.2-0
- Autogenerated by Bloom

