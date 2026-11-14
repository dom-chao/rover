#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "umrt-arm-ros-firmware::umrt-arm-ros-firmware" for configuration ""
set_property(TARGET umrt-arm-ros-firmware::umrt-arm-ros-firmware APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(umrt-arm-ros-firmware::umrt-arm-ros-firmware PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libumrt-arm-ros-firmware.so"
  IMPORTED_SONAME_NOCONFIG "libumrt-arm-ros-firmware.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS umrt-arm-ros-firmware::umrt-arm-ros-firmware )
list(APPEND _IMPORT_CHECK_FILES_FOR_umrt-arm-ros-firmware::umrt-arm-ros-firmware "${_IMPORT_PREFIX}/lib/libumrt-arm-ros-firmware.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
