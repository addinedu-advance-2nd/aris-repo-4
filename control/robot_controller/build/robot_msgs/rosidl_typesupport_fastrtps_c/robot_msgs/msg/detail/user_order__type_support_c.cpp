// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/user_order__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robot_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robot_msgs/msg/detail/user_order__struct.h"
#include "robot_msgs/msg/detail/user_order__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // action, icecream, topping, topping_type
#include "rosidl_runtime_c/string_functions.h"  // action, icecream, topping, topping_type

// forward declare type support functions


using _UserOrder__ros_msg_type = robot_msgs__msg__UserOrder;

static bool _UserOrder__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _UserOrder__ros_msg_type * ros_message = static_cast<const _UserOrder__ros_msg_type *>(untyped_ros_message);
  // Field name: action
  {
    const rosidl_runtime_c__String * str = &ros_message->action;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: icecream
  {
    const rosidl_runtime_c__String * str = &ros_message->icecream;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: topping
  {
    const rosidl_runtime_c__String * str = &ros_message->topping;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: topping_type
  {
    const rosidl_runtime_c__String * str = &ros_message->topping_type;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _UserOrder__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _UserOrder__ros_msg_type * ros_message = static_cast<_UserOrder__ros_msg_type *>(untyped_ros_message);
  // Field name: action
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->action.data) {
      rosidl_runtime_c__String__init(&ros_message->action);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->action,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'action'\n");
      return false;
    }
  }

  // Field name: icecream
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->icecream.data) {
      rosidl_runtime_c__String__init(&ros_message->icecream);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->icecream,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'icecream'\n");
      return false;
    }
  }

  // Field name: topping
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->topping.data) {
      rosidl_runtime_c__String__init(&ros_message->topping);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->topping,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'topping'\n");
      return false;
    }
  }

  // Field name: topping_type
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->topping_type.data) {
      rosidl_runtime_c__String__init(&ros_message->topping_type);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->topping_type,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'topping_type'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t get_serialized_size_robot_msgs__msg__UserOrder(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _UserOrder__ros_msg_type * ros_message = static_cast<const _UserOrder__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name action
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->action.size + 1);
  // field.name icecream
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->icecream.size + 1);
  // field.name topping
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->topping.size + 1);
  // field.name topping_type
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->topping_type.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _UserOrder__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robot_msgs__msg__UserOrder(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t max_serialized_size_robot_msgs__msg__UserOrder(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: action
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: icecream
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: topping
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: topping_type
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = robot_msgs__msg__UserOrder;
    is_plain =
      (
      offsetof(DataType, topping_type) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _UserOrder__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_robot_msgs__msg__UserOrder(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_UserOrder = {
  "robot_msgs::msg",
  "UserOrder",
  _UserOrder__cdr_serialize,
  _UserOrder__cdr_deserialize,
  _UserOrder__get_serialized_size,
  _UserOrder__max_serialized_size
};

static rosidl_message_type_support_t _UserOrder__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_UserOrder,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robot_msgs, msg, UserOrder)() {
  return &_UserOrder__type_support;
}

#if defined(__cplusplus)
}
#endif
