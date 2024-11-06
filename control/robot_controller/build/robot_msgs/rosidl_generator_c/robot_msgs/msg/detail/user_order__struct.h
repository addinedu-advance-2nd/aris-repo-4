// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'action'
// Member 'icecream'
// Member 'topping'
// Member 'topping_type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/UserOrder in the package robot_msgs.
typedef struct robot_msgs__msg__UserOrder
{
  rosidl_runtime_c__String action;
  rosidl_runtime_c__String icecream;
  rosidl_runtime_c__String topping;
  rosidl_runtime_c__String topping_type;
} robot_msgs__msg__UserOrder;

// Struct for a sequence of robot_msgs__msg__UserOrder.
typedef struct robot_msgs__msg__UserOrder__Sequence
{
  robot_msgs__msg__UserOrder * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__UserOrder__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__USER_ORDER__STRUCT_H_
