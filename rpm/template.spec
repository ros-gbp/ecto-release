Name:           ros-indigo-ecto
Version:        0.6.8
Release:        0%{?dist}
Summary:        ROS ecto package

Group:          Development/Libraries
License:        BSD
URL:            http://ecto.willowgarage.com
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-devel
Requires:       python-xdot
BuildRequires:  boost-devel
BuildRequires:  python-devel
BuildRequires:  ros-indigo-catkin

%description
Ecto is a hybrid C++/Python development framework for constructing and
maintaining pipelines.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 13 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.6.8-0
- Autogenerated by Bloom

