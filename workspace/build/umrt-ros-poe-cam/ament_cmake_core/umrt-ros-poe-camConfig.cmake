# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_umrt-ros-poe-cam_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED umrt-ros-poe-cam_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(umrt-ros-poe-cam_FOUND FALSE)
  elseif(NOT umrt-ros-poe-cam_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(umrt-ros-poe-cam_FOUND FALSE)
  endif()
  return()
endif()
set(_umrt-ros-poe-cam_CONFIG_INCLUDED TRUE)

# output package information
if(NOT umrt-ros-poe-cam_FIND_QUIETLY)
  message(STATUS "Found umrt-ros-poe-cam: 1.0.3 (${umrt-ros-poe-cam_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'umrt-ros-poe-cam' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${umrt-ros-poe-cam_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(umrt-ros-poe-cam_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${umrt-ros-poe-cam_DIR}/${_extra}")
endforeach()
